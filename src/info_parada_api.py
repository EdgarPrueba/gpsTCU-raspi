from ucr_api import *
from math import sqrt
#  {
#         "url": "https://databus.bucr.digital/api/gtfs/schedule/stops/1/?format=api",
#         "feed": "1",
#         "stop_id": "bUCR_0_01",
#         "stop_code": "",
#         "stop_name": "Facultad de Educación",
#         "stop_desc": "Frente al jardín de la Facultad de Educación (FE)",
#         "stop_lat": "9.935610",
#         "stop_lon": "-84.048993",
#         "stop_point": "SRID=4326;POINT (-84.04899295728595 9.935610136323218)",
#         "zone_id": "bUCR_0",
#         "stop_url": "",
#         "location_type": 0,
#         "parent_station": "",
#         "stop_timezone": "",
#         "wheelchair_boarding": 1,
#         "platform_cod": ""
#     }
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
        # print(f"{p['shape_id']} - {p['shape_pt_lat']} - {p['shape_pt_lon']} - {p['shape_pt_sequence']} - {p['shape_dist_traveled']}")

get_shapes("hacia_artes")

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
closer_point("hacia_artes")