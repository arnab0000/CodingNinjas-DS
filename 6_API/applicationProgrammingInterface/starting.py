# import requests
# res = requests.get('http://api.open-notify.org/iss-now.json')
# print(res.status_code)
import requests
import json
res = requests.get('https://codingninjas.in/api/v3/courses')
text = res.text
python_data = json.loads(text)
x = python_data['data']['courses']
for i in x:
    print(i['title'])
print(len(x))