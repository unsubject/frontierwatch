# Biotech Frontier Intelligence Report — Specification

## Overview

An analyst-level personal briefing tracking frontier developments in biotech and life sciences, combining scientific depth (mechanism of action, clinical context) with soft financial signals (ticker symbols, funding stages, capital allocation trends). No explicit trade ideas.

## Schedule

- **Frequency:** 1st and 3rd Mondays of each month
- **Target read time:** 30–45 minutes

## Scope

### Disease Areas
All areas: oncology, neurology, metabolic disease, infectious disease, rare diseases, longevity, immunology, cardiovascular, gene therapy, cell therapy, and beyond.

### Geography
Global — United States, Europe, China, Japan, and emerging biotech hubs worldwide.

## Depth & Lens

**Analyst-level deep dive.** Each frontier item includes:
- **Scientific layer:** Mechanism of action, clinical/research context, what makes this novel
- **Financial layer (soft):** Note ticker symbols and funding stages where relevant. Describe capital allocation trends and market positioning. No explicit trade ideas or investment recommendations.

### Peer-Reviewed Research Requirement

Each issue must feature **1–2 peer-reviewed papers with disruptive potential**, woven directly into Section 2 (Frontier Developments) rather than siloed in a separate section. These are treated as **journal-club-depth analysis**: not merely cited as a source, but unpacked — explaining the experimental design, key findings, limitations, and why the result could reshape the field if validated.

**Scope:** Biotech and life-science papers only (published in journals such as *Nature*, *Science*, *Cell*, *NEJM*, *The Lancet*, *Nature Medicine*, *Nature Biotechnology*, *Science Translational Medicine*, etc.).

**Selection criteria:** Prioritize papers that introduce a novel mechanism, challenge an established assumption, or demonstrate a step-change in therapeutic efficacy or safety. Incremental improvements do not qualify.

**Format within a Frontier Development entry:** When a paper is the anchor of a writeup, add a `### Paper Spotlight` sub-section within the entry containing:
- **Citation:** Full author list, journal, date, DOI
- **Key finding:** One-sentence distillation
- **Experimental design:** Brief description of methodology (in vivo / in vitro / clinical trial design)
- **Limitations:** What the paper doesn't prove or leaves open
- **Disruptive if…:** The condition under which this finding reshapes the field

## Sources (Priority Order)

1. STAT News
2. Endpoints News
3. FierceBiotech
4. FDA / EMA announcements
5. ClinicalTrials.gov / EU Clinical Trials Register (EU CTR)
6. SEC filings and earnings calls
7. *Nature*, *Science*, *NEJM*, *The Lancet*, *Cell* (for breakthrough science)

## Notion Architecture

