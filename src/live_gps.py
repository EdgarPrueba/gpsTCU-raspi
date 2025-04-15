from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import requests

# URL de la API para obtener datos GPS
api_url = "https://api-tcu-ucr-default-rtdb.firebaseio.com/location.json"

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('map.html')


def send_gps_data():
    """Función para enviar datos GPS a los clientes conectados.
    Esta función se ejecuta en segundo plano y envía datos GPS
    a través de WebSocket.
    """
    while True:
        try:
            # Realiza la solicitud HTTP a la API para obtener los datos GPS
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                lat = data['latitude']
                lon = data['longitude']

                # Enviar los datos GPS al cliente
                socketio.emit('gps_update', {'lat': lat, 'lon': lon})
            else:
                print("Error al obtener datos de la API:"
                      f"{response.status_code}")
        except Exception as e:
            print(f"Error al hacer la solicitud: {e}")

        # Enviar cada 1 segundo
        time.sleep(1)


@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")


if __name__ == '__main__':
    socketio.start_background_task(send_gps_data)
    socketio.run(app, debug=True, host='0.0.0.0',
                 port=5000, allow_unsafe_werkzeug=True)
