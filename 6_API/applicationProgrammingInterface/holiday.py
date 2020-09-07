import requests
import json
res = requests.get('https://www.metaweather.com/api/location/search', params={"query": "USA"})
json_data = res.text
python_data = json.loads(json_data)