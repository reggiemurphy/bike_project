import pymysql

class ScraperDB:
    '''Class that deals with creating/connecting/disconnecting/commiting to DB.'''

    def __init__(self):
        # Opening connection
        self.open()
        # Creating cursor.
        c = self.conn.cursor()

        # Statement to create database if it does not exist. 
        c.execute("""CREATE TABLE IF NOT EXISTS BikeData_V2(
        id INT,
        address TEXT,
        lat FLOAT(9,6),
        lng FLOAT(9,6),
        status TEXT,
        bike_stands INT,
        available_bike_stands INT,
        available_bikes INT,
        weather_main TEXT,
        weather_description TEXT,
        temp TEXT,
        last_update DATETIME,
        PRIMARY KEY (id, last_update)
        )""")

        # Committing statement
        self.conn.commit()
        # Closing connection
        self.conn.close()


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
        print("Data Committed, DB Connection Closed") 
        print("-- Five Minutes Until Next Scrape --\n")


    #--------------------------------------------------------------------------#
    # Insert row into table
    def insert(self, number, station, lat, lng, status, total_stands, free_stands, free_bikes, weather_main, weather_description, temp, updated):
        # Creating cursor.
        c = self.conn.cursor()

        # Statement to insert row into table. 
        c.execute("INSERT IGNORE INTO BikeData_V2 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (int(number), station, float(lat), float(lng), status, int(total_stands), int(free_stands), int(free_bikes), weather_main, weather_description, str(temp), str(updated)))

        # Committing statement
        self.conn.commit()
        pass
