import requests
import json

# Road freight - check raw value structure
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/road_go_ta_tott"
params = {"format": "JSON", "lang": "EN", "geo": "DE", "time": "2022"}

response = requests.get(url, params=params)
data = response.json()

print("IDs:", data["id"])
print("Sizes:", data["size"])
print("Value count:", len(data.get("value", {})))
print("First 5 values:", dict(list(data.get("value", {}).items())[:5]))

# Check index structure
for dim in data["id"]:
    cats = data["dimension"][dim]["category"]
    print(f"\n{dim} index:", cats["index"])
    print(f"{dim} label:", cats.get("label", {}))
