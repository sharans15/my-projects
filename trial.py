from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("mumbai")
 
# printing address
print(getLoc.address)
 
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)
# Import module
from geopy.geocoders import Nominatim
 
# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
 
# Assign Latitude & Longitude
Latitude = "25.594095"
Longitude = "85.137566"
 

 
# Get location with geocode
location = geolocator.geocode(Latitude+","+Longitude)


location = list((location))[0]
place = []
for x in location:
    
    place.append(x)
    if ',' in x:
        break
places = "".join(place)
places = places[0:-1]
print(places)
 
