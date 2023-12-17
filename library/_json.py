import json

x = '{"nama": "Buchori", "umur": 22, "kota": "New York"}'

y = json.loads(x)

print(y["umur"])
