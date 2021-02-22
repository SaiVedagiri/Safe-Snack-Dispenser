import time
from gpiozero import DistanceSensor, Motor

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
# servo = AngularServo(24, min_angle=-135, max_angle=135)
stepper = Motor(24, 25)

while True:
    ultrasonic.wait_for_in_range()
    print('entered range')

    stepper.forward()

    ultrasonic.wait_for_out_of_range()
    print('left range')

    stepper.stop()