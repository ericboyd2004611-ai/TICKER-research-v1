"""AI-generated scenario FCFF engine. USD millions and shares in millions.

Illustrative economics, not sourced module prices. Equity funding is a liquidity
diagnostic, excluded from FCFF and the valuation denominator to avoid charging
negative FCFF and financing dilution against the same investor twice.
"""
from datetime import date
import math


def validate(common, scenario):
    for value in common.values():
        if isinstance(value, (int, float)) and not math.isfinite(value):
            raise ValueError('Nonfinite assumption')
    if common['discount_rate'] <= common['terminal_growth'] or common['terminal_growth'] < 0:
        raise ValueError('Require discount rate > terminal growth >= zero')
    if common['discount_rate'] <= 0 or common['opex_growth'] < 0:
        raise ValueError('Require positive discount rate and nonnegative cost growth')
    if common.get('terminal_method', 'none') not in ('none', 'exit_multiple', 'perpetuity'):
        raise ValueError('Unknown terminal method')
    for key in ('exit_ebitda_multiple', 'authorized_class_a_shares_m'):
        if key in common and common[key] < 0:
            raise ValueError(f'Negative assumption: {key}')
    for key in ('cash_tax_rate', 'incremental_nwc_fraction_revenue',
                'capex_fraction_revenue', 'depreciation_fraction_opening_ppe',
                'existing_services_margin', 'installed_services_margin'):
        if not 0 <= common[key] <= 1:
            raise ValueError(f'Invalid fraction: {key}')
    if not 0 <= common['equity_issuance_fee'] < 1 or common['funding_issue_price_fraction_market'] <= 0:
        raise ValueError('Invalid funding assumptions')
    for key in ('assumed_july_august_cash_use_m', 'annual_cash_opex_m',
                'minimum_annual_capex_m', 'minimum_cash_m', 'additional_equity_claims_m',
                'annual_existing_services_revenue_m', 'installed_module_annual_service_revenue_m',
                'opening_ppe_m', 'historical_pma_first_tranche_m'):
        if common[key] < 0:
            raise ValueError(f'Negative assumption: {key}')
    if common['historical_pma_cohort_modules'] <= 0 or common['pma_first_tranche_fraction'] <= 0:
        raise ValueError('Invalid historical fee derivation')
    if not 0 < common['historical_pma_fraction_paid_2025'] <= 1:
        raise ValueError('Historical payment fraction must be in (0, 1]')
    if common['pma_annual_escalation'] < 0 or common['module_price_annual_growth'] <= -1:
        raise ValueError('Invalid fee escalation or module-price growth')
    if not math.isclose(sum(common[k] for k in
                           ('pma_first_tranche_fraction', 'pma_binding_fraction', 'pma_purchase_fraction')), 1):
        raise ValueError('PMA fractions must sum to one')
    for key in ('pma_binding_lead_years', 'pma_purchase_lead_years'):
        if not isinstance(common[key], int) or common[key] < 0:
            raise ValueError('Lead years must be nonnegative integers')
    deliveries = scenario['deliveries']
    if len(deliveries) != common['last_forecast_year'] - common['first_forecast_year'] + 1:
        raise ValueError('Delivery schedule length mismatch')
    if any(not isinstance(n, int) or n < 0 for n in deliveries):
        raise ValueError('Deliveries must be nonnegative integers')
    if not 0 <= scenario['module_gross_margin_before_pma'] <= 1 or scenario['module_price_m'] <= 0:
        raise ValueError('Invalid module economics')


