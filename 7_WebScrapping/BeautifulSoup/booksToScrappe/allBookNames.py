import requests
from bs4 import BeautifulSoup
allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']
for i in allPages:
    response = requests.get(i)
    # print(response.status_code)
    # print(response.text)
    data = BeautifulSoup(response.text, 'html.parser')
    x = data.find_all(class_="product_pod")
    for i in x:
        y = i.h3.a['title']
        print(y)