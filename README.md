[Lab 07 Checkout Draft.md](https://github.com/user-attachments/files/32260042/Lab.07.Checkout.Draft.md)
# Lab 07 Checkout Draft

This is a working draft for the Brightspace Lab 07 attempt. Use only entries that match your actual target, frozen policy, sources, and in-class work. The Asbury exercise and the official synthetic teaching case are different calculations.

## Target and decision

- **Prior Week 3 target:** NuScale Power (SMR), based on `Week 03/Lab 6 Complete.md`. **Confirm this is also your Lab 07 target.**
- **Metric warning if SMR is the target:** Its FY2025 Form 10-K reports a $2.17 diluted loss per Class A share and a $689.571M operating loss. A conventional positive P/E cannot be calculated from the reported loss. Check any proposed EV/EBITDA denominator and its definition before using it. [NuScale FY2025 Form 10-K, filed February 26, 2026](https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm).
- **Valuation/as-of date:** [Enter the date used in your Lab 07 peer work. Do not silently reuse Week 3's date.]
- **Decision being supported:** [Enter the specific decision.]

## Frozen peer-selection policy

[Paste your policy exactly as written before AI suggested candidates. Do not rewrite it after viewing prices or candidate lists.]

## Official synthetic teaching-case known answers

The Week 4 synthetic target has EBITDA of $80 million, net income of $40 million, cash of $50 million, debt of $300 million, and 50 million diluted shares. These are **not** SMR or Asbury inputs.

| Peer | EV / EBITDA | Equity value / net income |
|---|---:|---:|
| Alpha | 10.0x | 12.0x |
| Beta | 16.0x | 20.0x |
| Gamma | 9.0x | 15.0x |
| Delta | 16.0x | 15.0x |

- Median EV/EBITDA: **13.0x**. Enterprise value = 13.0 x $80M = **$1,040M**. Equity value = $1,040M + $50M cash - $300M debt = **$790M**. At 50M diluted shares, **$15.80 per share**.
- Applying the **lowest** synthetic peer EV/EBITDA (9.0x) produces **$9.40 per share** after the bridge; applying the **highest** (16.0x) produces **$20.60 per share**. These are the synthetic enterprise-route peer endpoints, not the Asbury range.
- Median P/E: **15.0x**. Equity value = 15.0 x $40M = **$600M**. At 50M diluted shares, **$12.00 per share**. No cash/debt bridge is applied to P/E.
- Qualified precedent at 14.0x EV/EBITDA: EV = **$1,120M**, equity = **$870M**, or **$17.40 per share**. Do not mechanically average these three routes.

## Asbury P/E exercise and changed-peer test

- AutoNation P/E: **10.037825x**; Group 1 Automotive P/E: **11.450149x**; median: **10.743987x**.
- Asbury's peer-implied range: **$215.81 to $246.18**; median-implied price: **$231.00**.
- Asbury's December 31, 2024 closing price was **$243.03**. The median peer-implied price is **$12.03 below** that closing price.
- **Remove AutoNation:** Group 1 remains. The median-implied price becomes **$246.18**, an **increase of $15.18** from the two-peer estimate. With only one peer, this is a reference estimate without a range.
- **Prediction before result:** Removing Group 1, the higher-multiple peer, should lower the implied price.
- **Observed result:** Removing Group 1 leaves AutoNation and lowers the estimate to **$215.81**, a **$15.18 decrease** from the two-peer estimate. With one peer, there is one reference estimate, not a low-to-high range.
- **Peer decision:** Do not change the original Group 1 disposition solely because its removal changes the estimate. Change it only if your frozen policy and verified business evidence warrant doing so.
- **Asbury EV/EBITDA status:** The calculator does not produce an Asbury enterprise-route estimate yet. The supplied Asbury case has no target EBITDA, cash, debt, diluted-share count, or peer enterprise values and EBITDA. These need verified, date-aligned inputs before the result is meaningful.

## AI candidate audit for your chosen target

Enter every distinct candidate from the Codex and Gemini lists. A source must support each important fact and have a date. AI output alone is not evidence.

**AI use reported so far:** Codex. Do not claim Gemini was used unless you actually ran it. The local Lab 07 instructions call for sending the same frozen-policy candidate request to both systems; if only Codex was used, record that honestly in the AI disclosure and check the open Brightspace attempt for how to handle the missing second list.

| Candidate | Suggested by | Source and date actually checked | Policy facts checked | Accept / qualify / reject | Consequence |
|---|---|---|---|---|---|
| [Candidate] | [Codex / Gemini / both] | [Filing or other source, date] | [Public/operating, model, scale, geography, metric definition] | [Disposition] | [Keep in median / sensitivity only / exclude] |

## Verified peer multiples and implied range for your target

[Enter the verified peer table excerpt, the period and definition for each denominator, and your own EV/EBITDA and P/E calculations. If SMR remains your target, check whether its reported earnings and EBITDA make these multiples meaningful. Do not turn a negative or undefined denominator into a positive valuation multiple.]

- **Enterprise route:** [Median EV/EBITDA] x [target EBITDA] = [EV]; then + [cash] - [debt] = [equity]; divide by [diluted shares] = [price per share].
- **Equity route:** [Median P/E] x [target net income] = [equity]; divide by [diluted shares] = [price per share]. No cash/debt bridge.
- **Implied range and endpoint methods:** [Low value and route] to [high value and route].
- **Changed-peer test for your chosen target:** [Candidate, prediction, recalculated value/range, direction, explanation]. If no candidate is borderline, say so; do not manufacture a rejection.
- **Limitation:** [What this peer set cannot tell the decision maker.]

## Brightspace checkout fields to complete personally

Lab date; teammates or learning partners and your contribution; target, as-of date, and decision; frozen policy; synthetic known answers; candidate dispositions; verified peer table excerpt; implied range; changed-peer test; limitation; optional link; AI disclosure; session token from the board; in-person attendance declaration; truth attestation; receipt confirmation. Add the ungraded growth note before submitting.

## Sources used for this draft

- `Course Materials/lessons/week-04/slides-session-07.md`
- `Course Materials/lessons/week-04/teach-comps-worked-example.md`
- `Week 03/Lab 6 Complete.md`
- `Week 04/peer_pe_valuation.py`
