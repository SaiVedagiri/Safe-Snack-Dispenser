import time
from gpiozero import DistanceSensor, AngularServo

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
# servo = AngularServo(24, min_angle=-135, max_angle=135)
servo = AngularServo(24)

servo.angle = 0
while True:
    ultrasonic.wait_for_in_range()
    print('entered range')

    servo.min()
    print(servo.angle)

    ultrasonic.wait_for_out_of_range()
    print('left range')

    servo.max()
    print(servo.angle)