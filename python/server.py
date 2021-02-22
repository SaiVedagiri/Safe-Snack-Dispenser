import requests
from flask import Flask, request
import time
# from gpiozero import DistanceSensor

trigger = False
app = Flask(__name__)

@app.route('/dispense', methods=['POST'])
def dispense():
    global trigger
    trigger = True
    return 0

while True:
    if trigger:
        print('dispense!')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)