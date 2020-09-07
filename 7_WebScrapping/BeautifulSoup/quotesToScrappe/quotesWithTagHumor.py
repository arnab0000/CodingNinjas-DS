import requests
from bs4 import BeautifulSoup
all_urls = ['http://quotes.toscrape.com/tag/humor/page/1/',
            'http://quotes.toscrape.com/tag/humor/page/2/']
for i in all_urls:
    response = requests.get(i)
    data = BeautifulSoup(response.text, 'html.parser')
    posts_data = data.find_all(class_='text')
    for j in posts_data:
        print(j.string.strip())