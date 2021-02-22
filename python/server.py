import requests
from flask import Flask, request
import RPi.GPIO as GPIO
import time
from gpiozero import DistanceSensor

app = Flask(__name__)

@app.route('/dispense', methods=['POST'])
def dispense():

    GPIO.setmode(GPIO.BCM)

    trigger = 18
    echo = 24
    
    #set GPIO direction (IN / OUT)
    GPIO.setup(trigger, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    # set Trigger to HIGH
    GPIO.output(trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)