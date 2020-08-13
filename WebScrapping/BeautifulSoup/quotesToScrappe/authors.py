import requests
from bs4 import BeautifulSoup
base_url = 'http://quotes.toscrape.com/page/'
d = []
for i in range(1, 11, 1):
    url = base_url + str(i) + '/'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'html.parser')
    authors_raw = data.find_all(class_='author')
    for j in authors_raw:
        d.append(j.string.strip())

x = []
for i in d:
    if i not in x:
        x.append(i)
x.sort()
for i in x:
    print(i)