import time, serial

import inverse_kinametics as kinamatics
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

"""Defined variables."""
kinamatics_test: bool = True

# Schouder max = 180
# Schouder min = 50

# Bovenbeen max = 150 (liever niet verder dan 120-130)
# Bovenbeen min = 20 (liever niet verder dan 50)

# Onderbeen max = 110
# Onderbeen min = 30

def correct_value(axis, value):
    if (value < 5 | value == 255):
        return -5
    return -value

def main():
    # x: int = 1
    x: int = 1
    y: int = -110
    z: int = 0

    print('Running. Press CTRL-C to exit.')
    with serial.Serial('/dev/ttyUSB0', 115200) as arduino:
        time.sleep(0.1)
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    value = arduino.readline().decode('utf-8').rstrip()
                    y = correct_value(int(value))
                    print(value)
                    lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(x, y, z)
                    # Schouder
                    kit.servo[0].angle = shoulderLeg
                    # Bovenbeen
                    kit.servo[1].angle = upperLeg # 50 / 110
                    # Onderbeen
                    kit.servo[2].angle = lowerLeg # 80 / 30
                    time.sleep(0.005)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")

if __name__ == "__main__":
    main()
