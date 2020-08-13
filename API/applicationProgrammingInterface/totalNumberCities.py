import requests
import json
res = requests.get('https://api.openaq.org/v1/cities/', params={"country": "AU"})
json_data = res.text
python_data = json.loads(json_data)
counrtyAU = python_data['results']
# print(python_data)
print(len(counrtyAU))