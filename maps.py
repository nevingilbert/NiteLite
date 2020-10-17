import json
import googlemaps
from datetime import datetime

sensitive = json.load("sensitive.json")
gmaps = googlemaps.Client(key=sensitive.APIKey)

origin = ""
destination = ""

# Request directions via walking
now = datetime.now()
directions_result = gmaps.directions(origin,
                                     destination,
                                     mode="walking",
                                     departure_time=now)

steps = directions_result["routes"][0]["legs"][0]["steps"][0]

# Store image urls of route
urls = []

for step in steps:
    end_location = step["end_location"]
    lat = end_location["lat"]
    lng = end_location["lng"]
    urls.append("https://maps.googleapis.com/maps/api/streetview?location=" + lat + "," + lng + "&" + sensitive)
