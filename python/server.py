import requests
from flask import Flask, request
import time
from gpiozero import DistanceSensor, AngularServo

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
def dispenseCandy():
    print('dispenseCandy()')
    if (servo.angle < 0):
        servo.angle = 0
    elif (servo.angle < 90):
        servo.angle = 90
    else:
        servo.angle = -90

@app.route('/dispense', methods=['POST'])
def dispense():
    shutdown_server()
    return None
    
if __name__ == "__main__":
    ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.3)
    servo = AngularServo(24)
    voice = False
    servo.angle = -90

    while True:
        if not voice:
            ultrasonic.wait_for_in_range()
            dist = ultrasonic.distance
            print(dist)
            if dist < 0.1:
                voice = True
                print('voice = True')
        else:
            voice = False
            print('voice = False')
            app.run(host='0.0.0.0', port=80)
            print('verbal dispense')

        dispenseCandy()
        ultrasonic.wait_for_out_of_range()
        print('left')
    