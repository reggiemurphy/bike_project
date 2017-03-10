import sys
import logging
import rds_config
import pymysql


rds_host = rds_config.bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com:3306
name = rds_config.administrator
password = rds_config.bikebikebaby2
db_name = rds_config.bikebikebaby2
port = 3306
logger = logging.getLogger()
logger.setLevel(logging.INFO)


try:
 conn = pymysql.connect(rds_host, user=name,
 passwd=password, db=db_name, connect_timeout=5)


 # Adding to database goes here???

except:
 logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
 sys.exit()