import requests
import json
response = requests.get('https://dog.ceo/api/breeds/list/all')
json_data = response.text
python_data = json.loads(json_data)
breeds = python_data['message']
hound = breeds['hound']
for i in hound:
    print(i)