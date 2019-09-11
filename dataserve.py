from sense_hat import SenseHat
from flask import Flask, jsonify, json, request, render_template
from flask_cors import CORS
from time import sleep
import json

app = Flask(__name__)
CORS(app)

sense = SenseHat()

@app.route('/JSON')

def index():

    Temperature = sense.get_temperature()
    Pressure = sense.get_pressure()
    Humidity = sense.get_humidity()
    orientation = sense.get_orientation()
    Pitch = (orientation["pitch"])
    Yaw = (orientation["yaw"])
    Roll = (orientation["roll"])
    mag = sense.get_compass_raw()
    MagX = (mag["x"])
    MagY = (mag["y"])
    MagZ = (mag["z"])
    acc = sense.get_accelerometer_raw()
    AccX = (acc["x"])
    AccY = (acc["y"])
    AccZ = (acc["z"])
    gyro = sense.get_gyroscope_raw()
    GyroX = (gyro["x"])
    GyroY = (gyro["y"])
    GyroZ = (gyro["z"])

    return jsonify(Temperature=Temperature, Pressure=Pressure, Humidity=Humidity, Pitch=Pitch, Yaw=Yaw, Roll=Roll, MagX=MagX, MagY=MagY, MagZ=MagZ, AccX=AccX, AccY=AccY, AccZ=AccZ, GyroX=GyroX, GyroY=GyroY, GyroZ=GyroZ)
    sleep(0.5)

@app.route('/weather')

def getweather():

   temperature = round(sense.get_temperature(), 6)
   pressure = round(sense.get_pressure(), 6)
   humidity = round(sense.get_humidity(), 6)
   orientation = sense.get_orientation_degrees()
   raw = sense.get_compass_raw()

   return render_template('weather.html', Temperature=temperature, Pressure=pressure, Humidity=humidity, Orientation=orientation, Raw=raw)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
