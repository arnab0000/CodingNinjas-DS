import requests
import json
param={"client_id":"cec7ff4cb92972cbf859","redirect_uri":"https://www.google.com","scope":"(no scope)","state":"random_123","allow_signup":"false"}
json_data= requests.get("https://github.com/login/oauth/authorize",params=param)

print(json_data.url)

data={"client_id":"cec7ff4cb92972cbf859","client_secret":"cb5b2629da673b6d73be5063f6242e7ca85ca963","code":"a272156ce62b93a9fa43","redirect_uri":"https://www.google.com","state":"random_123"}
post=requests.post("https://github.com/login/oauth/access_token",data=data)
print(post.text)

header={'User-Agent':'MankaranS','Authorization': 'token  48cf3f8893407e13418a3206c71f6e2cd6e78efb',"type":"all"}

r=requests.get("https://api.github.com/orgs/fossasia/repos",headers=header)
python_data= r.json()
for i in python_data:
    if (i["fork"]== False):
        print(i["name"])