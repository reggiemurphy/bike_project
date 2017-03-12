import requests
import json
import time
import traceback


# Weather Scraper
URI = "https://api.openweathermap.org/data/2.5/weather"

params = {'id': '7778677', 'appid': 'ad2cefd7ca2ae31891e04ebae16aadba'}

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
