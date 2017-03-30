from flask import Flask, render_template, jsonify
from bike_db.BikeDB import BikeDB
from scraper.__main__ import scrape_weather

# View site @ http://localhost:5000/
#--------------------------------------------------------------------------#
# Creating Flask App
app = Flask(__name__)


#--------------------------------------------------------------------------#
# Index Page
@app.route('/')
def index():
    weather_desc, weather_sum, temp = scrape_weather()
    return render_template('index.html', **locals())


#=================================== API ==================================#
# An API is used to allow the website to dynamically query the DB without
# having to be refreshed. This API has three methods: 
#   - /api/current/station_name -> returns info for station at current time. 
#   - /api/day/station_name     -> returns info for station for full day.
#   - /api/stations             -> returns station info (name, lat, lng, etc.)
#--------------------------------------------------------------------------#
# API - Returns JSON file with current occupancy info. 
@app.route('/api/current/<string:name>', methods=['GET'])
def get_current_info(name):
    # Getting info for station at current time. 
    current_info = BikeDB().get_now(name)

    # Formatting current_info into JSON.
    info = {
            'total': current_info.total,
            'available': current_info.available,
            'time': current_info.time,
            'bikes': current_info.bikes,
        }

    # Returning JSON.
    return jsonify({'current': info})


#--------------------------------------------------------------------------#
# API - Returns JSON file with occupancy info for whole day. 
@app.route('/api/day/<string:name>', methods=['GET'])
def get_day_info(name):
    # Get info for station for full day. 
    full_day_info = BikeDB().get_day(name)

    # Formatting full_day_info into JSON.
    times = []
    for info in full_day_info:
        half_hour = {
                'total': info.total,
                'available': info.available,
                'time': info.time,
                'bikes': info.bikes,
            }
        times.append(half_hour)

    # Returning JSON.
    return jsonify({'times': times})


#--------------------------------------------------------------------------#
# API - Returns JSON file with station info. 
@app.route('/api/stations', methods=['GET'])
def get_station_info():
    # Getting station info. 
    station_info = BikeDB().station_info()

    # Formatting station_info into JSON.
    stations = []
    for info in station_info:
        station = {
            'name': info.name,
            'lat': info.lat,
            'lng': info.long,
            'total': info.total,
            'available': info.available,
            'bikes': info.bikes
        }
        stations.append(station)

    # Returning JSON.
    return jsonify({'stations': stations})


#--------------------------------------------------------------------------#
# Setting app to run only if this file is run directly. 
if __name__ == '__main__':
    app.run(debug = True)