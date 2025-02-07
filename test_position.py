from ucr_api import *
import datetime


def post_journey(equipment, operator, vehicle, route_id, trip_id, direction_id, shape_id, start_date, start_time, schedule_relationship, journey_status):
    
    payload = {
        "operator": operator,
        "equipment": equipment,
        "vehicle": vehicle,
        "route_id": route_id,
        "trip_id": trip_id,
        "direction_id": direction_id,
        "shape_id": shape_id,
        "start_date": start_date,
        "start_time": start_time,
        "schedule_relationship": schedule_relationship,
        "journey_status": journey_status,
    }
    return post_data("journey/", payload)

def post_position(journey_id ,lat, lon, bearing, speed, odometer):

    timestamp = datetime.datetime.now().isoformat()
    payload = {
        "journey": journey_id,
        "timestamp": timestamp,
        "point": f"SRID=4326;POINT ({lon} {lat})",
        "latitude": lat,
        "longitude": lon,
        "bearing": bearing,
        "speed": speed,
        "odometer": odometer,
        }
    post_data("position/", payload)

