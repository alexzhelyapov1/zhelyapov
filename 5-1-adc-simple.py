import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
number = [0] * len (dac)
comp = 4
troyka = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (leds, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)
GPIO.output(dac, 0)
GPIO.output(leds, 0)

def dec2bin(x, number):
    t = x
    for i in range (7, -1, -1):
        number[i] = t % 2
        t >>= 1
    # print(number)

def adc ():
    for i in range (256):
        dec2bin(i, number)
        GPIO.output (dac, number)
        if GPIO.input (comp) == 0:
            print ("i = ", i, number, "voltage = ", i/255*3.3)
            return i
    print ("i = ", 255, number, "voltage = ", 255/255*3.3)
    return 255   

try:
    while True:
        k = adc ()
        GPIO.output(dac, 0)
        time.sleep (0.1)



finally:
    print ("Finally!")
    GPIO.output(dac, 0)
    GPIO.cleanup()