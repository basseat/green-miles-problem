import requests

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/road_go_ta_tott"

# Test single country
r1 = requests.get(url, params={"format": "JSON", "lang": "EN", "geo": "DE"})
d1 = r1.json()
print("Single country (DE) value count:", len(d1.get("value", {})))

# Test multi country
r2 = requests.get(url, params={"format": "JSON", "lang": "EN", "geo": "DE,FR,NL"})
d2 = r2.json()
print("Multi country value count:", len(d2.get("value", {})))
print("Multi country geo dimension:", d2["dimension"]["geo"]["category"]["index"])
