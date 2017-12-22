#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import GMAPSAPI, HEREID, HERECODE
import json
import urllib2

#Empty lists for storing latitude, longitude and descriptive address
flat = []
flon = []
fadd = []

#Function that replaces spaces and commas in the address string by '+'
#so that it can be added to the GET request url
def replace_space(s):
    t = []

    for i in range(len(s)):
        if (s[i] == ' ') or (s[i] == ','):
            t.append('+')   #Replace space or comma with '+'
        else:
            t.append(s[i])  #Make no changes otherwise

    return "".join(t)       #Join char array to form a string

#Function that promts for different parts of an address - Street Address,
#City, State, Country and Postal Code
def categorical_address():
    street_address  = str(replace_space(raw_input("Street Address: ")))
    city  = str(replace_space(raw_input("City: ")))
    state  = str(replace_space(raw_input("State: ")))
    country  = str(replace_space(raw_input("Country: ")))
    postcode  = str(replace_space(raw_input("Postal Code: ")))
    #Join all the parts to form a single string
    address = street_address + "+" + city + "+" + state + "+" + country + "+" + postcode

    return address

#Function that takes in a single line address or names of landmarks or
#important buildings
def line_address():
    address  = str(replace_space(raw_input("Address: ")))

    return address

#Function that sends a GET request to the Google Maps API and retrieves a JSON
#file with the details of the location
def googlemaps(address):
    print "\nGOOGLE MAPS:\n"
    ################################# GET REQUEST TO GOOGLE MAPS API ###########################################################
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address +"&key=" + GMAPSAPI
    try:
        data = json.load(urllib2.urlopen(url))  #Retrieve JSON data
    ############################################################################################################################
        fstat = str(data['status'])
        print "Status: " + fstat + "\n"
        #Check if Status is OK. If not, exit funtion and try the second API
        if fstat != 'OK':
            return 1

        #Retrieve Latitude and Longitude coordinates and the Formatted Address for query
        for i in range(len(data['results'])):
            flat.append(data['results'][i]['geometry']['location']['lat'])
            flon.append(data['results'][i]['geometry']['location']['lng'])
            fadd.append(data['results'][i]['formatted_address'])

        #Display Latitude and Longitude coordinates and the Formatted Address for query
        for i in range(len(data['results'])):
            print str(i+1) + ". " + str(fadd[i]) + "\n[Latitude, Longitude] : [" + str(flat[i]) + ", " + str(flon[i]) + "]\n"

        #If number of results is greater than 1, prompt for more specific
        #address or choose one of the displayed addresses
        if len(data['results']) > 1:
            print "\nMore than 1 address retreived. Choose desired address from the list or enter a more specific address:\n"

        return 0    #Success

    #Check for errors
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):    #Reason for error
            print 'Google Maps API Failure'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):    #HTTP Status code for error
            print 'Google Maps could not fulfill the request.'
            print 'Error code: ', e.code

        return 1    #Failed

#Function that sends a GET request to the HERE API and retrieves a JSON
#file with the details of the location
def heremaps(address):
    print "\nHERE MAPS:\n"
    ######################################## GET REQUEST TO HERE API ###########################################################################
    url = "https://geocoder.cit.api.here.com/6.2/geocode.json?app_id=" + HEREID + "&app_code=" + HERECODE + "&searchtext=" + address
    try:
        data = json.load(urllib2.urlopen(url))  #Retrive JSON data
    ############################################################################################################################################

        #Retrieve Latitude and Longitude coordinates and the Formatted Address for query
        for i in range(len(data['Response']['View'][0]['Result'])):
            flat.append(data['Response']['View'][0]['Result'][i]['Location']['DisplayPosition']['Latitude'])
            flon.append(data['Response']['View'][0]['Result'][i]['Location']['DisplayPosition']['Longitude'])
            fadd.append(data['Response']['View'][0]['Result'][i]['Location']['Address']['Label'])

        #Display Latitude and Longitude coordinates and the Formatted Address for query
        for i in range(len(data['Response']['View'][0]['Result'])):
            print str(i+1) + ". " + str(fadd[i]) + "\n[Latitude, Longitude] : [" + str(flat[i]) + ", " + str(flon[i]) + "]\n"

        #If number of results is greater than 1, prompt for more specific address
        #or choose one of the displayed addresses
        if len(data['Response']['View'][0]['Result']) > 1:
            print "\nMore than 1 address retreived. Choose desired address from the list or enter a more specific address:\n"

        return 0    #Success

    #Check for errors
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):    #Reason for error
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):    #HTTP Status code for error
            print 'The server could not fulfill the request.'
            print 'Error code: ', e.code

        return 1    #Failed


def main():
    #Choose input format for address
    option = int(raw_input("Choose one of the following options by entering the corresponding number:\n1. Search by Street Address, City, State, Country and Postal Code\n2. Search by General Address, Landmarks etc.\n"))
    if option == 1:
        address = categorical_address()
    else:
        address = line_address()

    #Use Google Maps API first. If it fails, use HERE API
    if googlemaps(address) == 1:
        if heremaps(address) == 1:
            print "Geocoding Failed in Both APIs\n"  #Print if both APIs fail

    #Prompt till user decides to stop
    ans = str(raw_input("Continue? (Y/N)"))
    if ans == 'Y' or ans == 'y':
        del flat[:]
        del flon[:]
        del fadd[:]
        main()


if __name__ == '__main__':
    main()  #Call main() function
