import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
# print(response.status_code)
data = BeautifulSoup(response.text, 'html.parser')
x = data.find_all(class_ = "product_pod")
for i in x:
    y = i.h3.a['title']
    print(y)