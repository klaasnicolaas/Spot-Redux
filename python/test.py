import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

while True:
    for angle in range(50, 180, 1):
        kit.servo[0].angle = angle
        time.sleep(0.05)