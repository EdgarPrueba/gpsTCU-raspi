from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

# Datos de configuración
config = configparser.ConfigParser()
config.read("src/pipeline.cfg")
system = config["db"]["system"]
name = config["db"]["name"]

# Crear la clase base de la tabla
Base = declarative_base()


# Definir los modelos
class Equipment(Base):
    #{
    #     "url": "https://databus.bucr.digital/api/equipment/16736b9e-43d6-49f0-a269-6f71573d7730/",
    #     "data_provider": "1964",
    #     "vehicle": "SJB5678",
    #     "serial_number": "H4939GNE9",
    #     "brand": "Hertz",
    #     "model": "LM741",
    #     "software_version": "v2.4",
    #     "provides_vehicle": true,
    #     "provides_operator": true,
    #     "provides_journey": true,
    #     "provides_position": true,
    #     "provides_progression": true,
    #     "provides_occupancy": true,
    #     "provides_conditions": false,
    #     "provides_emissions": false,
    #     "provides_travelers": false,
    #     "provides_authorizations": false,
    #     "provides_fares": false,
    #     "provides_transfers": false,
    #     "provides_alerts": true,
    #     "created_at": "2024-08-29T13:43:20.404000-06:00",
    #     "updated_at": "2024-08-29T13:43:20.404000-06:00"
    # }
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    data_provider = Column(String)
    vehicle = Column(String)
    serial_number = Column(String)
    brand = Column(String)
    model = Column(String)
    software_version = Column(String)
    provides_vehicle = Column(String)
    provides_operator = Column(String)
    provides_journey = Column(String)
    provides_position = Column(String)
    provides_progression = Column(String)
    provides_occupancy = Column(String)
    provides_conditions = Column(String)
    provides_emissions = Column(String)
    provides_travelers = Column(String)
    provides_authorizations = Column(String)
    provides_fares = Column(String)
    provides_transfers = Column(String)
    provides_alerts = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Operator(Base):
    #  {
    #     "url": "https://databus.bucr.digital/api/operator/1-1234-5678/",
    #     "user": 2,
    #     "agency": [],
    #     "vehicle": null,
    #     "equipment": null,
    #     "phone": "87654321",
    #     "photo": null,
    #     "data_provider": []
    # }
    __tablename__ = "operator"
    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    agency = Column(String)
    vehicle = Column(String)
    equipment = Column(String)
    phone = Column(String)
    photo = Column(String)
    data_provider = Column(String)

class Journey(Base):
    # {
    #     "url": "https://databus.bucr.digital/api/journey/2/",
    #     "equipment": "2d01a00e-6287-4bfe-8a2b-7bc8a4e2aa5c",
    #     "operator": "1-1234-5678",
    #     "vehicle": "SJB1234",
    #     "route_id": "bUCR_L1",
    #     "trip_id": "desde_educacion_con_milla_entresemana_13:30",
    #     "direction_id": 0,
    #     "shape_id": "desde_educacion_con_milla",
    #     "start_date": "2024-08-29",
    #     "start_time": "13:30:06",
    #     "schedule_relationship": "SCHEDULED",
    #     "journey_status": "IN_PROGRESS"
    # }
    __tablename__ = "journey"

    id = Column(Integer, primary_key=True)
    equipment = Column(String)
    operator = Column(String)
    vehicle = Column(String)
    route_id = Column(String)
    trip_id = Column(String)
    direction_id = Column(Integer)
    shape_id = Column(String)
    start_date = Column(DateTime)
    start_time = Column(DateTime)
    schedule_relationship = Column(String)
    journey_status = Column(String)

class Position(Base):
    # {
    #     "url": "https://databus.bucr.digital/api/position/2/",
    #     "journey": 2,
    #     "timestamp": "2024-08-29T13:35:48-06:00",
    #     "point": "SRID=4326;POINT (-84.04555530733563 9.93540698388418)",
    #     "latitude": 9.93540698388418,
    #     "longitude": -84.04555530733563,
    #     "bearing": 0.0,
    #     "odometer": 9.0,
    #     "speed": 12.0
    # }
    __tablename__ = "position"

    id = Column(Integer, primary_key=True)
    journey = Column(Integer)
    timestamp = Column(DateTime)
    point = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    bearing = Column(Float)
    odometer = Column(Float)
    speed = Column(Float)

class Progression(Base):
    # {
    #     "url": "https://databus.bucr.digital/api/progression/2/",
    #     "journey": 2,
    #     "timestamp": "2024-08-29T14:03:29.055000-06:00",
    #     "current_stop_sequence": 3,
    #     "stop_id": "bUCR_0_04",
    #     "current_status": "INCOMING_AT",
    #     "congestion_level": "RUNNING_SMOOTHLY"
    # }
    __tablename__ = "progression"
    id = Column(Integer, primary_key=True)
    journey = Column(Integer)
    timestamp = Column(DateTime)
    current_stop_sequence = Column(Integer)
    stop_id = Column(String)
    current_status = Column(String)
    congestion_level = Column(String)
    
# Crear la conexión a la base de datos SQLite3
engine = create_engine(f"{system}:///{name}")
Session = sessionmaker(bind=engine)
session = Session()

# Crear la(s) tabla(s) en la base de datos
Base.metadata.create_all(engine)