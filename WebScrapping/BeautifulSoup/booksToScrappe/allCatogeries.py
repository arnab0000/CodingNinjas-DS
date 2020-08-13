import requests
from bs4 import BeautifulSoup
response = requests.get('http://books.toscrape.com/')
data = BeautifulSoup(response.text, 'html.parser')
x = data.find('ul', class_= "nav nav-list")
y = x.find_all('li')
for i in y[1:]:
    print(i.a.string.strip())
# children = x.findChildern('ul', recursive=False)
# for c in children:
#     print(c)