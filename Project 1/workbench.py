"""Local browser workbench. Every edit reruns the calculation engine in memory."""
from copy import deepcopy
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import math
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from commercialization import run
from valuation_methods import wacc, terminal_diagnostics, rate_diagnostic, gordon_cell

# Bounds are research-informed stress choices; sources do not disclose exact
# commercial-price or margin endpoints. The UI states this distinction.
CONTROLS={
 'module_price_m':dict(label='Supplier revenue / module ($m)',min=100,max=400,step=5,source='docs/assumption-register.md#module-price'),
 'module_gross_margin_before_pma':dict(label='Module margin before PMA',min=0,max=.60,step=.01,source='docs/assumption-register.md#module-margin'),
 'discount_rate':dict(label='WACC',min=.08,max=.25,step=.0025,source='docs/cost-of-capital.md'),
 'exit_ebitda_multiple':dict(label='Operating exit / EBITDA',min=0,max=10,step=.5,source='docs/peer-analysis.md'),
 'pma_annual_escalation':dict(label='Annual PMA escalation',min=.05,max=.10,step=.005,source='https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm'),
 'terminal_growth':dict(label='Terminal growth (perpetuity only)',min=0,max=.08,step=.005,source='docs/cost-of-capital.md'),
}


def load():
    return (json.loads((ROOT/'data/commercialization-scenarios.json').read_text()),
            json.loads((ROOT/'data/research-inputs.json').read_text()))


def defaults(scenario_index=1):
    config,_=load()
    c=config['common'];s=config['scenarios'][scenario_index]
    # The frozen 15% case stays the reference; the CAPM result is a separate preset.
    values={k:(s[k] if k in s else c[k]) for k in CONTROLS}
    return dict(values,scenario_index=scenario_index,terminal_method='exit_multiple')


def calculate(changes):
    config,research=load()
    checks=[]
    def check(name,passed,detail): checks.append(dict(name=name,passed=bool(passed),detail=detail))
    index=changes.get('scenario_index',1)
    if type(index) is not int or not 0<=index<len(config['scenarios']):
        return dict(valid=False,checks=[dict(name='Scenario',passed=False,detail='Choose a listed scenario.')],result=None)
    values=defaults(index);values.update(changes)
    common=deepcopy(config['common']);scenario=deepcopy(config['scenarios'][index])
    unknown=set(changes)-set(CONTROLS)-{'scenario_index','terminal_method'}
    check('Recognized controls',not unknown,'Only exposed drivers can be edited.')
    for key,spec in CONTROLS.items():
        v=values[key]
        valid=type(v) in (int,float) and math.isfinite(v) and spec['min']<=v<=spec['max']
        check(spec['label'],valid,f"Allowed {spec['min']} to {spec['max']}; source/basis: {spec['source']}")
        if valid:
            (scenario if key in scenario else common)[key]=v
    method=values.get('terminal_method')
    check('Terminal method',method in ('exit_multiple','perpetuity','none'),'Choose operating exit, conditional perpetuity, or no operating exit.')
    common['terminal_method']=method
    check('WACC exceeds growth',common['discount_rate']>common['terminal_growth'],'WACC must exceed g; reset or lower growth.')
    check('Perpetuity fee path',method!='perpetuity' or common['terminal_growth']>=common['pma_annual_escalation'],
          'Growth below the 5% contractual fee floor cannot sustain this simplified perpetuity. Use operating exit or explicitly model a transition.')
    if not all(x['passed'] for x in checks):
        return dict(valid=False,checks=checks,result=None,values=values)
    try:
        result=run(common,scenario,research)
    except (ValueError,OverflowError) as error:
        check('Engine validation',False,str(error))
        return dict(valid=False,checks=checks,result=None,values=values)
    check('Balance sheets reconcile',all(abs(r['balance_gap'])<1e-7 for r in result['rows']),'Assets equal liabilities plus equity in every year.')
    feasibility=[dict(name='Share authorization proxy',passed=not result['share_authorization_capacity_exceeded'],detail='Future modeled shares must fit the current 662m proxy.'),
                 dict(name='Assumed financing supported',passed=all(x['subscription_supported_by_model'] for x in result['funding_valuation_checks']),detail='Modeled future subscriber value must cover the assumed issue price; funding is not guaranteed.')]
    rates=sorted(set([.10,.1303,.15,.20,common['discount_rate']]))
    grid=[dict(wacc=rate,growth=g,**gordon_cell(result,rate,g,common['pma_annual_escalation'])) for rate in rates for g in (.02,.025,.03,.05,.06)]
    return dict(valid=True,checks=checks,feasibility=feasibility,result=result,values=values,
                terminal=terminal_diagnostics(result),monotonicity=rate_diagnostic(result,rates),growth_grid=grid)


class Handler(BaseHTTPRequestHandler):
    def send_json(self,payload,status=200):
        raw=json.dumps(payload,allow_nan=False).encode()
        self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        if self.path=='/':
            raw=(ROOT/'web/index.html').read_bytes()
            self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.end_headers();self.wfile.write(raw)
        elif self.path=='/api/config':
            cap=json.loads((ROOT/'data/cost-of-capital.json').read_text())
            config,_=load()
            self.send_json(dict(controls=CONTROLS,defaults=defaults(),presets=[defaults(i) for i in range(len(config['scenarios']))],scenarios=[s['name'] for s in config['scenarios']],cost_of_capital=wacc(cap)))
        elif self.path=='/api/methods':
            p=ROOT/'output/valuation-methods.json'
            if not p.exists():self.send_json({'status':'Run python3 build_methods.py'});return
            import hashlib
            record=json.loads(p.read_text())
            if any(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=expected for name,expected in record['source_sha256'].items()):
                self.send_json({'status':'Method evidence is stale. Run python3 build_methods.py.'});return
            self.send_json(record)
        elif self.path.startswith('/docs/') and self.path.endswith('.md') and '/' not in self.path[6:]:
            p=ROOT/self.path.lstrip('/')
            if p.is_file():
                self.send_response(200);self.send_header('Content-Type','text/plain; charset=utf-8');self.end_headers();self.wfile.write(p.read_bytes())
            else: self.send_error(404)
        else:self.send_error(404)
    def do_POST(self):
        if self.path!='/api/calculate':self.send_error(404);return
        try:
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=16384:raise ValueError('Invalid request size')
            payload=json.loads(self.rfile.read(size))
            if not isinstance(payload,dict):raise ValueError('Expected control object')
            self.send_json(calculate(payload))
        except (ValueError,TypeError) as e:self.send_json(dict(error=str(e)),400)
    def log_message(self,*args):pass


def serve(port=8765):
    server=ThreadingHTTPServer(('127.0.0.1',port),Handler)
    print(f'NuScale live workbench: http://127.0.0.1:{port}',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()


if __name__=='__main__':serve()
