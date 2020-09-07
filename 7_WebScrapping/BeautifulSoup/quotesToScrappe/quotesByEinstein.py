import requests
from bs4 import BeautifulSoup
base_url = 'http://quotes.toscrape.com/page/'
d = []
name = "Albert Einstein"
for i in range(1, 11, 1):
    url = base_url + str(i) + '/'
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'html.parser')
    authors_raw = data.find_all(class_='quote')
    for j in authors_raw:
        x = j.find(class_='author').string.strip()
        if x == name:
            print(j.span.string.strip())