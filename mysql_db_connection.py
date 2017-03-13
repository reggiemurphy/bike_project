import pymysql

# Connect to the database
conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
                             user='administrator',
                             password='bikebikebaby2',
                             db='bikebikebaby2',
                             charset='utf8',)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Bike(
number INT PRIMARY KEY,
address TEXT,
lat INT,
lng INT,
status TEXT,
bike_stands INT,
available_bike_stands INT,
available_bikes INT,
last_update INT
)""")
conn.commit()
conn.close()
