from bs4 import BeautifulSoup
import requests
all_urls = ['https://www.imdb.com/search/title/?release_date=2010&sort=num_votes,desc&page=2&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2011&sort=num_votes,desc&page=2&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2012&sort=num_votes,desc&page=2&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2013&sort=num_votes,desc&page=2&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2014&sort=num_votes,desc&page=2&ref_=adv_nxt'
            ]
for i in all_urls:
    response = requests.get(i)
    data = BeautifulSoup(response.text, 'html.parser')
    movie = data.find(class_="lister-item-header")
    print(movie.a.string.strip())