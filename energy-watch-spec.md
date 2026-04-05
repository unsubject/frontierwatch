# Energy Frontier Briefing — Specification

## Overview

A personal enrichment briefing tracking frontier developments and innovations with the potential to disrupt the energy market. For private reading — not channel content.

## Cadence

Twice monthly: **2nd Monday** and **last Monday** of each month.

## Scope

All energy segments, filtered for genuine disruptive potential:

- Electricity & Grid
- Oil & Gas
- Nuclear (fission + fusion)
- Renewables & Storage
- Cross-cutting (e.g. quantum, AI-for-energy, novel materials)

## Framing

**Tech-forward** — what's physically possible. Not economics-first.

## Format

- **Language:** English only
- **Length:** ~500 words, short and scannable (bullet-heavy)
- **Items per issue:** 3–5, with enough depth to understand what's new and why it matters
- **Market commentary:** None — purely informational
- **Continuity:** Track key companies/projects across issues via the Watchlist DB

## Notion Architecture

**Parent page:** [Energy Watch](https://www.notion.so/leesimon/Energy-Watch-33911045597580358cd3ef72ecf9a7f5) (under Frontier Research)

### 1. Energy Frontier Briefing (Database)

One row per issue. Rich page body holds the briefing items.

| Property   | Type      | Notes                                      |
|------------|-----------|--------------------------------------------|
| Title      | Title     | e.g. "Issue #2 — [Theme]"                 |
| Issue      | Number    | Sequential issue number                    |
| Date       | Date      | Publication date                           |
| Theme      | Rich Text | One-line thread connecting the items       |
| Item Count | Number    | Number of briefing items in this issue     |

**Data Source ID:** `c19cf72b-b1d9-4539-8a84-27b537a1b586`

### 2. Energy Frontier Watchlist (Database)

One row per company/technology being tracked. Persistent across issues.

| Property     | Type   | Options / Notes                                                        |
|--------------|--------|------------------------------------------------------------------------|
| Name         | Title  | Company or technology name                                             |
| Sector       | Select | Electricity & Grid, Nuclear, Renewables & Storage, Oil & Gas, Cross-cutting |
| Stage        | Select | Lab, Pilot, Commercial                                                 |
| Status       | Text   | One-line status update                                                 |
| Date Added   | Date   | When first added to the watchlist                                      |
| Last Updated | Date   | When the status was last refreshed                                     |

**Data Source ID:** `82f0a570-b609-4de3-8d09-64c51cbe8c44`

## Issue Structure

Each briefing page follows this template:

```
# [N]. [Headline]
**Sector:** [sector] | **Stage:** [stage]

[What happened — 2-3 sentences]

**Why it's potentially disruptive:** [1 paragraph]

**Key players:** [comma-separated list]

---

(repeat for each item)

# Watchlist
[Summary of new additions and status changes since last issue]
```

## Sources

Best available — no single-source bias:

- Peer-reviewed / academic papers
- Industry press (Canary Media, Utility Dive, etc.)
- Investor/analyst reports (BloombergNEF, IEA, Lazard)
- Company announcements and DOE releases

## Production Workflow

1. Search for developments since the last issue across all energy segments
2. Check the Watchlist DB for items that may have updates
3. Select the 3–5 most significant frontier items
4. Write the briefing page and create it in the Briefing DB
5. Add new entries or update existing entries in the Watchlist DB
6. Update the `Last Updated` date on any watchlist item that was referenced

## Trigger Phrase

Say **"Energy briefing"** or **"Energy Watch"** followed by the issue number to produce the next issue.
