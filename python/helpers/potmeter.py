#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    print('Running. Press CTRL-C to exit.')
    with serial.Serial('/dev/ttyUSB0', 115200) as arduino:
        time.sleep(0.1)
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    line = arduino.readline().decode('utf-8').rstrip()
                    print(line)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")