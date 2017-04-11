from flask import jsonify
import pymysql
import datetime
import pymysql
import datetime

class BikeDB:
    '''Class that deals with querying DB.'''

    def __init__(self):
        pass

    #--------------------------------------------------------------------------#
    # Returns name and positional info for each station in json format. 
    def station_info(self):
        # Getting current time, floored to half-hour.   
        time = self.current_time_floored()

        # Connecting to DB. 
        self.open()

        # Creating cursor. 
        c1 = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT * FROM StationInfo"
        # Executing SQL query. 
        c1.execute(query)

        # Creating cursor. 
        c2 = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT bike_stands, available_bike_stands FROM HalfHourlyInfo WHERE time = '" + str(time) + "'"
        # Executing SQL query. 
        c2.execute(query)

        # Disconnecting from DB. 
        self.close()

        # Accessing rows returned from query - formatting into json. 
        # SQL table is ordered in the data analytics stage, so no need to order results from the above two queries.
        stations = []
        for row1, row2 in zip(c1, c2):
            station = {
                'name': row1[0],
                'lat': row1[1],
                'lng': row1[2],
                'total': int(row2[0]),
                'available': int(row2[1]),
                'bikes': int(row2[0]) - int(row2[1])
            }
            stations.append(station)

        # Returning info 
        return jsonify({'stations': stations})


    #--------------------------------------------------------------------------#
    # Gets info for specific station for the whole day.
    def occupancy_info(self, station):
        # Connecting to DB. 
        self.open()

        # Account for ' character in queries
        station = station.replace("'", "''")

        # Creating cursor. 
        c = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT bike_stands, available_bike_stands, time, weather FROM HalfHourlyInfo_WithWeather WHERE address = '" + station + "'"
        # Executing SQL query. 
        c.execute(query)

        # Disconnecting from DB. 
        self.close()

        # Accessing rows returned from query - formatting into json. 
        dry = []
        wet = []
        index = 0
        for row in c:
            half_hour = {
                    'total': int(row[0]),
                    'available': int(row[1]),
                    'time': str(row[2])[0:-3],
                    'bikes': int(row[0]) - int(row[1]),
                }

            # First 48 rows returned from query are for dry weather. 
            if (index < 48):
                dry.append(half_hour)
            # Last 48 rows returned from query are for wet weather.
            else:
                wet.append(half_hour)

            # Increment index
            index += 1

        # Returning info 
        current = self.current_time_floored_index()
        return jsonify({'current_dry': dry[current], 'current_wet': wet[current], 'dry_day': dry, 'wet_day': wet})


    #--------------------------------------------------------------------------#
    # Returns current time floored to half hour increments
    def current_time_floored(self):
        # Get current time 
        time = datetime.datetime.now().time()

        # Minutes is change to 0 if < 30, or 30 if >= 30. 
        minutes = 0
        if (time.minute >= 30):
            minutes = 30

        # Creating and returning new datetime.time object. 
        return datetime.time(time.hour, minutes, 0)


    #--------------------------------------------------------------------------#
    # Returns the index of the current half hour - e.g. 0:30 == 1, 2:30 == 5
    def current_time_floored_index(self):
        time = self.current_time_floored()
        return int(time.hour * 2 + time.minute / 30)


    #--------------------------------------------------------------------------#
    # Opening connection to database
    def open(self):
        # Connect to the database
        self.conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
            user='administrator',
            password='bikebikebaby2',
            db='bikebikebaby2',
            charset='utf8',)


    #--------------------------------------------------------------------------#
    # Close connection to database
    def close(self):
        # Disconnect from database
        self.conn.close()
