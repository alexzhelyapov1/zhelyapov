import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * len (dac)
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)

def dec2bin(x, number):
    t = x
    for i in range (7, -1, -1):
        number[i] = t % 2
        t >>= 1
    print(number)
    

try:
    a = int(input("Input delay in sec\n"))
    while True:
        for i in range(256):
            dec2bin(i, number)
            GPIO.output (dac, number)
            time.sleep(a/256)
        for i in range(255, -1, -1):
            dec2bin(i, number)
            GPIO.output (dac, number)
            time.sleep(a/256)

            


finally:
    print ("Finally!")
    GPIO.output(dac, 0)
    GPIO.cleanup()