**Parent page:** [BioTech Watch](https://www.notion.so/leesimon/BioTech-Watch-33911045597580f6b9befb9efba72a05) (under Frontier Research)

### 1. Biotech Frontier Reports (Database)

One row per report. Rich page body holds the full briefing.

| Property          | Type     | Notes                                              |
|-------------------|----------|----------------------------------------------------|
| Title             | Title    | `Biotech Watch — [Date Range]`                     |
| Issue             | Number   | Sequential issue number                            |
| Date Range        | Text     | e.g. `Mar 23 – Apr 6, 2026`                       |
| Date Published    | Date     | Publication date                                   |
| Item Count        | Number   | Number of frontier development writeups            |
| Has Capital Trends| Checkbox | Whether Section 3 is included this issue           |
| Has Regulatory    | Checkbox | Whether Section 4 is included this issue           |

**Data Source ID:** `2583c017-68fe-41a3-8c56-65f4afafb875`

### 2. Biotech Frontier Watchlist (Database)

One row per company, drug, or platform technology. Persistent across issues.

| Property         | Type         | Options / Notes                                                                                                     |
|------------------|--------------|---------------------------------------------------------------------------------------------------------------------|
| Name             | Title        | Company, drug, or technology name                                                                                   |
| Ticker           | Text         | Stock ticker if public; blank if private                                                                            |
| Therapeutic Area | Multi-select | Oncology, Neurology, Metabolic, Infectious Disease, Rare Disease, Longevity, Immunology, Cardiovascular, Other      |
| Platform         | Multi-select | Gene Therapy, Cell Therapy, mRNA, ADC, CRISPR, Small Molecule, Protein Degradation, Radiopharmaceutical, AI Drug Discovery, Other |
| Stage            | Select       | Preclinical, Phase 1, Phase 2, Phase 3, Approved, Platform (non-clinical tech)                                      |
| Status           | Text         | One-line status update                                                                                              |
| Date Added       | Date         | When first added to the watchlist                                                                                   |
| Last Updated     | Date         | When the status was last refreshed                                                                                  |

**Data Source ID:** `0b8d7a5c-679b-4d3e-b950-7ad2b6f3b6f3`

## Report Structure

Each report page follows this template:

### 1. Executive Summary

Bullet-point key takeaways from the current cycle — the most significant developments at a glance.

### 2. Frontier Developments (3–5 items)

Analyst-level writeups. Grouping is flexible per cycle — by therapeutic area OR technology platform, whichever produces clearer narrative structure. Each entry includes:

```
## [Drug/Company/Technology Name] — [One-line headline]
**Therapeutic Area:** [area] | **Platform:** [platform] | **Stage:** [stage]
**Ticker:** [if public]

### What it is
[Mechanism of action and scientific context — 2-3 paragraphs]

### Paper Spotlight *(when a peer-reviewed paper anchors this entry)*
- **Citation:** [Authors, Journal, Date, DOI]
- **Key finding:** [One-sentence distillation]
- **Experimental design:** [Methodology — in vivo / in vitro / clinical trial design]
- **Limitations:** [What the paper doesn't prove or leaves open]
- **Disruptive if…:** [The condition under which this reshapes the field]

### Where it stands
[Clinical stage, trial data, regulatory status, or research milestones]

### Why it matters
[Capital flow implications, competitive positioning, what this signals for the field]
```

**Paper quota:** At least 1 and up to 2 of the 3–5 frontier items per issue should be anchored by a peer-reviewed paper with a Paper Spotlight sub-section. The remaining items may be driven by clinical data, regulatory events, or industry developments.

### 3. R&D Capital Trends *(included only when notable)*

Where money is flowing this cycle:
- Notable VC funding rounds (company, amount, stage, investors)
- IPOs and public market entries
- M&A activity and strategic acquisitions
- Licensing deals and partnerships

### 4. Regulatory Milestones *(included only when notable)*

- FDA / EMA approvals and denials
- Breakthrough therapy designations
- Fast-track and priority review designations
- Complete Response Letters (CRLs) and rejections

### 5. Watch List

Early-stage developments to monitor in the next cycle. Each item is also added to the Biotech Frontier Watchlist DB for cross-issue tracking.

## Production Workflow

1. Search for biotech/life-science developments since the last report across all therapeutic areas and platforms
2. Search for recent peer-reviewed papers with disruptive potential in top-tier journals (*Nature*, *Science*, *Cell*, *NEJM*, *The Lancet*, *Nature Medicine*, *Nature Biotechnology*, *Science Translational Medicine*)
3. Check the Watchlist DB for items that may have updates
4. Select the 3–5 most significant frontier items for deep writeup, ensuring at least 1–2 are anchored by a peer-reviewed paper
5. Assess whether R&D Capital Trends and Regulatory Milestones sections have enough notable content to include
6. Write the full report page and create it in the Reports DB
7. Add new entries or update existing entries in the Watchlist DB
8. Update the `Last Updated` date on any watchlist item that was referenced

## Trigger Phrase

Say **"Biotech Watch"** or **"Biotech briefing"** followed by the issue number to produce the next report.
