# Energy Frontier Briefing — Specification (v2)

## Overview

A personal enrichment briefing tracking frontier developments and innovations with the potential to disrupt the energy market. Combines tech-forward depth (mechanism, physics, engineering context) with soft financial signals (ticker symbols where relevant, capital flow context). No explicit trade ideas. For private reading — not channel content.

## Schedule

- **Frequency:** 2nd and last Mondays of each month
- **Target read time:** 15–20 minutes

## Scope

All energy segments, filtered for genuine disruptive potential:

- Electricity & Grid
- Oil & Gas
- Nuclear (fission + fusion)
- Renewables & Storage
- Cross-cutting (e.g. quantum, AI-for-energy, novel materials)

### Geography

Global — United States, Europe, China, Japan, and emerging energy tech hubs worldwide.

## Depth & Lens

**Tech-forward** — what's physically possible. Each item gets a structured writeup covering what it is, where it stands, and why it matters.

**Financial layer (soft):** Note ticker symbols where companies are public. Describe capital flow and competitive positioning. No explicit investment recommendations.

### Peer-Reviewed Research Requirement

Each issue must feature **1–2 peer-reviewed papers with disruptive potential**, woven directly into the Frontier Developments section (not siloed separately). These are treated as **journal-club-depth analysis**: not merely cited as a source, but unpacked — explaining the experimental design, key findings, limitations, and why the result could reshape the field if validated.

**Scope:** Energy science and engineering papers only (published in journals such as *Nature Energy*, *Joule*, *Science*, *Nature*, *Science Advances*, *Applied Energy*, *Energy & Environmental Science*, *Advanced Energy Materials*, etc.).

**Selection criteria:** Prioritize papers that introduce a novel mechanism, challenge an established assumption, or demonstrate a step-change in performance. Incremental improvements do not qualify.

**Format within a Frontier Development entry:** When a paper anchors a writeup, add a `### Paper Spotlight` sub-section containing:
- **Citation:** Full author list, journal, date, DOI
- **Key finding:** One-sentence distillation
- **Experimental design:** Brief description of methodology
- **Limitations:** What the paper doesn't prove or leaves open
- **Disruptive if…:** The condition under which this finding reshapes the field

## Sources (Priority Order)

1. DOE / EIA announcements and reports
2. IEA reports and commentaries
3. *Nature Energy*, *Joule*, *Science*, *Science Advances* (for breakthrough science)
4. Industry press (Canary Media, Utility Dive, Recharge News, pv magazine)
5. BloombergNEF / Lazard LCOE / S&P Global
6. Company and startup announcements
7. SEC filings and earnings calls (where relevant)

## Notion Architecture

**Parent page:** [Energy Watch](https://www.notion.so/leesimon/Energy-Watch-33911045597580358cd3ef72ecf9a7f5) (under Frontier Research)

> **Migration note:** The v1 databases (Energy Frontier Briefing, Energy Frontier Watchlist) should be manually deleted. The v2 databases below replace them with all data migrated.

### 1. Energy Frontier Briefing v2 (Database)

One row per report. Rich page body holds the full briefing.

| Property       | Type     | Notes                                              |
|----------------|----------|----------------------------------------------------|
| Title          | Title    | `Energy Watch — [Date Range]`                      |
| Issue          | Number   | Sequential issue number                            |
| Date Range     | Text     | e.g. `Mar 24 – Apr 5, 2026`                       |
| Date Published | Date     | Publication date                                   |
| Item Count     | Number   | Number of frontier development writeups            |
| Has Policy     | Checkbox | Whether Policy & Regulation section is included    |
| Theme          | Text     | One-line thread connecting the items               |

**Data Source ID:** `31814856-b31d-4f45-805d-cb708f59d374`

### 2. Energy Frontier Watchlist v2 (Database)

One row per company/technology being tracked. Persistent across issues.

| Property     | Type   | Options / Notes                                                        |
|--------------|--------|------------------------------------------------------------------------|
| Name         | Title  | Company or technology name                                             |
| Ticker       | Text   | Stock ticker if public; blank if private                               |
| Sector       | Select | Electricity & Grid, Nuclear, Renewables & Storage, Oil & Gas, Cross-cutting |
| Stage        | Select | Lab, Pilot, Commercial                                                 |
| Status       | Text   | One-line status update                                                 |
| Date Added   | Date   | When first added to the watchlist                                      |
| Last Updated | Date   | When the status was last refreshed                                     |

**Data Source ID:** `42b44214-3942-478b-bc45-9a47e065d046`

## Report Structure

Each report page follows this template:

### 1. Executive Summary

Bullet-point key takeaways from the current cycle — the most significant developments at a glance.

### 2. Frontier Developments (3–5 items)

Structured writeups. Each entry includes:

```
## [Company/Technology Name] — [One-line headline]
**Sector:** [sector] | **Stage:** [stage]
**Ticker:** [if public]

### What it is
[Mechanism, physics, engineering context — 1-2 paragraphs]

### Paper Spotlight *(when a peer-reviewed paper anchors this entry)*
- **Citation:** [Authors, Journal, Date, DOI]
- **Key finding:** [One-sentence distillation]
- **Experimental design:** [Methodology]
- **Limitations:** [What the paper doesn't prove or leaves open]
- **Disruptive if…:** [The condition under which this reshapes the field]

### Where it stands
[Current stage, milestones, timeline]

### Why it matters
[Competitive positioning, capital flow context, what this signals for the field]

**Key players:** [comma-separated list]
```

**Paper quota:** At least 1 and up to 2 of the 3–5 items per issue should be anchored by a peer-reviewed paper with a Paper Spotlight sub-section. The remaining items may be driven by engineering milestones, regulatory events, or industry developments.

### 3. Policy & Regulation *(included only when notable)*

- DOE / IEA funding announcements and strategy shifts
- Permitting milestones
- IRA / tax credit changes and international equivalents
- Notable standards or safety regulations

### 4. Watchlist

Running list of companies/technologies carried forward from previous issues, with a one-line status update on anything that has moved. New additions noted. References the Watchlist v2 DB.

## Production Workflow

1. Search for energy frontier developments since the last report across all segments
2. Search for recent peer-reviewed papers with disruptive potential in top-tier energy journals (*Nature Energy*, *Joule*, *Science*, *Science Advances*, *Energy & Environmental Science*, *Advanced Energy Materials*)
3. Check the Watchlist DB for items that may have updates
4. Select the 3–5 most significant frontier items for writeup, ensuring at least 1–2 are anchored by a peer-reviewed paper
5. Assess whether Policy & Regulation section has enough notable content to include
6. Write the full report page and create it in the Briefing DB
7. Add new entries or update existing entries in the Watchlist DB
8. Update the `Last Updated` date on any watchlist item that was referenced
