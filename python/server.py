import requests
from flask import Flask, request
import time
ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
# from gpiozero import DistanceSensor

# trigger = False
app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
def dispenseCandy():
    return 0

@app.route('/dispense', methods=['POST'])
def dispense():
    shutdown_server()
    return None
    
if __name__ == "__main__":
    while True:
        ultrasonic.wait_for_in_range()
        dispenseCandy()
        break
    
    app.run(host='0.0.0.0', port=80)
    dispenseCandy()