import requests
import json
username='codingninjas123'
password='cnninjas123'
license = requests.get('https://api.github.com/' + 'repos/google/go-cloud', auth=(username,password))
json_data = license.text
print(license.json())
pdata = json.loads(json_data)
print(pdata)
# print(license.json().get('license').get('name'))