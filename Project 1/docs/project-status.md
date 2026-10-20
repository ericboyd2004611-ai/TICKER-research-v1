# Project status and next work

**Initial planning record. Current completion inventory: [HANDOFF.md](../HANDOFF.md).**
The corrected model, linked economic statements, terminal application, 20 checks,
clean-directory rehearsal, three reviewed PDF drafts and video rehearsal scripts
are now prepared. Earlier planning items below describe the starting audit.

Current update: an explicit operating exit, exit-multiple sensitivity and
existing-holder financing value are implemented. Existing NuScale Lab 11 records
are preserved; their timing/tool boundary requires verification rather than
automatically repeating the exercise. See docs/lab11-evidence-map.md.

## Reusable coursework

- Week 3 DCF: diagnostic only. Negative starting FCFF, placeholder growth/WACC,
  and weighted-average EPS shares prevent using its price as a final valuation.
- Week 5 linked statements: copied into src, with assumptions and existing tests.
  Useful conditional downside case; successful commercialization is excluded.
- Week 5 Lab 10 and Week 6 sensitivities: additional existing evidence to reconcile
  before choosing a final model version; not silently merged into this snapshot.

## Required analytical work

Progress: the commercialization scenario engine, sensitivity analysis and
reverse valuation are implemented as AI-generated illustrations. See
`output/commercialization-report.md`. Contract economics, assumption approval,
point-in-time completeness and full statement reconciliation remain open.

1. Fix one valuation/information date and keep post-date evidence separate.
2. Verify each historical anchor with filing date, period, statement/note, locator,
   units and URL. Separate cash, short-term investments, longer-term investments,
   restricted cash, and operating obligations without overlap.
3. Reconcile current share classes, exchangeable interests and awards to the same
   date; disclose funding-driven future dilution separately.
4. Build a sourced commercialization scenario: timing, contract economics,
   ENTRA1 obligations, reinvestment, cash requirements and financing. Do not infer
   binding module orders from preliminary agreements.
5. Develop a valuation range and comparable-company policy; explain disagreement
   between approaches instead of mechanically averaging them.
6. Propagate a downside shock through the linked statements and explain its effect
   on liquidity, valuation, and the committee action.
7. Set monitoring owner/frequency and measurable reversal conditions.

## Student-owned evidence still needed

- Actual submitted Edition A PDF and first successful receipt/attempt timestamp.
  User reports it was submitted; no receipt has been inspected in this workspace.
- Locked Changed-Input Record: student writes prediction with AI off before the
  designated run, freezes the evidence, executes AI closed, and reconciles results.
  No generated prediction or completed record is supplied here.
- Edition B and evidence-backed A-to-B table, final memo/deck, validation PDF,
  three personally recorded videos, corrected transcripts, accessible repository
  and completed manifest. Final PDFs have not been created.

## Date decision for Edition B

The submitted baseline remains unchanged. Its stated December 31, 2025 valuation
date conflicts with reliance on a later-published annual report. Either establish
a later information date and refresh every input, or explicitly present the old
model as retrospective supporting evidence. Do not label the current snapshot a
point-in-time December 2025 recommendation.
