from bs4 import BeautifulSoup
import requests
url = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start=201&ref_=adv_nxt'
response = requests.get(url)
data = BeautifulSoup(response.text, 'html.parser')
movie_details = movie = data.find_all(class_='lister-item-header')
time_data = data.find_all(class_='runtime')
print(len(movie), len(time_data))