======================
USING THE SERVICES API
======================


HTTP Request
------------
HTTP requests are made using the 'urllib2' module in Python 2.7. The function 'urllib2.urlopen()' is used to access the URL. In case of an error, the error code and reason are logged using 'urllib2.URLError'.


Data Serialization
------------------
Data serialization is carried out in the JSON format in this project. The GET requests made to the Geocoding APIs specify that the returned data should be in JSON format. We then use Python's 'json' module to parse this data and extract the required information.


Geocoding Services
------------------
Two third party Geocoding Services are used in this project:

	1. Google Maps API
	2. HERE API

1. Google Maps API

Google Maps API provides Geocoding services by responding to an HTTP request like the one shown below:

	* 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY'

This request specifies that the data to be returned should be in JSON format and the address that is to be looked up is 1600 Amphithetre Parkway, Mountain View, CA. This is transmitted as a query string. The API key can be obtained from the Google API console.

Once the JSON data is received, the Latitude, Longitude and Formatted address can be extracted by accessing the following elements:

	* Latitude = ['results'][{i}]['geometry']['location']['lat']
        * Longitude = ['results'][{i}]['geometry']['location']['lng']
        * Address = ['results'][{i}]['formatted_address']

More information about the Google Maps API can be found at https://developers.google.com/maps/documentation/geocoding/start

2. HERE API

HERE API provides Geocoding services by responding to an HTTP request like the one shown below:

	* 'https://geocoder.cit.api.here.com/6.2/geocode.json?app_id={YOUR_APP_ID}&app_code={YOUR_APP_CODE}&searchtext=425+W+Randolph+Chicago'

Like the previous request, this request also specifies that the data must be in JSON format. The address to be looked up is 425 W Randoplph, Chicago. The APP ID and APP CODE can be obtained after registering with HERE.

Once the data is received, the details can be extracted as shown below:

	* Latitude = ['Response']['View'][0]['Result'][{i}]['Location']['DisplayPosition']['Latitude'])
        * Longitude = ['Response']['View'][0]['Result'][{i}]['Location']['DisplayPosition']['Longitude'])
        * Address = ['Response']['View'][0]['Result'][{i}]['Location']['Address']['Label'])

More information about the HERE Maps API can be found at https://developer.here.com/documentation/geocoder/topics/quick-start-geocode.html
