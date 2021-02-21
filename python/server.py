import requests
from flask import Flask, request
import RPi.GPIO as GPIO
import time
from gpiozero import DistanceSensor

app = Flask(__name__)

@app.route('/dispense', methods=['POST'])
def dispense():
    # my code here
    return "OK"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)