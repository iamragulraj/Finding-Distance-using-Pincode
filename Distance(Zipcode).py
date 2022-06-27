from geopy.geocoders import Nominatim
from geopy import distance
geolocater=Nominatim(user_agent="sample")
geocoder=Nominatim(user_agent="sample")
geolocator=Nominatim(user_agent="sample")

zipcode1=int(input("Enter zipcode1:"))
zipcode2=int(input("Enter zipcode2:"))
print()
location1=geolocator.geocode(zipcode1)
location2=geolocator.geocode(zipcode2)
print("The location1 name is",location1.address)
print("The location2 name is",location2.address)
print()

coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)

lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

place1=(lat1,long1)
place2=(lat2,long2)

print("The distance between location1 and location2 is",distance.distance(place1,place2).km,"kms")