def run(common, scenario, research):
    validate(common, scenario)
    c = common
    start = date.fromisoformat(c['valuation_date'])
    if start.year != c['first_forecast_year'] - 1:
        raise ValueError('Stub year must immediately precede full forecast')
    money, owners = research['usd_millions'], research['shares']
    initial_liquidity = sum(money[k] for k in ('cash', 'short_term_investments', 'investments'))
    initial_liquidity -= c['assumed_july_august_cash_use_m']
    if initial_liquidity < 0:
        raise ValueError('Assumed lag burn exceeds opening liquidity')
    denominator = sum(owners[k] for k in ('class_a', 'exchangeable_llc_units', 'options', 'rsus')) / 1e6
    if denominator <= 0 or research['price_usd'] <= 0:
        raise ValueError('Shares and market price must be positive')
    # Infer a 2025 fee scale from the 50% historical cash installment, avoiding
    # treating a mixed-year escalated expense as a 2025 base. Still an inference.
    fee = c['historical_pma_cash_paid_2025_m'] / c['historical_pma_fraction_paid_2025'] / c['historical_pma_cohort_modules'] / c['pma_first_tranche_fraction']
    first_year, last_year = c['first_forecast_year'], c['last_forecast_year']
    # Schedule each cohort's fees before delivery. First historical cohort has
    # already paid tranche 1; later cohorts pay all tranches. A steady run rate
    # beyond the horizon supplies fee obligations falling inside the horizon.
    delivery_schedule = dict(zip(range(first_year, last_year + 1), scenario['deliveries']))
    for y in range(last_year + 1, last_year + max(c['pma_binding_lead_years'], c['pma_purchase_lead_years']) + 1):
        delivery_schedule[y] = scenario['deliveries'][-1]
    fees = {}
    served = 0
    for year, count in delivery_schedule.items():
        already_first_paid = min(count, max(0, c['historical_pma_cohort_modules'] - served))
        later_modules = count - already_first_paid
        binding_year = year - c['pma_binding_lead_years']
        purchase_year = year - c['pma_purchase_lead_years']
        if binding_year < start.year or purchase_year < start.year:
            if count:
                raise ValueError('Scenario requires modeled fee payments before valuation year')
        fees[binding_year] = fees.get(binding_year, 0) + fee * (
            count * c['pma_binding_fraction'] + later_modules * c['pma_first_tranche_fraction'])
        fees[purchase_year] = fees.get(purchase_year, 0) + fee * count * c['pma_purchase_fraction']
        served += count
    for year in fees:
        fees[year] *= (1 + c['pma_annual_escalation']) ** (year - 2025)
    cash, ppe, nwc, installed = initial_liquidity, c['opening_ppe_m'], 0.0, 0
    # Hold nonliquid legacy assets and liabilities at their reported balances.
    # Opening cash-use allowance reduces book equity rather than acting as a plug.
    fixed_other_assets = money['total_assets'] - sum(money[k] for k in
                         ('cash', 'short_term_investments', 'investments')) - money['ppe']
    liabilities = money['total_liabilities']
    equity = money['consolidated_equity'] - c['assumed_july_august_cash_use_m']
    # Opening PP&E overrides require an explicit matching change in opening equity.
    equity += ppe - money['ppe']
    if not math.isclose(cash + ppe + fixed_other_assets, liabilities + equity, abs_tol=1e-7):
        raise ValueError('Opening economic balance sheet does not reconcile')
    cumulative_funding, new_shares, total_fees = 0.0, 0.0, 0.0
    rows = []
    for year in range(start.year, last_year + 1):
        fraction = (date(year, 12, 31) - start).days / 365.25 if year == start.year else 1.0
        t = (date(year, 12, 31) - start).days / 365.25
        n = delivery_schedule.get(year, 0)
        base_service = c['annual_existing_services_revenue_m'] * fraction
        recurring = installed * c['installed_module_annual_service_revenue_m'] * fraction
        module_revenue = n * scenario['module_price_m'] * (1 + c['module_price_annual_growth']) ** (year - start.year)
        revenue = base_service + recurring + module_revenue
        gross_profit = (base_service * c['existing_services_margin']
                        + recurring * c['installed_services_margin']
                        + module_revenue * scenario['module_gross_margin_before_pma'])
        opex = c['annual_cash_opex_m'] * (1 + c['opex_growth']) ** (year - start.year) * fraction
        pma = fees.get(year, 0.0)
        total_fees += pma
        capex = max(c['minimum_annual_capex_m'] * fraction, revenue * c['capex_fraction_revenue'])
        depreciation = ppe * c['depreciation_fraction_opening_ppe'] * fraction
        # PMA cash expense timing is an economic convention, not GAAP guidance.
        ebitda = gross_profit - opex - pma
        ebit = ebitda - depreciation
        tax = max(0.0, ebit) * c['cash_tax_rate']
        target_nwc = max(0.0, module_revenue + recurring) * c['incremental_nwc_fraction_revenue']
        delta_nwc = target_nwc - nwc
        fcff = ebit - tax + depreciation - capex - delta_nwc
        pre_funding_cash = cash + fcff
        funding = max(0.0, c['minimum_cash_m'] - pre_funding_cash)
        issue_price = research['price_usd'] * c['funding_issue_price_fraction_market']
        issued = funding / (1 - c['equity_issuance_fee']) / issue_price
        cumulative_funding += funding
        new_shares += issued
        end_cash = pre_funding_cash + funding
        income = ebit - tax
        closing_equity = equity + income + funding
        closing_assets = end_cash + ppe + capex - depreciation + target_nwc + fixed_other_assets
        balance_gap = closing_assets - liabilities - closing_equity
        if abs(balance_gap) > 1e-7:
            raise ValueError('Forecast economic balance sheet does not reconcile')
        row = dict(year=year, fraction=fraction, discount_years=t, delivered=n,
                   installed_at_start=installed, revenue=revenue, gross_profit=gross_profit,
                   cash_opex=opex, pma_cash=pma, ebitda=ebitda, depreciation=depreciation,
                   ebit=ebit, cash_tax=tax, capex=capex, delta_nwc=delta_nwc, fcff=fcff,
                   opening_liquidity=cash, pre_funding_liquidity=pre_funding_cash,
                   funding_net=funding, issued_shares_m=issued,
                   closing_liquidity=end_cash, ppe=ppe + capex - depreciation,
                   incremental_nwc=target_nwc,
                   net_income=income, cfo=income + depreciation - delta_nwc,
                   cfi=-capex, cff=funding, fixed_other_assets=fixed_other_assets,
                   liabilities=liabilities, opening_equity=equity,
                   equity=closing_equity, assets=closing_assets, balance_gap=balance_gap,
                   pv_fcff=fcff / (1 + c['discount_rate']) ** t)
        if not all(math.isfinite(v) for v in row.values()):
            raise ValueError('Nonfinite forecast')
        if abs(end_cash - cash - fcff - funding) > 1e-7:
            raise ValueError('Cash roll-forward failed')
        rows.append(row)
        cash, ppe, nwc = end_cash, row['ppe'], target_nwc
        equity = closing_equity
        installed += n
    # Normalize the mature run rate using all three PMA tranches. Do not carry
    # sunk historical tranche relief or a one-year working-capital release forever.
    g = c['terminal_growth']
    last = rows[-1]
    next_module_revenue = scenario['deliveries'][-1] * scenario['module_price_m'] * (1 + c['module_price_annual_growth']) ** (last_year + 1 - start.year)
    next_services = installed * c['installed_module_annual_service_revenue_m']
    terminal_revenue = next_module_revenue + next_services + c['annual_existing_services_revenue_m']
    normalized_gross = (next_module_revenue * scenario['module_gross_margin_before_pma']
                        + next_services * c['installed_services_margin']
                        + c['annual_existing_services_revenue_m'] * c['existing_services_margin'])
    normalized_opex = c['annual_cash_opex_m'] * (1 + c['opex_growth']) ** (last_year + 1 - start.year)
    normalized_fee = scenario['deliveries'][-1] * fee * (1 + c['pma_annual_escalation']) ** (last_year + 1 - 2025)
    terminal_da = last['ppe'] * c['depreciation_fraction_opening_ppe']
    terminal_ebit = normalized_gross - normalized_opex - normalized_fee - terminal_da
    terminal_capex = max(c['minimum_annual_capex_m'], terminal_revenue * c['capex_fraction_revenue'])
    terminal_nwc_change = (next_module_revenue + next_services) * c['incremental_nwc_fraction_revenue'] - last['incremental_nwc']
    terminal_fcff = (terminal_ebit - max(0.0, terminal_ebit) * c['cash_tax_rate']
                     + terminal_da - terminal_capex - terminal_nwc_change)
    method = c.get('terminal_method', 'none')
    if method == 'perpetuity' and g < c['pma_annual_escalation']:
        raise ValueError('A growing perpetuity cannot ignore the contractual fee escalation floor')
    normalized_ebitda = normalized_gross - normalized_opex - normalized_fee
    if method == 'exit_multiple':
        tv = max(0.0, normalized_ebitda) * c['exit_ebitda_multiple']
        terminal_status = 'ASSUMED_EXIT_MULTIPLE' if normalized_ebitda > 0 else 'NONPOSITIVE_EXIT_EBITDA_ZERO_OPERATING_EXIT'
    elif method == 'perpetuity':
        tv = max(0.0, terminal_fcff) / (c['discount_rate'] - g)
        terminal_status = 'ASSUMED_PERPETUITY' if terminal_fcff > 0 else 'NO_GOING_CONCERN_TERMINAL_VALUE'
    else:
        tv = 0.0
        terminal_status = 'WITHHELD_UNSUPPORTED_STEADY_STATE'
    pv_tv = tv / (1 + c['discount_rate']) ** last['discount_years']
    pv_explicit = sum(r['pv_fcff'] for r in rows)
    ev = pv_explicit + pv_tv
    equity_raw = ev + initial_liquidity - money['reported_debt'] - c['additional_equity_claims_m']
    final_shares = denominator + new_shares
    terminal_equity = max(0.0, tv + cash - money['reported_debt'] - c['additional_equity_claims_m'])
    shareholder_pv_per_share = terminal_equity / final_shares / (1 + c['discount_rate']) ** last['discount_years']
    # Existing investors supply no new cash in this alternative. All operating
    # losses already reduce cash, and new investors buy shares at the assumed
    # fixed issue price. Do not subtract PV(FCFF) again from this terminal payoff.
    funding_price = research['price_usd'] * c['funding_issue_price_fraction_market']
    funding_valuation_checks = []
    for row in rows:
        if row['funding_net']:
            modeled_share_pv_at_raise = terminal_equity / final_shares / (1 + c['discount_rate']) ** (last['discount_years'] - row['discount_years'])
            funding_valuation_checks.append(dict(year=row['year'], assumed_issue_price=funding_price,
                    modeled_value_at_raise=modeled_share_pv_at_raise,
                    subscription_supported_by_model=modeled_share_pv_at_raise >= funding_price))
    capacity_exceeded = final_shares > c.get('authorized_class_a_shares_m', float('inf'))
    return dict(name=scenario['name'], assumptions=scenario, common=c, rows=rows,
                opening_liquidity=initial_liquidity, gross_award_shares_m=denominator,
                implied_pma_total_per_module_m=fee, total_explicit_pma_cash=total_fees,
                terminal_fcff=terminal_fcff, terminal_status=terminal_status,
                terminal_method=method, normalized_exit_ebitda=normalized_ebitda,
                terminal_enterprise_value=tv,
                pv_explicit_fcff=pv_explicit, pv_terminal=pv_tv, enterprise_value=ev,
                equity_value_unfloored=equity_raw, equity_value=max(0.0, equity_raw),
                value_per_share=max(0.0, equity_raw) / denominator,
                funding_net_m=cumulative_funding, diagnostic_new_shares_m=new_shares,
                diagnostic_existing_holder_fraction=denominator / (denominator + new_shares),
                investor_exit_value_per_initial_share=shareholder_pv_per_share,
                terminal_equity_proceeds=terminal_equity,
                final_economic_shares_m=final_shares,
                share_authorization_capacity_exceeded=capacity_exceeded,
                funding_valuation_checks=funding_valuation_checks,
                first_funding_year=next((r['year'] for r in rows if r['funding_net'] > 0), None),
                status='ILLUSTRATIVE_UNAPPROVED_NOT_A_PRICE_TARGET')
