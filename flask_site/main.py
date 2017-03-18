from flask import Flask, render_template
from bike_db.BikeDB import BikeDB

# View site @ http://localhost:5000/
#--------------------------------------------------------------------------#
# Creating Flask App
app = Flask(__name__)


#--------------------------------------------------------------------------#
# Index Page
@app.route('/')
def index():
    # Instance of BikeDB class.
    db = BikeDB()

    # Getting station names / coordinates. 
    station_info = db.station_info()

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