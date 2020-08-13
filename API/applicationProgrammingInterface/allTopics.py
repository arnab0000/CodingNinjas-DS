import requests
import json
username='codingninjas123'
password='cnninjas123'
header={"Accept":"application/vnd.github.mercy-preview+json"}

license = requests.get('https://api.github.com/repos/' + 'google/clusterfuzz/topics', auth=(username,password),headers = header)
pdata = json.loads(license.text)['names']
# print(pdata['topic'])
for i in pdata:
    print(i)