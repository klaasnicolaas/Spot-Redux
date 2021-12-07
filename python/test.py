import time
import threading

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def bovenbeen_loop():
    while True:
        """Bovenbeen."""
        for angle in range(180, 20, -1):
            # Omlaag
            kit.servo[1].angle = angle
            time.sleep(0.1)
        # for angle in range(50, 180, 1):
        #     # Omhoog
        #     kit.servo[1].angle = angle
        #     time.sleep(0.1)

def onderbeen_loop():
    """Onderbeen."""
    while True:
        for angle in range(110, 30, -1):
            # Omhoog
            kit.servo[2].angle = angle
            time.sleep(0.1)
        # for angle in range(30, 110, 1):
        #     # Omlaag
        #     kit.servo[2].angle = angle
        #     time.sleep(0.1)

def schouder_loop():
    """Schouder."""
    while True:
        for angle in range(80, 180, 1):
            # Naar buiten
            kit.servo[0].angle = angle
            time.sleep(0.05)
        for angle in range(180, 80, -1):
            # Naar binnen
            kit.servo[0].angle = angle
            time.sleep(0.05)


if __name__ == '__main__':
    thread_schouder = threading.Thread(target=schouder_loop)
    thread_bovenbeen = threading.Thread(target=bovenbeen_loop)
    thread_onderbeen = threading.Thread(target=onderbeen_loop)

    thread_schouder.start()
    # thread_bovenbeen.start()
    # thread_onderbeen.start()
