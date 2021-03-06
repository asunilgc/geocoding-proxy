# Geocoding Proxy Service - Important Instructions
Provides a Python Geocoding Service that looks up Latitude and Longitude for a given address

IMPORTANT:

* In order to run the program, you have to first obtain credentials from Google Maps API and also from the HERE API.
* Once the Google Maps API Key, HERE App ID and HERE App Code are obtained, insert them in the appropriate fields in the file - 'config.py' in the directory - 'scripts'.

* From 'scripts' directory, find 'geocode.py'
* Run 'geocode.py' using Python 2.7 : $ python geocode.py
  
The following screenshots show different cases of running the service:

* Providing the address in the Street Address format with Street Number and Name, City, State, Country and Postal Code:

![alt text](https://github.com/asunilgc/geocoding-proxy/blob/master/screenshots/mode_1_gmaps.png?raw=true)

* Providing a single line address:

![alt text](https://github.com/asunilgc/geocoding-proxy/blob/master/screenshots/mode_2_gmaps.png?raw=true)

* Providing a Landmark Name:

![alt text](https://github.com/asunilgc/geocoding-proxy/blob/master/screenshots/mode_2_landmark_gmaps.png?raw=true)

* Providing ambiguous address:

![alt text](https://github.com/asunilgc/geocoding-proxy/blob/master/screenshots/mode2_list.png?raw=true)

* Google Maps Malfunctioning and Using HERE Maps:

![alt text](https://github.com/asunilgc/geocoding-proxy/blob/master/screenshots/mode2_heremaps.png?raw=true)
