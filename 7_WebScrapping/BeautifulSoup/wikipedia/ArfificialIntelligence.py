import requests
from bs4 import BeautifulSoup
response = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
data = BeautifulSoup(response.text, 'html.parser')
for i in range(37, 49, 1):
    applications = data.find_all(class_="toclevel-2 tocsection-" + str(i))
    value = applications[0].find(class_='toctext').string.strip()
    print(value)
    # print(applications[0].span(class_='toctext').string.split())