import urllib2
import json

import datetime
import ConfigParser

class cl:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

config = ConfigParser.SafeConfigParser()
config.read('keys.ini')

fioKey = config.get('keys', 'fio')
owmapKey = config.get('keys', 'owmap')
#wundKey = config.getint('keys', 'p3')

print fioKey
print owmapKey

## Open Weather Map

# openWeather = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=44.175131&lon=-44.28&APPID=111111111111')
# resp = openWeather.read()
# owm = json.loads(resp)

# print "Open Weather Data"
# print "-----------------"
# print "Wind Speed: %d km"%(3.6*(owm['wind']['speed'])) #m/ps
# print "Wind Deg: %d deg"%(owm['wind']['deg'])

# print ""

# openWeather.close()


## FORECAST IO (http://forecast.io/)

request = urllib2.urlopen('https://api.forecast.io/forecast/%s/44.28,-82.416'%(fioKey))

response = request.read()
json = json.loads(response)

print ""
print ""
print cl.OKBLUE+"Forecast IO"
print "-----------"+cl.ENDC
# print "Wind Speed: %d km"%(1.61*(json['currently']['windSpeed']))
# print "Wind Dir: %d deg"%(json['currently']['windBearing'])

# print json['daily']['data'][3]['windSpeed']
# print json['daily']['data'][3]['time']

# print len(json['hourly']['data'])
# print len(json['daily']['data'])

jason = json['hourly']['data']
dayson = json['daily']['data']

count = 0

print cl.OKGREEN+"Current Weather"+cl.ENDC
print "Wind Speed: %d km"%(1.61*(json['currently']['windSpeed']))
print "Wind Dir: %d deg"%(json['currently']['windBearing'])
print ""

print cl.OKGREEN+"8 Day Forecast"+cl.ENDC
print ""

for days in dayson:

	# print count

	print cl.OKBLUE+(datetime.datetime.fromtimestamp(int(json['daily']['data'][count]['time'])).strftime('%Y-%m-%d %H:%M:%S'))+cl.ENDC
	print "Wind Speed: %d km, %d deg"%(1.61*(json['daily']['data'][count]['windSpeed']),json['daily']['data'][count]['windBearing'])
	print ""

	count = count + 1

print ""
print cl.OKGREEN+"48 Hour Forecast"+cl.ENDC

# #print "%s Wind Speed: %d km, %d deg"%(datetime.datetime.fromtimestamp(int(json['daily']['data'][count]['time'])).strftime('%Y-%m-%d %H:%M:%S'),1.61*(json['daily']['data'][count]['windSpeed']),json['daily']['data'][count]['windBearing'])


counter = 0

for time in jason:

	#print counter

	print cl.OKBLUE+(datetime.datetime.fromtimestamp(int(json['hourly']['data'][counter]['time'])).strftime('%Y-%m-%d %H:%M:%S'))+cl.ENDC
	print "Wind Speed: %d km, %d deg"%(1.61*(json['hourly']['data'][counter]['windSpeed']),json['hourly']['data'][counter]['windBearing'])
	print ""

	#print "%s Wind Speed: %d km, %d deg"%(datetime.datetime.fromtimestamp(int(json['hourly']['data'][counter]['time'])).strftime('%Y-%m-%d %H:%M:%S'),1.61*(json['hourly']['data'][counter]['windSpeed']),json['daily']['data'][counter]['windBearing'])

	counter = counter + 1

request.close()


## Weather Underground

# f = urllib2.urlopen('http://api.wunderground.com/api/APIKEY/geolookup/conditions/q/44.28,-82.416.json')
# json_string = f.read()
# parsed_json = json.loads(json_string)

# print "Weather Underground"
# print "-------------------"

# print parsed_json

# print "Wind %d km"%(parsed_json['current_observation']['wind_kph'])
# print "Wind Dir: %d Deg"%(parsed_json['current_observation']['wind_degrees'])

# print ""

# f.close()

exit()



#### Things to look at

# Call current weather data for several cities
# Cities within a rectangle zone
# JSON returns the data from cities within the defined rectangle specified by the geographic coordinates.

# Example: http://api.openweathermap.org/data/2.5/find/city?bbox=12,32,15,37,10&cluster=yes

# or

# Cities in cycle
# JSON returns data from cities laid within definite circle that is specified by center point and radius.

# Example: http://api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10


exit()