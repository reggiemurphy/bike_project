#!/usr/bin/env python
from .ScraperDB import ScraperDB
import requests
import json
import time
import datetime
import traceback

#--------------------------------------------------------------------------#
def main():
	# Creating instance of ScraperDB to handle database operations. 
	db = ScraperDB()

	while (True):
		print(time.strftime('%a, %H:%M:%S'), "- Scraping Data...")

		# Getting summary of current weather. 
		weather = scrape_weather()

		# Getting JSON file with bike station data. 
		json = scrape_bikes()
		
		# Connecting to DB
		db.open()

		# Looping through all objects in JSON file. 
		for item in json: 
			# Parsing data from each object. 
			number, station, lat, lng, status, total_stands, free_stands, free_bikes, updated = parse_json(item)
			# Inserting weather + bike data into DB. 
			db.insert(number, station, lat, lng, status, total_stands, free_stands, free_bikes, weather, updated)

		# Disconnecting from DB
		db.close()

		# Sleep until next cycle. 
		time.sleep(5 * 60)


#--------------------------------------------------------------------------#		
def scrape_weather():
	'''Returns a summary of the current weather from the OpenWeather API'''
	# API URI 
	URI = 'http://api.openweathermap.org/data/2.5/weather'
	# API Parameters 
	params = {'q': 'Dublin', 'appid': 'e9b71166c5c433f0066ecbf407c8d9dc'}

	# Loading Data 
	try:
		req = requests.get(URI, params=params)
		data = json.loads(req.text)

	except:
		data = []
		print(traceback.format_exc())

	# Returning Summary
	return data['weather'][0]['description']



#--------------------------------------------------------------------------#
def scrape_bikes():
	'''Returns a JSON file containing data relating to Dublin Bike stations'''
	# API URI 
	URI = 'https://api.jcdecaux.com/vls/v1/stations'
	# API Parameters 
	params = {'contract': 'Dublin', 'apiKey': 'e651cb028b0b9aa6511acb9dcee4a6e84a5a8b41'}

	# Loading Data 
	try:
		req = requests.get(URI, params=params)
		data = json.loads(req.text)
	
	except:
		data = []
		print(traceback.format_exc())

	# Returning Data
	return data


#--------------------------------------------------------------------------#
def parse_json(item):
	'''Parses station data from JSON file.'''
	# Station Number
	number = item['number']
	# Station Name
	station = item['address']
	# Latitude
	lat = item['position']['lat']
	# Longitude
	lng = item['position']['lng']
	# Longitude
	status = item['status']
	# Total Bike Stands
	total_stands = item['bike_stands']
	# Total Bike Stands Available
	free_stands = item['available_bike_stands']
	# Total Bikes Available
	free_bikes = item['available_bikes']
	# Time of update, stored in a datetime object 
	updated = datetime.datetime.fromtimestamp(item['last_update'] / 1e3)
	
	# Returning parsed data
	return number, station, lat, lng, status, total_stands, free_stands, free_bikes, updated


#--------------------------------------------------------------------------#
if __name__ == '__main__':
    main()