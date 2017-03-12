import requests
import json
from pprint import pprint

# Weather Scraper (timed out at my IP address so causing error)
# URI = "https://api.openweathermap.org/data/2.5/weather"
#
# params = {'id': '7778677', 'appid': '6e21c96e4e61c8798d431cfa10e7df31'}
#
# r = requests.get(URI, params=params)
#
# pprint(json.loads(r.text))


# Bikes Scraper
URI = "https://api.jcdecaux.com/vls/v1/stations"

params = {'contract': 'Dublin', 'apiKey': 'e651cb028b0b9aa6511acb9dcee4a6e84a5a8b41'}

r = requests.get(URI, params=params)

pprint(json.loads(r.text))
