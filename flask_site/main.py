#!/usr/bin/env python
from flask import Flask, render_template
import urllib
import json
import requests
import traceback

# View site @ http://localhost:5000/

# Creating Flask App
app = Flask(__name__)


# Function to return the temperature data
def get_weather_data():
    """Returns weather data which is then sent to chart"""
    # API URI
    URI = 'http://api.openweathermap.org/data/2.5/weather'
    # API Parameters
    params = {'q': 'Dublin', 'appid': 'e9b71166c5c433f0066ecbf407c8d9dc'}
    temps = []

    # Loading Data
    try:
        req = requests.get(URI, params=params)
        data = json.loads(req.text)
        temps.append(data['main']['temp_min'])
        temps.append(data['main']['temp'])
        temps.append(data['main']['temp_max'])

    except:
        print(traceback.format_exc())

    return temps


# Index Page
@app.route('/')
def index():
    weather = get_weather_data()
    return render_template('index.html', **locals())

# Setting app to run only if this file is run directly. 
if __name__ == '__main__':
    app.run(debug = True)