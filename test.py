import time
from gpiozero import DistanceSensor, AngularServo

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
servo = AngularServo(24)

servo.angle = 0
count = 0

def turn(count):
    if count % 5 == 0:
        return -90
    elif count % 5 == 1:
        return -45
    elif count % 5 == 2:
        return 0
    elif count % 5 == 3:
        return 45
    else:
        return 90

while True:
    ultrasonic.wait_for_in_range()
    print('entered range')
    count += 1

    servo.angle = turn(count)
    print(servo.angle)

    ultrasonic.wait_for_out_of_range()
    print('left range')
    count += 1

    servo.angle = turn(count)
    print(servo.angle)