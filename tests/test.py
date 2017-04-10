from nose.tools import eq_, ok_
from flask_site.bike_db.BikeDB import *
from scraper.__main__ import scrape_weather

""" Tests for Project Functionality
    Testing framework used --> Nose """


def test_database_connection():
    """ Will Test if Database Connection was Successful """

    eq_(rds_connection(), True, 'Failed to establish a connection to the RDS')


def test_live_weather():
    """ Will Test if Live Open Weather API Call was successful """

    ok_(scrape_weather(), 'No Live Weather Update from Open Weather')


def test_apostrophe_query():
    """ Tests that query to stations with ' character returns information with escape character """

    ok_(steven(), "Cannot query stations with \' character")


# ---------------------------------------------------------------------- #
def rds_connection():
    """ Tests if Connection to RDS Exists """

    try:
        test_db = BikeDB()
        test_db.open()
        test_db.close()

        return True

    except:
        return False


# ---------------------------------------------------------------------- #
def steven():
    """ Tests query for 'def test_apostrophe_query()' """

    conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
            user='administrator',
            password='bikebikebaby2',
            db='bikebikebaby2',
            charset='utf8',)

    c = conn.cursor()
    query = "SELECT available_bike_stands FROM HalfHourlyInfo WHERE address = 'St. Stephen''s Green South';"
    c.execute(query)
    conn.close()

    return c
