import time

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

if (kinamatics_test):
    """Test with Inverse Kinamatics."""
    # x: int = 1
    y: int = -110
    z: int = 0

    while True:
        for x in range(-90, 120, 1):
            if (x == 0):
                x = 0.00001
            lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(x, y, z)
            # Schouder
            kit.servo[0].angle = shoulderLeg
            # Bovenbeen
            kit.servo[1].angle = upperLeg # 50 / 110
            # Onderbeen
            kit.servo[2].angle = lowerLeg # 80 / 30
            time.sleep(0.005)
        for x in range(120, -90, -1):
            if (x == 0):
                x = 0.00001
            lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(x, y, z)
            # Schouder
            kit.servo[0].angle = shoulderLeg
            # Bovenbeen
            kit.servo[1].angle = upperLeg # 50 / 110
            # Onderbeen
            kit.servo[2].angle = lowerLeg # 80 / 30
            time.sleep(0.005)
else:
    """Test with single positions."""
    # kit.servo[0].angle = 90
    # kit.servo[1].angle = 90 # 50 / 110
    # kit.servo[2].angle = 90 # 80 / 30

    x: int = 1
    y: int = -160
    z: int = 0

    lowerLeg, upperLeg, shoulderLeg = kinamatics.calculateLegJointsInDeg(x, y, z)
    # Schouder
    kit.servo[0].angle = shoulderLeg
    # Bovenbeen
    kit.servo[1].angle = upperLeg
    # Onderbeen
    kit.servo[2].angle = lowerLeg