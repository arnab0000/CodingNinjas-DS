import requests
import json
res = requests.get('https://codingninjas.in/api/v3/courses')
json_data = res.text
python_data = json.loads(json_data)
data = python_data['data']['courses']
for i in data:
    if i['id'] == 19:
        print(i['title'])
