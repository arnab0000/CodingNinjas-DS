import requests
import json
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('arnab.cool.banerjee@gmail.com', 'Majojan@123'))
json_data = response.text
python_data = json.loads(json_data)
print(response.status_code)
info = {'name': 'test_repository', 'description': 'Created via API call', 'auto_init': 'true'}
response = requests.post('https://api.github.com/user/repos', auth= HTTPBasicAuth('arnab.cool.banerjee@gmail.com', 'Majojan@123'), data= json.dumps(info))
print(response.status_code)