import requests

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/env_wastrt"
response = requests.get(url, params={"format": "JSON", "lang": "EN", "geo": "DE"})
data = response.json()

# Print actual codes (not labels) for each dimension
for dim in data["id"]:
    cats = data["dimension"][dim]["category"]
    print(f"\n{dim} codes: {list(cats['index'].keys())[:10]}")
