import requests
from bs4 import BeautifulSoup
response = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
data = BeautifulSoup(response.text, 'html.parser')
img = data.find_all('img')
# print(img)
d = {}
for i in img:
    if "height" in i.attrs and "width" in i.attrs:
        height = int(i.attrs['height'].strip())
        width = int(i.attrs['width'].strip())
        area = height * width
        src = i.attrs['src']
        d[src] = area

keyMax = max(d, key=d.get)
print(keyMax)