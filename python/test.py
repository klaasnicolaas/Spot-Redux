import time
import threading

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

upperLegAngle: int
lowerLegAngle: int
shoulderAngle: int

def bovenbeen_loop(sleep):
    global upperLegAngle, lowerLegAngle
    while True:
        """Bovenbeen."""
        for upperLegAngle in range(170, 30, -1):
            # Omlaag
            kit.servo[1].angle = upperLegAngle
            time.sleep(sleep)
        for upperLegAngle in range(30, 170, 1):
            # Omhoog
            kit.servo[1].angle = upperLegAngle
            time.sleep(sleep)

def onderbeen_loop(sleep):
    """Onderbeen."""
    global upperLegAngle, lowerLegAngle
    while True:
        for lowerLegAngle in range(100, 30, -1):
            # Omhoog
            if upperLegAngle <= 100:
                kit.servo[2].angle = 30
            else:
                kit.servo[2].angle = lowerLegAngle
            time.sleep(sleep)
        for lowerLegAngle in range(30, 100, 1):
            # Omlaag
            if upperLegAngle <= 100:
                kit.servo[2].angle = 30
            else:
                kit.servo[2].angle = lowerLegAngle
            time.sleep(sleep)

def schouder_loop():
    """Schouder."""
    while True:
        for shoulderAngle in range(80, 180, 1):
            # Naar buiten
            kit.servo[0].angle = shoulderAngle
            time.sleep(0.05)
        for shoulderAngle in range(180, 80, -1):
            # Naar binnen
            kit.servo[0].angle = shoulderAngle
            time.sleep(0.05)


if __name__ == '__main__':
    thread_schouder = threading.Thread(target=schouder_loop)
    thread_bovenbeen = threading.Thread(target=bovenbeen_loop, args=(0.03,))
    thread_onderbeen = threading.Thread(target=onderbeen_loop, args=(0.03,))

    # thread_schouder.start()
    thread_bovenbeen.start()
    thread_onderbeen.start()
