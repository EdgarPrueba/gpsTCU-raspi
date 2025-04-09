from celery import Celery
from celery.schedules import timedelta
import configparser
from datetime import datetime as dt
from test_position import *
# from models import session, Equipment, Position

# Datos de configuración
config = configparser.ConfigParser()
config.read("pipeline.cfg")
url = config["api"]["url"]
token = config["api"]["token"]
period = int(config["scheduler"]["period"])

# Crear "app" de Celery
app = Celery("tasks", broker="redis://localhost")

# Configurar las tareas de Celery
@app.task
def test_task():
    # post_position(journey_id["id"],9.9346491, -84.0456201, 0, 25, 110)
    post_position(10,9.9346491, -84.0456201, 0, 25, 110)
    return "Listo"


@app.task
def schedule_task():
    journey_id = post_journey(
            "2d01a00e-6287-4bfe-8a2b-7bc8a4e2aa5c",
            "1-1234-5678",
            "SJB1234",
            "bUCR_L1",
            "desde_educacion_con_milla_entresemana_13:30",
            0,
            "desde_educacion_con_milla",
            "2024-12-1",
            "13:30:06",
            "SCHEDULED",
            "IN_PROGRESS"
    )
    return "¡Hola mundo cada 60 minutos!"


# ----------
# Configurar aquí las tareas de Celery para el procesamiento de los datos
# ----------

# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "test-schedule": {
        "task": "tasks.test_task",
        "schedule": timedelta(seconds=10),
    },
    "test-schedule-task": {
        "task": "tasks.schedule_task",
        "schedule": timedelta(seconds=60),
    },
}
