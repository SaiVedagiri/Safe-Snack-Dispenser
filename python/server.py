import requests
from flask import Flask, request
import time
from gpiozero import DistanceSensor, AngularServo

app = Flask(__name__)
count = 0

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
def dispenseCandy():
    print('dispenseCandy()')
    if count % 4 == 0:
        servo.angle = -90
    elif count % 4 == 1:
        servo.angle = -45
    elif count % 4 == 2:
        servo.angle = 15
    else:
        servo.angle = 90

@app.route('/dispense', methods=['POST'])
def dispense():
    print('closing')
    shutdown_server()
    return 'ok'
    
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
            count += 1
            if dist < 0.1:
                voice = True
                print('voice = True')
        else:
            voice = False
            print('voice = False')
            count += 1
            app.run(host='0.0.0.0', port=80)
            print('verbal dispense')
            dispenseCandy()
            time.sleep(2)
            count += 1
            app.run(host='0.0.0.0', port=80)

        dispenseCandy()
        ultrasonic.wait_for_out_of_range()
        print('left')
    