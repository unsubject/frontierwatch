# Weekly Central Bank Monetary Policy Briefing — Specification

**Version:** 1.0
**Created:** 2026-04-05
**Author:** Simon Lee / Claude
**Status:** Final
**Notion:** https://www.notion.so/leesimon/Monetary-Watch-339110455975801d87c3f743c78200ab

---

## 1. Purpose & Use Case

A weekly reference briefing on global central bank monetary policy, designed for **personal research**. The briefing is a factual input layer — no editorial angle baked in.

## 2. Scope

### 2.1 Central Banks Covered (13)

Ordered by approximate nominal GDP of jurisdiction.

| # | Central Bank | Abbreviation | Currency |
|---|---|---|---|
| 1 | Federal Reserve (US) | Fed | USD |
| 2 | People's Bank of China | PBoC | CNY |
| 3 | European Central Bank | ECB | EUR |
| 4 | Bank of Japan | BoJ | JPY |
| 5 | Reserve Bank of India | RBI | INR |
| 6 | Bank of England | BoE | GBP |
| 7 | Bank of Canada | BoC | CAD |
| 8 | Banco Central do Brasil | BCB | BRL |
| 9 | Bank of Korea | BoK | KRW |
| 10 | Reserve Bank of Australia | RBA | AUD |
| 11 | Central Bank of the Republic of Turkey | CBRT | TRY |
| 12 | Swiss National Bank | SNB | CHF |
| 13 | South African Reserve Bank | SARB | ZAR |

### 2.2 Content Categories (ranked by priority)

1. **Rate decisions & forward guidance** — policy rate changes, holds, vote splits, updated dot plots / projections, forward guidance language shifts
2. **Open market operations** — QE/QT pace changes, repo/reverse repo facility adjustments, balance sheet policy, liquidity injections/withdrawals, FX interventions
3. **Regulatory & supervisory changes** — reserve requirement changes, macroprudential measures, capital/liquidity rule updates, new regulatory proposals
4. **Published research & working papers** — staff working papers, financial stability reports, monetary policy reports (only if they contain material new findings or signal shifts)
5. **Official speeches & testimony** — governor/deputy speeches, parliamentary/congressional testimony (only if they contain new forward-looking signals beyond the latest statement)

### 2.3 Depth

**Signal-focused.** Only material actions, shifts, and surprises. Routine operations that match prior guidance are omitted or noted in a single line. The test: *would this change a market participant's base case?*

### 2.4 Time Horizon

Rolling **7-day window** ending on the briefing date, every week on Sunday at 1000 US Eastern Time.

## 3. Source Hierarchy

**Official sources only.** Each central bank's own website, press releases, meeting minutes, and published research. No wire services, no analyst commentary, no market pricing data.

Primary source URLs:

| Bank | Primary Source |
|---|---|
| Fed | federalreserve.gov |
| PBoC | pbc.gov.cn |
| ECB | ecb.europa.eu |
| BoJ | boj.or.jp |
| RBI | rbi.org.in |
| BoE | bankofengland.co.uk |
| BoC | bankofcanada.ca |
| BCB | bcb.gov.br |
| BoK | bok.or.kr |
| RBA | rba.gov.au |
| CBRT | tcmb.gov.tr |
| SNB | snb.ch |
| SARB | resbank.co.za |

## 4. Output Format

**Structured Markdown** — suitable for Notion page import or direct reading.

## 5. Document Structure

```
# Weekly Monetary Policy Briefing
## Week ending: [YYYY-MM-DD]

---

### Quick-Reference Table

| Bank | Policy Rate | Policy Direction | Last Action | Last Action Date | Next Meeting |
|------|------------|-----------------|-------------|-----------------|--------------|
| Fed  | x.xx%      | Easing/Holding/Tightening | +/- / hold  | YYYY-MM-DD      | YYYY-MM-DD   |
| PBoC | ...        | ...             | ...         | ...             | ...          |
| ECB  | ...        | ...             | ...         | ...             | ...          |
| ...  | ...        | ...             | ...         | ...             | ...          |

---

### Cross-Bank Analysis

Brief prose (3–5 sentences) identifying:
- Directional convergence or divergence across banks this week
- Notable policy regime gaps (e.g., one bank cutting while others hold)
- Any emerging coordination or conflict signals

---

### 1. Federal Reserve (US)

**Rate Decision & Forward Guidance**
[Material developments only, or "No action this week."]

**Open Market Operations**
[QT pace, repo facilities, balance sheet changes, or "No material change."]

**Regulatory & Supervisory**
[New rules, proposals, or "Nothing material."]

**Research & Publications**
[Staff papers, reports with signal value, or "Nothing material."]

**Speeches & Testimony**
[Only if new signal beyond latest statement, or "Nothing material."]

---

### 2. People's Bank of China
[Same subsection structure]

### 3. European Central Bank
[Same subsection structure]

### 4. Bank of Japan
[Same subsection structure]

### 5. Reserve Bank of India
[Same subsection structure]

### 6. Bank of England
[Same subsection structure]

### 7. Bank of Canada
[Same subsection structure]

### 8. Banco Central do Brasil
[Same subsection structure]

### 9. Bank of Korea
[Same subsection structure]

### 10. Reserve Bank of Australia
[Same subsection structure]

### 11. Central Bank of Turkey
[Same subsection structure]

### 12. Swiss National Bank
[Same subsection structure]

### 13. South African Reserve Bank
[Same subsection structure]

---

### Source Log

Numbered list of all official sources consulted, with URLs and access dates.
```

## 6. Language

English only. No bilingual annotations.

## 7. Editorial Policy

**Purely factual.** No classical liberal framing, no editorial commentary, no episode angle suggestions. The briefing is a reference input — editorial analysis happens downstream in episode prep.

## 8. Design Principles

- **Signal over noise** — if it wouldn't move a base case, skip it or compress to one line
- **Consistency** — every bank gets the same five subsections, even if most say "Nothing material"
- **Source discipline** — official sources only; if something interesting is rumored but not officially published, it doesn't exist in this briefing
- **Scannable** — the quick-reference table and cross-bank analysis should give 80% of the value in 30 seconds

## 9. Repeatable Template & Future Automation

This spec is designed as a **repeatable weekly template**.

**Future automation path:**
- Web search across all 13 central bank sites can be scripted
- RSS feeds / press release pages can be monitored
- Output be pushed to a Notion database (one entry per week)
- Cross-bank table can be maintained as a running time series

---

*End of specification.*
