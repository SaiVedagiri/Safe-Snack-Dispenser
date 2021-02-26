import time
from gpiozero import DistanceSensor, Motor

ultrasonic = DistanceSensor(echo=18, trigger=23, max_distance=1, threshold_distance=0.2)
motor = Motor(24)


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
    # print(ultrasonic.distance)

    ultrasonic.wait_for_in_range()
    print('entered range')

    motor.backward()
    time.sleep(3)
    motor.stop()

    ultrasonic.wait_for_out_of_range()
    print('left range')

    motor.forward()
    time.sleep(3)
    motor.stop()