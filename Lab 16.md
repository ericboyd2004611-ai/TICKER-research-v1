# Lab 16 — What Was Knowable on the Decision Date?

## Question

On 31 March 2026, what did the data actually say, and how much of what we see now came later?

## Inputs and method

The supplied training table contains 12 rows for AAA, BBB, and CCC. The decision date is **2026-03-31**, inclusive: a publication on that date would be knowable.

`asof.py` stores the editable table and decision date at the top and uses only the Python standard library. It applies the four rules in the specified order. Exact duplicates are identified using ticker, month measured, publication date, and index; the source row number is an identifier, not part of duplicate detection.

The signal is `(latest month index / previous calendar month index - 1) × 100`. The naive comparison keeps the latest publication for each ticker and measured month without the decision-date cutoff, after excluding missing tickers and duplicates.

## Row funnel

| Rule | Rows removed | Source row numbers | Rows remaining |
|---|---:|---|---:|
| Starting table | — | — | 12 |
| 1. Quarantine missing ticker | 1 | 11 | 11 |
| 2. Remove exact duplicate | 1 | 7 | 10 |
| 3. Remove publication after decision date | 3 | 3, 8, 10 | 7 |
| 4. Keep latest revision available by decision date | 1 | 2 | 6 |

Row 4 supersedes row 2 because its March 25 revision was already published by March 31. Row 10 cannot supersede row 12 in the as-of panel because row 10 was not published until April 5.

## As-of panel

| Source row | Ticker | Month measured | Published on | Index |
|---|---|---|---|---:|
| 1 | AAA | 2026-01 | 2026-02-10 | 101.0 |
| 4 | AAA | 2026-02 | 2026-03-25 | 103.0 |
| 5 | BBB | 2026-01 | 2026-02-10 | 98.0 |
| 6 | BBB | 2026-02 | 2026-03-10 | 97.0 |
| 9 | CCC | 2026-01 | 2026-02-10 | 110.0 |
| 12 | CCC | 2026-02 | 2026-03-10 | 111.0 |

## Signals

| Ticker | As-of comparison | As-of signal | Naive comparison | Naive signal |
|---|---|---:|---|---:|
| AAA | February / January | +1.98% | March / February | +5.83% |
| BBB | February / January | −1.02% | March / February | −5.15% |
| CCC | February / January | +0.91% | February / January | +1.82% |

## Interpretation

On March 31, the latest knowable month was February for all three tickers. AAA's index rose from 101 to its already-revised value of 103, BBB fell from 98 to 97, and CCC rose from 110 to 111.

Three later publications change the naive view: AAA's March index of 109 and BBB's March index of 92 were published April 10; CCC's revised February index of 112 was published April 5. Using them for a March 31 decision introduces look-ahead bias.

AAA's naive signal exceeds its as-of signal by 3.85 percentage points, and BBB's is 4.13 points lower, using unrounded calculations. These compare different measured months, so they are not revision-only effects. CCC's naive signal is 0.91 points higher solely because of a later revision to the same measured month. These are index-change signals, not demonstrated trading returns.

## Verification and reproduction

Ran `python asof.py` successfully. Its output contained the four-rule funnel, the six-row as-of panel, and an as-of and naive signal for each ticker. All removals, panel values, and signals are computed from the editable inputs rather than hard-coded answers.

Reran the script against the supplied expected results: **every row number, signal month, and two-decimal signal matches**. No debugging changes were needed. In particular, AAA uses row 4's revised February index of 103 and removes row 2's older value of 104. Its as-of signal is therefore **+1.98%**, not the **+2.97%** that keeping row 2 would produce. CCC's naive February signal uses the later revision, while its as-of February signal uses row 12.

From this folder, run:

```sh
python asof.py
```

## Rule 4 — line-by-line code explanation

The publication-date cutoff happens first:

```python
knowable = [r for r in unique if r["published"] <= decision]
panel = latest_publications(knowable)
```

The first line keeps only rows published on or before the decision date. The second passes those eligible rows into the revision-selection function. The function itself does not apply the cutoff; this lets the naive comparison reuse it with all cleaned rows.

```python
def latest_publications(rows):
    latest = {}
    for row in rows:
        key = row["ticker"], row["month"]
        if key not in latest or row["published"] > latest[key]["published"]:
            latest[key] = row
        elif (row["published"] == latest[key]["published"]
              and row["index"] != latest[key]["index"]):
            raise ValueError(f"Conflicting values for {key} on {row['published']}")
    return sorted(latest.values(), key=lambda r: (r["ticker"], r["month"]))
```

| Code line | Explanation |
|---|---|
| `def latest_publications(rows):` | Defines a function that selects one publication for each ticker and measured month. |
| `latest = {}` | Creates an empty dictionary to hold the selected rows. |
| `for row in rows:` | Examines each input row in turn. |
| `key = row["ticker"], row["month"]` | Creates a pair such as `("AAA", "2026-02")`, grouping observations about the same ticker and month. |
| `if key not in latest or row["published"] > latest[key]["published"]:` | Accepts the row if this pair has not been seen, or if its publication is newer than the stored publication. It compares publication dates, not index values. |
| `latest[key] = row` | Stores the whole row, replacing the older selection when necessary. |
| `elif (row["published"] == latest[key]["published"]` | Starts a check for a publication-date tie within the same ticker and month. |
| `and row["index"] != latest[key]["index"]):` | Completes the check: the tied publications have different index values. |
| `raise ValueError(...)` | Stops with an explanatory error because conflicting values on the same publication date cannot be resolved by this rule. |
| `return sorted(latest.values(), key=lambda r: (r["ticker"], r["month"]))` | Returns the selected rows sorted by ticker and measured month. |

For AAA February, row 2 is stored first. Row 4 replaces it because March 25 is later than March 10. Its index of 103 is selected even though it is lower than 104. For CCC February, row 10 is excluded by the cutoff before revision selection, leaving row 12 eligible.

## Look-ahead bias — explanation

**1. What is look-ahead bias?**

Look-ahead bias occurs when information published after a decision date is used to make or evaluate that earlier decision. This makes a strategy appear better informed than it could actually have been.

**2. How do event time, publication time, and revisions work?**

- **Event time:** the period the observation measures, such as March 2026.
- **Publication time:** when the observation becomes available. A March observation published April 10 is unavailable on March 31.
- **Revision time:** when an updated value becomes available. A revision can be used only if it was published by the decision date.

The filter first excludes publications after the decision date, then selects the latest remaining publication for each ticker and measured month. Selecting the latest revision before applying the cutoff could incorrectly discard an older, knowable value.

**3. Why does AAA's +5.83% look better than what was knowable?**

On March 31, AAA's January index was 101 and its latest available February index was 103, revised on March 25. Its latest knowable signal was `(103 / 101 - 1) × 100 = +1.98%`.

The naive signal is `(109 / 103 - 1) × 100 = +5.83%`. It looks like stronger upward momentum, but the March index of 109 was not published until April 10. It was therefore impossible to calculate that signal using the supplied information available on March 31.

The two signals also describe different periods: the as-of signal measures February versus January, while the naive signal measures March versus February. The stronger signal comes from seeing a later month. It does not establish that a trade would have earned a higher return.

