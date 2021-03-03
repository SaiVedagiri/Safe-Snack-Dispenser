import time
from gpiozero import DistanceSensor, AngularServo

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
servo = AngularServo(24)

servo.angle = 0
count = 0

def turn(count):
    if count % 4 == 0:
        return -90
    elif count % 4 == 1:
        return -45
    elif count % 4 == 2:
        return 0
    else:
        return 90

while True:
    # servo.angle = turn(count)
    # count += 1
    # time.sleep(3)
    
    servo.angle = turn(3)

#     print('entered range')
#     count += 1

#     servo.angle = turn(count)
#     print(servo.angle)

#     ultrasonic.wait_for_out_of_range()
#     print('left range')
#     count += 1

#     servo.angle = turn(count)
#     print(servo.angle)
