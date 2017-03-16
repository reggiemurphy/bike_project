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


#--------------------------------------------------------------------------#
# Creating Flask App
app = Flask(__name__)


#--------------------------------------------------------------------------#
# Index Page
@app.route('/')
def index():
    # Instance of BikeDB class.
    db = BikeDB()
    # Current Station - changing this variable changes the station
    station = 'Greek Street'
    # Getting info for station at current time. 
    current_info = db.get_now(station)
    # Get info for station for full day. 
    full_day_info = db.get_day(station)

    return render_template('index.html', **locals())


#--------------------------------------------------------------------------#
# Setting app to run only if this file is run directly. 
if __name__ == '__main__':
    app.run(debug = True)