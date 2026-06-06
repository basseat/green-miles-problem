import pandas as pd
import gzip
import os

POSTAL_FILE = "data/raw/postal/grow_post_cube1_x$post_dtr_1_filtered_en.csv.gz"
OUTPUT = "data/processed/postal_volumes.csv"

COUNTRIES = {
    "DE:Germany": "Germany",
    "FR:France": "France",
    "ES:Spain": "Spain",
    "NL:Netherlands": "Netherlands",
    "PL:Poland": "Poland"
}

INDICATORS = {
    "DTR401_01:Domestic letter mail services, total volumes": "letter_mail_per_inhabitant",
    "DTR401_03:Domestic parcel services, total volumes": "parcel_per_inhabitant"
}


def run():
    print("Loading postal data...")
    with gzip.open(POSTAL_FILE, "rt", encoding="utf-8") as f:
        df = pd.read_csv(f)

    print(f"  Raw rows: {len(df)}")

    # Filter to our countries and indicators
    df = df[df["GEO"].isin(COUNTRIES.keys())]
    df = df[df["INDIC_PS"].isin(INDICATORS.keys())]

    # Clean up
    df["country"] = df["GEO"].map(COUNTRIES)
    df["indicator"] = df["INDIC_PS"].map(INDICATORS)
    df["year"] = df["TIME_PERIOD"]
    df["value"] = pd.to_numeric(df["OBS_VALUE"], errors="coerce")

    df = df[["country", "indicator", "year", "value"]].dropna(subset=["value"])

    # Pivot so letter_mail and parcel are separate columns
    df_pivot = df.pivot_table(
        index=["country", "year"],
        columns="indicator",
        values="value"
    ).reset_index()
    df_pivot.columns.name = None

    os.makedirs("data/processed", exist_ok=True)
    df_pivot.to_csv(OUTPUT, index=False)
    print(f"  Saved {len(df_pivot)} rows to {OUTPUT}")
    print(df_pivot.head(10))


if __name__ == "__main__":
    run()
