from flask import Flask, render_template
from flask_socketio import SocketIO
import csv
import random
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return render_template('map.html')


def send_gps_data():
    with open('datos_gps.csv', 'r') as csvfile:
        content = csv.reader(csvfile)

        for row in content:
            lat = float(row[0])
            lon = float(row[1])
            socketio.emit('gps_update', {'lat': lat, 'lon': lon})
            time.sleep(1)  # Enviar cada 1s


@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")


if __name__ == '__main__':
    socketio.start_background_task(send_gps_data)
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
