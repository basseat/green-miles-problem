import requests
import pandas as pd
import os

BASE_URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
COUNTRIES = ["DE", "FR", "ES", "NL", "PL"]

def parse_eurostat_json(data):
    ids = data["id"]
    sizes = data["size"]
    dimensions = data["dimension"]
    values = data["value"]

    pos_to_label = {}
    for dim in ids:
        cats = dimensions[dim]["category"]
        code_to_pos = cats["index"]
        code_to_label = cats.get("label", {})
        pos_to_label[dim] = {
            pos: code_to_label.get(code, code)
            for code, pos in code_to_pos.items()
        }

    strides = [1] * len(ids)
    for i in range(len(ids) - 2, -1, -1):
        strides[i] = strides[i + 1] * sizes[i + 1]

    rows = []
    for idx_str, value in values.items():
        idx = int(idx_str)
        row = {}
        for i, dim in enumerate(ids):
            pos = (idx // strides[i]) % sizes[i]
            row[dim] = pos_to_label[dim].get(pos, pos)
        row["value"] = value
        rows.append(row)

    return pd.DataFrame(rows)

all_dfs = []
for country in COUNTRIES:
    params = {
        "format": "JSON",
        "lang": "EN",
        "geo": country,
        "hazard": "HAZ_NHAZ",
        "wst_oper": "RCV_R",
        "waste": "TOTAL",
    }
    response = requests.get(f"{BASE_URL}/env_wastrt", params=params)
    if response.status_code != 200:
        print(f"ERROR {response.status_code} for {country}: {response.text[:150]}")
        continue
    data = response.json()
    if not data.get("value"):
        print(f"No data for {country}")
        continue
    df = parse_eurostat_json(data)
    all_dfs.append(df)
    print(f"{country}: {len(df)} rows")

if all_dfs:
    combined = pd.concat(all_dfs, ignore_index=True)
    os.makedirs("data/raw/recycling", exist_ok=True)
    combined.to_csv("data/raw/recycling/recycling_rates.csv", index=False)
    print(f"Saved {len(combined)} total rows")
