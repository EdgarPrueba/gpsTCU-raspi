from ucr_api import *
import datetime

def post_position(lat, lon, bearing, speed, odometer):

    timestamp = datetime.datetime.now().isoformat()
    payload = {
        "journey": 2,
        "timestamp": timestamp,
        "point": f"SRID=4326;POINT ({lon} {lat})",
        "latitude": lat,
        "longitude": lon,
        "bearing": bearing,
        "speed": speed,
        "odometer": odometer,
        }
    post_data("position/", payload)

post_position(9.9346491, -84.0456201, 0, 25, 110)