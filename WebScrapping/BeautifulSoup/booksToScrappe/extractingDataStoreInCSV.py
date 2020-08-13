import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
all_urls = ['http://books.toscrape.com/catalogue/page-1.html']
current_url = 'http://books.toscrape.com/catalogue/page-1.html'
base_url = 'http://books.toscrape.com/catalogue/'
response = requests.get(current_url)
book_details_list = []
while response.status_code == 200:
    page_data = BeautifulSoup(response.text, 'html.parser')
    #searching Books
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
        book_details_list.append([name, b_url, price, qty])

    #going to next page
    next_page = page_data.find(class_="next")
    if next_page is None:
        break
    next_page_url = base_url + next_page.a['href']
    current_url = next_page_url
    all_urls.append(current_url)
    response = requests.get(current_url)

df = pd.DataFrame(book_details_list, columns=['Title', 'Link', 'Price', 'Quantity in stock'])
df.to_csv('books.csv')
