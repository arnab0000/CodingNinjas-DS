import requests
import json
username='codingninjas123'
password='cnninjas123'
license = requests.get('https://api.github.com/repos/' + 'google/science-journal-ios/languages', auth=(username,password))
json_data = license.text
pdata = json.loads(json_data)
for i in pdata:
    print(i)