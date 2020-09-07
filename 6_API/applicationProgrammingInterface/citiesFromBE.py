import requests
import json
res = requests.get('https://api.openaq.org/v1/cities/', params={"country": "BE", "order_by" : "city"})
json_data = res.text
python_data = json.loads(json_data)
countryBE = python_data['results']
# print(countryBE[0])
for i in range(5):
    print(countryBE[i]['city'])