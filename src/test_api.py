from ucr_api import *

payload = {
        "url": "https://databus.bucr.digital/api/gtfs/schedule/fare-rules",
        "agency": 1,
        "label": "Pruebas2",
        "license_plate": "HHH123",
        "wheelchair_accessible": "WHEELCHAIR_ACCESIBLE",
        "wifi": "UNAVAILABLE",
        "air_conditioning": "UNAVAILABLE",
        "mobile_charging": "AVAILABLE",
        "bike_rack": "UNAVAILABLE",
        "has_screen": True,
        "has_headsign_screen": True,
        "has_audio": True
    }

# {
#     "url": "https://databus.bucr.digital/api/gtfs/schedule/fare-rules",
#     "agency": [123],
#     "name": "test",
#     "description": "hola"
# }
post_data('vehicle/', payload)
# data = get_data("gtfs/schedule/fare-rules")
# print(data)
