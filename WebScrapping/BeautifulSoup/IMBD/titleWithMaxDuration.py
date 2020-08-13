from bs4 import BeautifulSoup
import requests
import re
all_urls = ['https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=1&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=51&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=101&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=151&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=201&ref_=adv_nxt'
            ]
d = {}
for i in all_urls:
    response = requests.get(i)
    data = BeautifulSoup(response.text, 'html.parser')
    movie_details = data.find_all(class_='lister-item-content')
    # print(movie_details)
    # time_details = movie_details.find_all(class_='runtime')
    for j in movie_details:
        # print(movie)
        title = j.h3.a.string.strip()
        a = j.p.find(class_='runtime')
        if a is not None:
            time_string = a.string.strip()
            time = int(re.search('\d+', time_string).group())
            d[title] = time
keyMax = max(d, key=d.get)
print(keyMax, d[keyMax])