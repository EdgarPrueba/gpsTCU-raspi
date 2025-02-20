from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('map.html')  # Frontend page

# Simulating GPS Data Stream (Replace this with actual GPS input)
def send_gps_data():
    lat, lon = 40.758896, -73.985130  # Initial location (NYC)
    while True:
        lat += random.uniform(-0.0005, 0.0005)  # Small variation
        lon += random.uniform(-0.0005, 0.0005)
        socketio.emit('gps_update', {'lat': lat, 'lon': lon})
        time.sleep(1)  # Send every 1s

@socketio.on('connect')
def handle_connect():
    print("Client connected")

if __name__ == '__main__':
    socketio.start_background_task(send_gps_data)  # Start GPS simulation
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
