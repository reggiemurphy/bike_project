import pandas as pd
import datetime
import pymysql

#--------------------------------------------------------------------------#
def main():
    # Creating HalfHourlyInfo table. 
    write_db(half_hourly_info(), 'HalfHourlyInfo_WithWeather')

    # Creating StationInfo table, commented out - as doesn't need to be updated.  
    #write_db(station_info(), 'StationInfo')


#--------------------------------------------------------------------------#
def half_hourly_info():
    '''Function that returns dataframe containing bike info for each station in half hour increments.'''
    # Loading data from DB. 
    df = get_db()

    # Loading dry weather categories. 
    f = open('data_analytics/data/dry_weather.txt', 'r')
    dry = f.read().split('/')

    # Dropping unnecessary columns
    df.drop(df.columns[[0, 2, 3, 4, 7, 8, 10]], axis=1, inplace=True)

    # Removing date information, only keeping time. 
    df['last_update'] = df['last_update'].dt.time

    # Flooring time to half hour increments.
    df['last_update'] = df['last_update'].apply(lambda d : round_time(d))

    # Changing all weather descriptions to be either dry or wet.
    df['weather_description'] = df['weather_description'].apply(lambda d : classify_weather(d, dry))

    # Grouping by address and time. 
    df = df.groupby(['address', 'last_update', 'weather_description']).mean().round(0)

    # Order by station name / time. 
    df = df.reset_index()
    df.sort_values(by=['weather_description', 'address', 'last_update'], inplace=True)

    # Returning dataframe. 
    return df


#--------------------------------------------------------------------------#
def station_info():
    '''Function that returns dataframe containing station names and coordinates.'''
    # Loading Data. 
    df = get_db()

    # Dropping unnecessary columns
    df.drop(df.columns[[0, 4, 5, 6, 7, 8, 9, 10, 11]], axis=1, inplace=True)

    # Dropping duplicate rows. 
    df = df.drop_duplicates()

    # Order by station name. 
    df = df.reset_index()
    df.sort_values(by='address', inplace=True)


    # Returning dataframe. 
    return df


#--------------------------------------------------------------------------#
def classify_weather(weather, dry):
    '''Function to group weather into being either dry or wet.'''
    # Minutes is change to 0 if < 30, or 30 if >= 30. 
    if (weather in dry):
        return 'Dry'

    else:
        return 'Wet'


#--------------------------------------------------------------------------#
def round_time(time):
    '''Function to floor datetime.time object to half hour increments.'''
    # Minutes is change to 0 if < 30, or 30 if >= 30. 
    minutes = 0
    if (time.minute >= 30):
        minutes = 30

    # Creating and returning new datetime.time object. 
    return datetime.time(time.hour, minutes, 0)


#--------------------------------------------------------------------------#
def get_db():
    '''Loads database, returns contents in pandas dataframe.'''
    # Connecting to the database
    conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
        user='administrator',
        password='bikebikebaby2',
        db='bikebikebaby2',
        charset='utf8',)

    # Importing DB as padas dataframe. 
    df = pd.read_sql('SELECT * FROM bikebikebaby2.BikeData', con=conn)

    # Closing Connection
    conn.close()

    # Returning dataframe. 
    return df


#--------------------------------------------------------------------------#
def write_db(df, name):
    # Connecting to the database
    conn = pymysql.connect(host='bikebikebaby2.c1ecxudgvgy2.us-west-2.rds.amazonaws.com',
        user='administrator',
        password='bikebikebaby2',
        db='bikebikebaby2',
        charset='utf8',)

    # Creating DB. 
    df.to_sql(con=conn, name=name, if_exists='replace', flavor='mysql')

    # Closing Connection
    conn.close()


#--------------------------------------------------------------------------#
if __name__ == '__main__':
    main()
