import requests
import json

# Test road freight with no filters first to see structure
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/road_go_ta_tott"
params = {
    "format": "JSON",
    "lang": "EN",
    "geo": "DE",
    "time": "2022"
}

response = requests.get(url, params=params)
print("Status:", response.status_code)
data = response.json()

# Print available dimension values
print("\nDimensions and available values:")
for dim in data["id"]:
    cats = data["dimension"][dim]["category"]["label"]
    print(f"\n{dim}: {list(cats.values())[:10]}")

print("\nValue count:", len(data.get("value", {})))
print("\nSample values:", dict(list(data.get("value", {}).items())[:5]))
