from ucr_api import *
from math import sqrt

def get_stops():
    data = get_data("gtfs/schedule/stops/")
    # print(data)
    for p in data:
        print(f"{p['stop_id']} - {p['stop_name']} - {p['stop_desc']} - {p['stop_lat']} - {p['stop_lon']} - {p['zone_id']} - {p['wheelchair_boarding']}")

def get_shapes(filter=None):
    data = get_data("gtfs/schedule/shapes/")
    # print(data)
    for p in data:
        if(filter is not None):
            if(filter in p['shape_id']):
                print(f"{p['shape_id']} - {p['shape_pt_lat']} - {p['shape_pt_lon']} - {p['shape_pt_sequence']} - {p['shape_dist_traveled']}")
        else:
            print(f"{p['shape_id']} - {p['shape_pt_lat']} - {p['shape_pt_lon']} - {p['shape_pt_sequence']} - {p['shape_dist_traveled']}")
# get_shapes("hacia_artes")

def closer_point(filter, lat = 9.934649, lon = -84.045620):
    data = get_data("gtfs/schedule/shapes/")
    # print(data)
    min_dist = 9999999999
    min_pt = 0
    for p in data:
        if(filter is not None):
            if(filter in p['shape_id']):
                    dist = sqrt((lat - float(p["shape_pt_lat"]))**2 + (lon - float(p["shape_pt_lon"]))**2)
                    if dist < min_dist:
                        min_dist = dist
                        min_pt = p["shape_pt_sequence"]
    print(f"El punto más cercano es: {min_pt}")
# closer_point("hacia_artes")

def get_stop_times(filter=None):
    data = get_data("gtfs/schedule/stop-times/")
    # print(data)
    for p in data:
        if(filter is not None):
            if(filter in p['trip_id']):
                print(f"{p['trip_id']} - {p['arrival_time']} - {p['departure_time']} - {p['stop_id']} - {p['stop_sequence']} - {p['pickup_type']} - {p['drop_off_type']} - {p['shape_dist_traveled']}")
        else:
            print(f"{p['trip_id']} - {p['arrival_time']} - {p['departure_time']} - {p['stop_id']} - {p['stop_sequence']} - {p['pickup_type']} - {p['drop_off_type']} - {p['shape_dist_traveled']}")

get_stop_times()
def get_trip(filter=None):
    data = get_data("gtfs/schedule/trips/")
    # print(data)
    for p in data:
        if(filter is not None):
            if(filter in p['trip_id']):
                print(f"{p['route_id']} - {p['service_id']} - {p['trip_id']} - {p['trip_headsign']} - {p['direction_id']} - {p['block_id']} - {p['shape_id']}")
        else:
            print(f"{p['route_id']} - {p['service_id']} - {p['trip_id']} - {p['trip_headsign']} - {p['direction_id']} - {p['block_id']} - {p['shape_id']}")
# get_trip("hacia_artes_entresemana_11:15")
# get_stop_times()