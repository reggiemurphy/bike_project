from flask import Flask, render_template
from bike_db.BikeDB import BikeDB
import json
import requests
import traceback

# View site @ http://localhost:5000/
#--------------------------------------------------------------------------#
def BikeDB_example():
    # Instance of BikeDB class. 
    db = BikeDB()

    # Array containing info for each station. 
    # Each element in array has three attributes: 
    # -- station_info.name -> name of station
    # -- station_info.lat -> latitude of station 
    # -- station_info.long -> longitude of station   
    station_info = db.station_info()

    # Object containg info for the station specified at the current time. 
    # Object has four attributes:
    # -- current_info.total -> total amount of stands at station. 
    # -- current_info.available -> amount of stands available. 
    # -- current_info.bikes -> amount of bikes available. 
    # -- current_info.time -> time 
    current_info = db.get_now('Greek Street')

    # Array containg info for the station specified for the whole day - in 30 minute increments.
    # Each element in array has four attributes:
    # -- current_info.total -> total amount of stands at station. 
    # -- current_info.available -> amount of stands available. 
    # -- current_info.bikes -> amount of bikes available. 
    # -- current_info.time -> time 
    full_day_info = db.get_day('Greek Street')

    return current_info


#--------------------------------------------------------------------------#
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


#--------------------------------------------------------------------------#
# Creating Flask App
app = Flask(__name__)


#--------------------------------------------------------------------------#
# Index Page
@app.route('/')
def index():
    info = BikeDB_example()
    weather = get_weather_data()
    return render_template('index.html', **locals())


#--------------------------------------------------------------------------#
# Setting app to run only if this file is run directly.
if __name__ == '__main__':
    app.run(debug=True)
