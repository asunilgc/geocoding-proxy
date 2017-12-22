====================
RUNNING THE SERVICES
====================

Run the script 'geocode.py' using Python 2.7. Python 2.7 was chosen over Python 3 as it is supported on even older systems and many frameworks for robotics have been developed in Python 2.7

	$ python2 geocode.py

Once the code starts, choose a format for the address being entered. For example:

1. If the user wishes to enter the address in a Street Address format, then choose option 1 and enter details in the following format

	$ Street Address: {Enter Street Address here}
	$ City: {City Name}
	$ State: {Enter full name of state or the 2 letter code}
	$ Country: {Enter full name of country or abbreviation}
	$ Postal Code: {Enter postal code/Zipcode for location}

	Any of these fields can be left blank if the value of that field is not known.

	* Example: 	
		* $ Street Address: 200 Central Park West
		* $ City : New York
		* $ State: NY
		* $ Country: USA
		* $ Postal Code: 10024

2. If the user wishes to enter the address in a more generic format or if the user wishes to copy and paste an address, use option 2

	Address: {Enter address/Landmark name/Building name}

	* Example 1: 	
		* $ Address: 200 Central Park West, New York, NY 10024

	* Example 2:
		* $ Address: Hayden Planetarium

Once the address is entered, the Python script will convert it into a query string and append it to the URL of the Geocoding Services. The script automatically sends a GET request to the Google Maps API first. If there is an error in the response, the script will then call the HERE API to look up the address that was passed.

If more than one result is returned for a given query, the script will display the list of results and prompt to re-enter the address in a more specific way if the desired result is not present in the list.

The format of the output is as follows:

	*  	{Number}. {Formatted Address}
	*	[Latitude, Longitude]: [{Lat},{Lng}]

	* 	Example:	
		* 1. 200 Central Park West, New York, NY 10024, USA
		* [Latitude, Longitude] : [40.7815275, -73.9732592]


Once the results are displayed, the script will prompt the user to choose whether to continue or not.