import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# Schouder max = 180
# Schouder min = 50

# Bovenbeen max = 130 (liever niet verder dan 120-130)
# Bovenbeen min = 20 (liever niet verder dan 50)

# Onderbeen max = 110
# Onderbeen min = 30

# Schouder
kit.servo[0].angle = 95
# Bovenbeen
kit.servo[1].angle = 120 # 50 / 110
# Onderbeen
kit.servo[2].angle = 90 # 80 / 30