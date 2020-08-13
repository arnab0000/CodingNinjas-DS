from bs4 import BeautifulSoup
import requests
response = requests.get('https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt')
# print(response.status_code)
data = BeautifulSoup(response.text, 'html.parser')
movies = data.find_all(class_="lister-item-header")
genre = data.find_all(class_="genre")
year = data.find_all(class_="lister-item-year text-muted unbold")
# print(year)
# print(genre)
for i in range(3):
    y = genre[i].string.strip().split(",")
    print(movies[i].a.string, end = ";")
    # print(year[i].string, end=" ")
    for j in y:
        print(j, end = ",")
    print()