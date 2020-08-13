import requests
import json
response = requests.get('https://dog.ceo/api/breeds/list/all')
json_data = response.text
python_data = json.loads(json_data)
breeds = python_data['message']
poodle = breeds['poodle']
print(len(poodle))