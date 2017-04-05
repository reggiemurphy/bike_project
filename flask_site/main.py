from flask import Flask, render_template, jsonify
from bike_db.BikeDB import BikeDB
from flask_cors import CORS


# View site @ http://localhost:5000/
#--------------------------------------------------------------------------#
# Creating Flask App
app = Flask(__name__)
# Enable Cross Origin Resource Sharing
CORS(app)


#--------------------------------------------------------------------------#
# Index Page
@app.route('/')
def index():
    # Loading dry weather categories. 
    f = open('data_analytics/data/dry_weather.txt', 'r')
    condition = ''
    dry_conditions = f.read().split('/')

    return render_template('index.html', **locals())


#=================================== API ==================================#
# An API is used to allow the website to dynamically query the DB without
# having to be refreshed. This API has two methods: 
#   - /api/occupancy/station_name     -> returns occupancy info for station.
#   - /api/stations                   -> returns station info (name, lat, lng, etc.)
#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
# API - Returns JSON file with occupancy info for whole day. 
@app.route('/api/occupancy/<string:name>', methods=['GET'])
def get_occupancy_info(name):
    return BikeDB().occupancy_info(name)


#--------------------------------------------------------------------------#
# API - Returns JSON file with station info. 
@app.route('/api/stations', methods=['GET'])
def get_station_info():
    return BikeDB().station_info()

    
#--------------------------------------------------------------------------#
# Setting app to run only if this file is run directly. 
if __name__ == '__main__':
    app.run(debug=True)
