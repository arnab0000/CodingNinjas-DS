#client id: WcNMlXMoSiD-4w
#client secret ID: XXJAmlYmlsXm72Ae5EoWq4nA6e8
import requests
import json
data = {'client_id': 'WcNMlXMoSiD-4w', 'response_type': 'code', 'state': 'randon_123', 'redirect_uri': 'https://google.com/', 'scope': 'read'}
response = requests.get('https://www.reddit.com/api/v1/authorize', params=data)
print(response.url)
#code: qkyGZOBRAuY6s99Yg4puzYW90RE
import requests
data2 = {'grant_type': 'authorization_code', 'code': 'qkyGZOBRAuY6s99Yg4puzYW90RE', 'redirect_uri': 'https://google.com/'}
r = requests.post('https://www.reddit.com/api/v1/access_token', data= data2, auth= ('WcNMlXMoSiD-4w', 'XXJAmlYmlsXm72Ae5EoWq4nA6e8'), headers= {'User-Agent': 'ArnabBanerjee'})
print(r.text)
#token: 598971860695-r5EWTYDpbHC6snrOzruDa4Rjf2c
import requests
import json
h = {'User-Agent': 'ArnabBanerjee', 'Authorization': 'bearer 598971860695-r5EWTYDpbHC6snrOzruDa4Rjf2c'}
res = requests.get('https://oauth.reddit.com/hot', headers=h)
data = res.json()
print(data.text)
posts = data['data']['children']
for p in posts:
    print(p['data']['author_fullname'], ":", p['data']['title'])
    print("----------")