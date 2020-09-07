import requests
from bs4 import BeautifulSoup
all_urls = ['http://books.toscrape.com/catalogue/page-1.html']
current_url = 'http://books.toscrape.com/catalogue/page-1.html'
base_url = 'http://books.toscrape.com/catalogue/'
response = requests.get(current_url)
print(current_url)
while response.status_code == 200:
    page_data = BeautifulSoup(response.text, 'html.parser')
    next_page = page_data.find(class_="next")
    if next_page is None:
        break
    next_page_url = base_url + next_page.a['href']
    current_url = next_page_url
    all_urls.append(current_url)
    print(current_url)
    response = requests.get(current_url)

# for i in all_urls:
#     print(i)
