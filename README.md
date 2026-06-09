# Miles, Emissions and Green Promises
### A data investigation into Germany's logistics footprint

**Author:** Abdulbasit Ayoade
**Tools:** Python, Pandas, Matplotlib, Tableau
**Data Sources:** Eurostat Road Freight Transport Database, EC GROW Postal Statistics, Eurostat GHG Emissions, Eurostat Waste Statistics
**Countries:** Germany, France, Spain, Netherlands, Poland
**Period:** 2000–2024 (varies by dataset)

---

## Research Question

Germany operates one of Europe's largest logistics networks and positions itself as a global climate leader. Does the data support both claims simultaneously, or is there a contradiction hiding in the numbers?

---

## Hypotheses

**H1 — Scale**
Germany processes significantly more freight and parcels than comparable European economies.

**H2 — Environmental Cost**
Germany's transport sector contributes disproportionately to GHG emissions relative to its EU peers.

**H3 — The Mitigation Gap**
Despite Germany's climate reputation, the gap between its logistics environmental impact and its mitigation efforts is larger than its green image suggests.

---

## Key Findings

| Hypothesis | Verdict | Key Stat |
|---|---|---|
| H1 — Scale | Partial | Germany averaged 307,893M TKM but Poland's recent peak of 385,089M TKM has overtaken it. On parcels, Germany processes over 3x more per person than France and the gap is still growing. |
| H2 — Emissions | Confirmed | Germany peaked at 182,200 Mt CO2e, highest of all five countries. Nearly 25% more than France despite similar population size. |
| H3 — Mitigation Gap | Partial | Emissions fell 20.4% (2000–2023) and recycling overtook emissions in 2018. But recycling grew only 8.7% (2010–2022) against sustained logistics scale. |

---

## Dashboard

View the full interactive Tableau dashboard here:
**[Miles, Emissions and Green Promises — Tableau Public](https://public.tableau.com/app/profile/abdulbasit.ayoade/viz/GreenMile_17809706709340/VerdictandImplications)**

---

## Repository Structure

    green-miles-problem/
    ├── data/
    │   ├── raw/          # Original data from Eurostat and EC GROW
    │   ├── processed/    # Cleaned and merged datasets
    │   └── exports/      # CSV files used in Tableau
    ├── notebooks/
    │   └── green_miles_eda.ipynb
    └── README.md

---

## Data Quality Notes

- Germany 2016 letter mail value excluded as a reporting anomaly
- UK excluded due to Eurostat coverage gaps post-Brexit
- Recycling data is biennial (every two years), not annual
- Germany parcel data missing for 2014 and 2015, interpolated visually in charts
- 2020 dip across all emissions data reflects COVID-19 lockdowns, not structural reduction
