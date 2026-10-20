# Cost of capital and terminal-value policy

The proposed CAPM build uses the September 1, 2026 Damodaran market inputs: 4.75% Treasury reference and 4.14% implied equity risk premium under the same unadjusted Treasury convention. These are dated market reference inputs, not today's quote. Source: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm (previous-month entry; October values are excluded).

Cost of equity = risk-free rate + beta × equity risk premium. A proposed beta of 2.0 produces 13.03%. Beta is an explicit research judgment for development-stage cyclicality and execution exposure; it is not an empirical regression result. The January 2026 US machinery cash-adjusted unlevered beta of 0.89 provides a mature supplier reference. A mature utility beta is inappropriate for this stage. Source: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html. The proposed uplift from 0.89 to 2.0 needs personal acceptance or replacement with a defensible beta estimate. It is not a disguised measured fact.

The no-financial-debt base uses equity weight 100%, debt weight 0%. WACC = Ke × E/(D+E) + Kd × (1-tax) × D/(D+E) = 13.03%. Kd is not estimated for nonexistent financial debt and contributes zero. No debt tax shield is claimed. The 25% normalized tax assumption affects operating taxes; loss years do not receive a cash tax refund. Leases remain in operating costs. Future leverage would require a separate credit spread and capital-weight decision. NuScale source: https://www.sec.gov/Archives/edgar/data/1822966/000182296626000085/smr-20260630.htm, Liquidity.

The original 15% rate remains a reference stress case, not a CAPM estimate. The workbench's CAPM preset uses 13.03%; its base reset restores 15% to reproduce the existing scenario record. Candidate-versus-reference values appear in output/valuation-methods.md.

## WACC control bounds

8–25% are analyst stress endpoints, not a confidence interval supplied by a source. With 4.75% risk-free and 4.14% ERP they imply betas about 0.785–4.891 under all-equity financing. This spans a mature equipment reference and a high-risk development stress. The lower endpoint is not a claim that SMR can raise money at 8%. Source inputs and beta-reference limitations are above. An out-of-range API input is rejected visibly.

## Growth and terminal checks

The main method is an assumed operating exit, for which g has no effect. The separate WACC–g grid uses normalized next-year FCFF / (WACC-g), discounted from end-2036. Next-year FCFF is already calculated; it is not multiplied by (1+g) again. Grid assumptions are distinct from the operating-exit base.

Growth control bounds 0–8% span contraction-free mature growth through a deliberately aggressive stress; they are judgmental, not evidence of achievable perpetual growth. The PMA requires at least 5% annual fee escalation (Section 1(c), https://www.sec.gov/Archives/edgar/data/1822966/000182296625000144/a101-partnershipmileston.htm). The grid therefore blocks a uniform FCFF perpetuity below that floor. 5–6% cases are conditional mathematical sensitivities only, with uniform future FCFF growth imposed; no perpetual terminal case is established as an economically defensible base. A lower-growth base would require an explicit contract transition, margin path, and reinvestment/ROIC normalization.

PV terminal / enterprise value is shown explicitly; nonpositive EV receives NM and negative explicit cash flows can make the ratio exceed 100%. Rate monotonicity is measured on fixed cash flows at 10%, 13.03%, 15%, and 20%. Mixed-sign FCFF does not mathematically guarantee decreasing EV, so failures are retained.
