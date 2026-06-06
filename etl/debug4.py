import requests

# Check what dimensions recycling dataset has
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_wastrt"
response = requests.get(url, params={"format": "JSON", "lang": "EN", "geo": "DE"})
print("Status:", response.status_code)
if response.status_code == 200:
    data = response.json()
    for dim in data["id"]:
        cats = data["dimension"][dim]["category"]["label"]
        print(f"\n{dim}: {list(cats.values())[:8]}")
    print("\nValue count:", len(data.get("value", {})))
else:
    print(response.text[:300])
