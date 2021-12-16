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
    if (axis == "x"):
        if (value < 5):
            if (value == 0):
                return 1
            return (5 - 105)
        elif (value >= 250):
            return (5 - 105)
    return (value - 200)

def main():
    # x: int = 1
    x: int = 1
    y: int = -195
    z: int = 10

    print('Running. Press CTRL-C to exit.')
    with serial.Serial('/dev/ttyUSB0', 115200) as arduino:
        time.sleep(0.1)
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    # value = arduino.readline().decode('utf-8').rstrip()
                    # y = correct_value("y", int(value))
                    # print(f"Beweging: {y} mm")
                    lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(x, y, z)
                    # Schouder
                    kit.servo[0].angle = shoulderLeg
                    # Bovenbeen
                    kit.servo[1].angle = upperLeg # 50 / 110
                    # Onderbeen
                    kit.servo[2].angle = lowerLeg # 80 / 30
                    time.sleep(0.005)
            except KeyboardInterrupt:
                reset_position()
                print("KeyboardInterrupt has been caught.")

def reset_position():
    lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(1, -110, 10)
    # Schouder
    kit.servo[0].angle = shoulderLeg
    # Bovenbeen
    kit.servo[1].angle = upperLeg # 50 / 110
    # Onderbeen
    kit.servo[2].angle = lowerLeg # 80 / 30

if __name__ == "__main__":
    main()
