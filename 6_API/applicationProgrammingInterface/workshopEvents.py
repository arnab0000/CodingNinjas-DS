import requests
import json
response = requests.get('https://api.codingninjas.com/api/v3/events?event_category=ALL_EVENTS&event_sub_category=All%20Time%20Favorites&tag_list=&offset=0&_ga=2.237238788.501134411.1596207493-1921114314.1579839235')
json_data = response.text
python_data = json.loads(json_data)
events = python_data['data']['events']
fEvent = events[0]
print(fEvent['short_desc'])
