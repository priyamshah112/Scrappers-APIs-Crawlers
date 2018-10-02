#Google Place API
#api_key = AIzaSyDOT2Bw7_GZKku97EQR42lC-x4xB5q8xpQ
# https://developers.google.com/places/web-service/search

import urllib.request
import json

api_key = 'AIzaSyDOT2Bw7_GZKku97EQR42lC-x4xB5q8xpQ'

# Restaurant Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

#Nearby Direction Suggestor

#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)


# Hospital Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=hospitals+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)


# Hotel Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Hotels+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Bar Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Bars+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Bank Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Banks+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Coffee Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Coffee+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Gas stations Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Gas+stations+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Parking Lots Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Parking+Lots+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Groceries Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Groceries+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)

# Post Offices Search
origin  = input("Enter your location ").replace(" ",'+')

restaurant_search = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=Post+offices+in+' + origin + '&key=' + api_key

response = urllib.request.urlopen(restaurant_search).read()
restaurant = json.loads(response)
print(restaurant)


