import pymysql.cursors
import pymysql

# Connect to the database
conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
                             user='administrator',
                             password='bikebikebaby2',
                             db='bikebikebaby2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

c = conn.cursor()

'''Insert MySQL Here'''

conn.close()
