# Securities & Futures Regulatory Watch — Specification

**Version:** 1.0
**Created:** 2026-04-05
**Author:** Simon Lee / Claude
**Status:** Final
**Notion:** https://www.notion.so/leesimon/Securities-and-Futures-Watch-3391104559758057b352df2f25b8403f

---

## 1. Purpose & Use Case

A fortnightly reference briefing on major securities and futures regulatory policy across five jurisdictions, designed for **personal research**. Purely factual — no editorial lens. Focuses on systemic policy shifts, not routine enforcement actions against individual firms.

## 2. Scope

### 2.1 Jurisdictions & Regulators (5 jurisdictions, 12 regulators)

Ordered by approximate nominal GDP of jurisdiction.

| # | Jurisdiction | Regulators Covered | Primary Source URLs |
|---|---|---|---|
| 1 | United States | SEC, CFTC, FINRA | sec.gov, cftc.gov, finra.org |
| 2 | China | CSRC, SAFE, NAFR | csrc.gov.cn, safe.gov.cn, nafr.gov.cn |
| 3 | European Union | ESMA, European Commission (financial regulation) | esma.europa.eu, ec.europa.eu |
| 4 | United Kingdom | FCA, PRA | fca.org.uk, bankofengland.co.uk/prudential-regulation |
| 5 | Hong Kong | SFC, HKEX (regulatory division) | sfc.hk, hkex.com.hk |

### 2.2 Content Categories (ranked by priority)

1. **New rulemaking & rule proposals** — proposed rules, final rules, consultation papers, regulatory guidance, no-action letters with policy significance
2. **Market structure changes** — clearing & settlement reforms, listing rule amendments, trading venue regulation, post-trade infrastructure changes
3. **Enforcement policy shifts** — changes in enforcement priorities, new penalty frameworks, policy statements on enforcement approach (not individual cases)
4. **Cross-border coordination & mutual recognition** — equivalence determinations, MoUs, joint regulatory initiatives, mutual recognition agreements
5. **Digital assets / crypto-specific regulation** — crypto asset classification, stablecoin rules, exchange licensing, DeFi regulatory frameworks
6. **Derivatives & futures-specific regulation** — margin requirements, position limits, reporting rules, CCP supervision changes

### 2.3 Exclusions

- Individual enforcement actions (fines against specific firms/persons) unless they signal a broader policy shift
- Routine administrative notices, staff changes, or procedural updates
- Market commentary, analyst opinions, or industry lobbying positions

### 2.4 Depth

**Signal-focused.** Only material policy shifts, new regulatory directions, and structural changes. The test: *does this represent a new regulatory direction, or is it business as usual?*

### 2.5 Time Horizon

Rolling **14-day window** ending on the briefing date.

## 3. Source Hierarchy

**Official sources only.** Regulator websites, official gazettes, government press releases, and published consultation documents. No wire services, no law firm client alerts, no industry commentary.

## 4. Output Format

**Structured Markdown** — suitable for Notion page import or direct reading.

## 5. Document Structure

The briefing uses a **hybrid structure**: thematic overview first, then jurisdiction-by-jurisdiction detail.

```
# Securities & Futures Regulatory Watch
## Fortnight ending: [YYYY-MM-DD]

---

### Quick-Reference Table

| Jurisdiction | Regulator | Key Action | Status | Effective / Comment Date |
|---|---|---|---|---|
| US | SEC | [Brief description] | Proposed / Final / Consultation | YYYY-MM-DD |
| US | CFTC | ... | ... | ... |
| China | CSRC | ... | ... | ... |
| ... | ... | ... | ... | ... |

(Only rows with material activity this fortnight. Omit jurisdictions with nothing to report.)

---

### Cross-Jurisdiction Analysis

Brief prose (3–5 sentences) identifying:
- Regulatory convergence across jurisdictions (e.g., multiple regulators moving on same issue)
- Divergence or conflicting approaches
- Emerging cross-border coordination signals
- Notable gaps (one jurisdiction acting where others are silent)

---

## Part A: Thematic Overview

### A1. Rulemaking & Rule Proposals
[Cross-jurisdiction summary of new/proposed rules this fortnight. Which jurisdictions acted, what's common, what diverges.]

### A2. Market Structure
[Cross-jurisdiction summary of clearing, settlement, listing, trading venue changes.]

### A3. Enforcement Policy
[Any systemic enforcement policy shifts across jurisdictions.]

### A4. Cross-Border Coordination
[MoUs, equivalence, mutual recognition developments.]

### A5. Digital Assets & Crypto
[Crypto-specific regulatory moves across jurisdictions.]

### A6. Derivatives & Futures
[Margin, position limits, CCP, reporting changes across jurisdictions.]

(Omit any thematic section entirely if no material activity this fortnight.)

---

## Part B: Jurisdiction Detail

### B1. United States (SEC · CFTC · FINRA)

**New Rulemaking & Proposals**
[Material developments only, or "Nothing material this fortnight."]

**Market Structure**
[Or "Nothing material."]

**Enforcement Policy**
[Or "Nothing material."]

**Cross-Border**
[Or "Nothing material."]

**Digital Assets**
[Or "Nothing material."]

**Derivatives & Futures**
[Or "Nothing material."]

---

### B2. China (CSRC · SAFE · NAFR)
[Same subsection structure]

### B3. European Union (ESMA · European Commission)
[Same subsection structure]

### B4. United Kingdom (FCA · PRA)
[Same subsection structure]

### B5. Hong Kong (SFC · HKEX)
[Same subsection structure]

---

### Source Log

Numbered list of all official sources consulted, with URLs and access dates.
```

## 6. Language

English only.

## 7. Editorial Policy

**Purely factual.** No editorial commentary, no classical liberal framing, no episode angle suggestions. The briefing is a reference input.

## 8. Design Principles

- **Policy over enforcement** — individual cases are noise unless they signal a regime change
- **Signal over noise** — if it doesn't represent a new direction, skip or compress to one line
- **Hybrid structure** — thematic overview gives the cross-cutting picture; jurisdiction detail gives the specifics
- **Consistency** — every jurisdiction gets the same six subsections; thematic sections can be omitted if empty
- **Source discipline** — official sources only
- **Scannable** — the quick-reference table and cross-jurisdiction analysis should give 80% of the value in 60 seconds

## 9. Repeatable Template & Future Automation

This spec is designed as a **repeatable fortnightly template**. Current workflow:

1. Simon triggers the briefing
2. Claude performs web searches against official regulator sites for the trailing 14 days
3. Claude populates the template and delivers as markdown

**Future automation path:**
- Web search across all 12 regulator sites can be scripted
- RSS feeds / press release pages can be monitored (most regulators publish feeds)
- Output can be pushed to a Notion database (one entry per fortnight)
- Quick-reference table can be maintained as a running regulatory action log

---

*End of specification.*
