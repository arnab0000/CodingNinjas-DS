from bs4 import BeautifulSoup
import re
import requests

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html']
base_url = 'http://books.toscrape.com/catalogue/'
column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']
for i in allPages:
    response = requests.get(i)
    page_data = BeautifulSoup(response.text, 'html.parser')
    # searching Books
    books_data = page_data.find_all(class_='product_pod')
    for i in books_data:
        b = i.h3.a['href']
        b_url = base_url + b
        r = requests.get(b_url)
        data = BeautifulSoup(r.text, 'html.parser')
        name = data.h1.string
        price_u = data.find(class_='price_color')
        price = price_u.string
        qty_u = data.find(class_='instock availability')
        qty = qty_u.contents[-1].strip()
        qty = int(re.search('\d+', qty).group())
        price = float(re.search('[\d.]+', price).group())
        print(name, b_url, price, qty)
