from nose.tools import eq_
from flask_site.bike_db.BikeDB import *

""" Tests for Project Functionality
    Testing framework used --> Nose """


def test_database_connection():
    """ Will Return True if RDS exists """

    eq_(rds_connection(), True, 'Failed to establish a connection to the RDS')


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

rds_connection()