from flask import Flask, render_template
from flask_socketio import SocketIO
import csv
import random
import time
import os
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('map.html')


def send_gps_data():
    while True:
        try:
            # Realiza la solicitud HTTP a la API para obtener los datos GPS
            response = requests.get("https://api-tcu-ucr-default-rtdb.firebaseio.com/location.json")  
            if response.status_code == 200:
                data = response.json()  # Suponiendo que la API devuelve un JSON con latitud y longitud
                lat = data['latitude']
                lon = data['longitude']
                
                # Enviar los datos GPS al cliente
                socketio.emit('gps_update', {'lat': lat, 'lon': lon})
            else:
                print(f"Error al obtener datos de la API: {response.status_code}")
        except Exception as e:
            print(f"Error al hacer la solicitud: {e}")
        
        time.sleep(1)  # Enviar cada 1 segundo

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")


if __name__ == '__main__':
    socketio.start_background_task(send_gps_data)
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)

