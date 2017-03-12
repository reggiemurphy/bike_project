import requests
import json
import time
import traceback

# Bikes Scraper
URI = "https://api.jcdecaux.com/vls/v1/stations"

params = {'contract': 'Dublin', 'apiKey': 'e651cb028b0b9aa6511acb9dcee4a6e84a5a8b41'}

while True:
    try:
        r = requests.get(URI, params=params)
        info = json.loads(r.text)
        f = open('bike_api.txt', 'w')

        for item in info:
            f.write("%s\n" % item)

        time.sleep(5*60)

    except:
        print(traceback.format_exc())
