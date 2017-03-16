from .StandInfo import StandInfo
from .StationInfo import StationInfo
import pymysql
import datetime

class BikeDB:
    '''Class that deals with querying DB.'''

    def __init__(self):
        pass

    #--------------------------------------------------------------------------#
    # Gets name and positional info for each station. 
    def station_info(self):
        # Array that holds information relating to all stations. 
        info = []

        # Connecting to DB. 
        self.open()

        # Creating cursor. 
        c = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT * FROM StationInfo"
        # Executing SQL query. 
        c.execute(query)

        # Disconnecting from DB. 
        self.close()

        # Accessing rows returned from query. 
        for row in c:
            # Storing data in an instance of StationInfo class. 
            info.append(StationInfo(row[0], row[1], row[2]))

        # Returning info 
        return info


    #--------------------------------------------------------------------------#
    # Gets info for specific station for the whole day.
    def get_day(self, station):
        # Array that holds the whole days information. 
        info = []

        # Connecting to DB. 
        self.open()

        # Creating cursor. 
        c = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT bike_stands, available_bike_stands, time FROM HalfHourlyInfo WHERE address = '" + station + "'"
        # Executing SQL query. 
        c.execute(query)

        # Disconnecting from DB. 
        self.close()

        # Accessing rows returned from query. 
        for row in c:
            # Storing data in an instance of StandInfo class. 
            info.append(StandInfo(row[0], row[1], row[2]))

        # Returning info 
        return info


    #--------------------------------------------------------------------------#
    # Gets info for specific station at the current time
    def get_now(self, station):
        # Getting current time, floored to half-hour.   
        time = self.current_time_floored()

        # Connecting to DB. 
        self.open()

        # Creating cursor. 
        c = self.conn.cursor()
        # Constructing SQL query. 
        query = "SELECT bike_stands, available_bike_stands, time FROM HalfHourlyInfo WHERE address = '" + station + "' AND time = '" + str(time) + "'"
        # Executing SQL query. 
        c.execute(query)

        # Disconnecting from DB. 
        self.close()

        # Returning data in an instance of StandInfo class. 
        for row in c:
            return StandInfo(row[0], row[1], row[2])


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