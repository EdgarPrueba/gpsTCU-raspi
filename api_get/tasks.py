from celery import Celery
from celery.schedules import timedelta
import configparser


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
    """ Función de prueba para Celery.
    Esta función imprime un mensaje en la consola y retorna un string.

    :return: _description_
    :rtype: _type_
    """
    print("¡Hola mundo!")
    return "Listo"


@app.task
def schedule_task():
    """ Función de rutina para Celery.

    :return: _description_
    :rtype: _type_
    """
    print("¡Hola mundo cada 60 minutos!")

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
