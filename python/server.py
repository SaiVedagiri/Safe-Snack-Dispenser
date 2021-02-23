import requests
from flask import Flask, request
import time
from gpiozero import DistanceSensor, AngularServo

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
servo = AngularServo(24)

app = Flask(__name__)

@app.route('/dispense', methods=['POST'])
def dispense():
    
 
    return distance
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)