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


# Insert more test functions here...

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
