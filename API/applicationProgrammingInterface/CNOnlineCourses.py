import requests
import json
res = requests.get('https://codingninjas.in/api/v3/courses')
text = res.text
python_data = json.loads(text)
courses = python_data['data']['courses']
groups = python_data['data']['course_groups']
for i in courses:
    if i['available_online'] is True:
        print(i['name'])
for j in groups:
    print(j['name'])
