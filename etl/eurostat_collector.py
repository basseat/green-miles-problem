import requests
import pandas as pd
import os

BASE_URL = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
COUNTRIES = ["DE", "FR", "ES", "NL", "PL"]

DATASETS = {
    "road_freight": {
        "id": "road_go_ta_tott",
        "params": {"format": "JSON", "lang": "EN"},
        "output": "data/raw/freight/road_freight.csv"
    },
    "transport_emissions": {
        "id": "env_air_gge",
        "params": {"format": "JSON", "lang": "EN", "airpol": "GHG"},
        "output": "data/raw/emissions/transport_emissions.csv"
    },
    "recycling_rates": {
        "id": "env_wastrt",
        "params": {
            "format": "JSON",
            "lang": "EN",
            "hazard": "HAZ_NHAZ",
            "wst_oper": "RCV_R",
            "waste": "TOTAL",
        },
        "output": "data/raw/recycling/recycling_rates.csv"
    }
}


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


def fetch_dataset(name, config):
    print(f"Fetching {name}...")
    all_dfs = []

    for country in COUNTRIES:
        params = {**config["params"], "geo": country}
        url = f"{BASE_URL}/{config['id']}"
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"  ERROR {response.status_code} for {country}: {response.text[:150]}")
            continue

        data = response.json()
        if not data.get("value"):
            print(f"  No data for {country}")
            continue

        df = parse_eurostat_json(data)
        all_dfs.append(df)
        print(f"  {country}: {len(df)} rows")

    if not all_dfs:
        print(f"  No data collected for {name}")
        return None

    combined = pd.concat(all_dfs, ignore_index=True)
    os.makedirs(os.path.dirname(config["output"]), exist_ok=True)
    combined.to_csv(config["output"], index=False)
    print(f"  Saved {len(combined)} total rows to {config['output']}")
    return combined


def run():
    for name, config in DATASETS.items():
        fetch_dataset(name, config)


if __name__ == "__main__":
    run()
