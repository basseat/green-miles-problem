# The Green Miles Problem
### A data investigation into Germany's logistics footprint vs its climate commitments

**Author:** Abdulbasit Ayoade  
**Tools:** Python · Pandas · Matplotlib · Seaborn · Tableau  
**Data Sources:** Eurostat API · EC GROW Postal Statistics (IPC GrowPost CUBE)  
**Countries:** Germany · France · Spain · Netherlands · Poland  
**Period:** 2000–2024 (varies by dataset)

---

## Research Question

Germany operates one of Europe's largest logistics networks and positions itself as a global climate leader. Does the data support both claims simultaneously, or is there a contradiction hiding in the numbers?

---

## Hypotheses & Verdicts

| # | Hypothesis | Verdict | Key Finding |
|---|---|---|---|
| H1 | Germany processes significantly more freight and parcels than comparable European economies | **Partial** | Germany dominated road freight for two decades but Poland has overtaken it in recent years (385,089M TKM vs 307,893M TKM avg). On parcels, Germany processes 3x more per person than France and the gap is still growing. |
| H2 | Germany's transport sector contributes disproportionately to GHG emissions relative to its EU peers | **Confirmed** | Germany peaked at 182,200 Mt CO₂e — the highest of all five countries and nearly 25% above France despite similar population size. |
| H3 | The gap between Germany's logistics environmental impact and its mitigation efforts is larger than its green image suggests | **Partial** | Emissions fell 20.4% (2000–2023), meaningful progress. But recycling grew only 8.7% (2010–2022) against a backdrop of sustained logistics scale. The green reputation is ahead of the green reality. |

---

## Dashboard

Full interactive Tableau dashboard:  
**[The Green Miles Problem — Tableau Public](https://public.tableau.com/app/profile/abdulbasit.ayoade/viz/GreenMile_17809706709340/VerdictandImplications)**

---

## Repository Structure

```
green-miles-problem/
├── data/
│   ├── raw/
│   │   ├── freight/          # road_freight.csv (Eurostat road_go_ta_tott)
│   │   ├── emissions/        # transport_emissions.csv (Eurostat env_air_gge)
│   │   ├── recycling/        # recycling_rates.csv (Eurostat env_wastrt)
│   │   └── postal/           # IPC GrowPost CUBE (compressed .csv.gz)
│   ├── processed/
│   │   └── postal_volumes.csv
│   └── exports/
│       ├── tableau_freight.csv
│       ├── tableau_emissions.csv
│       ├── tableau_recycling.csv
│       ├── tableau_postal.csv
│       ├── tableau_verdict.csv
│       ├── tableau_implications.csv
│       └── *.png              # EDA chart exports
├── eda/
│   └── green_miles_eda.ipynb  # Full analysis notebook
├── etl/
│   ├── pipeline.py            # Orchestrator — runs all collectors
│   ├── eurostat_collector.py  # Fetches freight, emissions, recycling from Eurostat API
│   ├── postal_loader.py       # Processes IPC GrowPost postal dataset
│   └── config.py
├── tableau/
│   └── Green Mile.twbx        # Packaged Tableau workbook
├── report/
│   ├── green_miles_report.docx
│   └── against_the_narrative_green_miles.md
└── requirements.txt
```

---

## How to Run

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the full ETL pipeline**
```bash
python etl/pipeline.py
```
This fetches all data from the Eurostat API and processes the postal dataset. Outputs land in `data/raw/` and `data/processed/`.

**3. Run the EDA notebook**
```bash
jupyter notebook eda/green_miles_eda.ipynb
```
Produces all analysis charts and exports the six Tableau-ready CSVs to `data/exports/`.

---

## Data Sources

| Dataset | Source | Eurostat ID | Period |
|---|---|---|---|
| Road Freight | Eurostat API | `road_go_ta_tott` | 1999–2024 |
| Transport Emissions (GHG) | Eurostat API | `env_air_gge` | 1990–2022 |
| Waste Recycling Rates | Eurostat API | `env_wastrt` | 2010–2022 |
| Postal & Parcel Volumes | EC GROW / IPC GrowPost CUBE | — | 2012–2024 |

---

## Data Quality Notes

- **Germany 2016 letter mail anomaly** — value of 1.25M items is 83% below adjacent years with no identifiable market event. Excluded from trend analysis.
- **Missing parcel values (France 2014, Germany 2014–2015)** — early reporting gaps in the EC GROW dataset, not data errors. Linearly interpolated in Tableau exports.
- **Recycling data is biennial** — Eurostat publishes every two years. Trend lines connect even-year data points.
- **UK excluded** — Eurostat coverage gaps post-Brexit make UK data unreliable for cross-country comparison.
- **Emissions filter** — filtered to `Fuel combustion in transport` (CRF 1.A.3) to isolate transport-sector emissions and avoid double-counting with the Energy sector total.
