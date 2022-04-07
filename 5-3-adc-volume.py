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
            print ("i = ", i, number, "voltage = ", i/256*3.3)
            return i
    print ("i = ", 255, number, "voltage = ", 255/255*3.3)
    return 256   

def adc_new ():
    dac_val = [0] * 8
    for i in range (8):
        dac_val[i] = 1
        GPIO.output (dac, dac_val)
        time.sleep (0.001)
        comp_out = GPIO.input (comp)
        time.sleep (0.001)
        if comp_out == 0:
            dac_val[i] = 0
    weight = 1
    sum = 0
    for i in range (8):
        sum += weight * dac_val[7 -i]
        weight *= 2
    GPIO.output (dac, 0)
    time.sleep (0.001)
    print ("i = ", sum, dac_val, "voltage = ", sum/256*3.3)
    return sum


try:
    while True:
        k = adc ()
        GPIO.output(dac, 0)
        time.sleep (0.001)
        # print ("leds = ", leds[:(int) (k/32)])
        GPIO.output (leds[:(int) (k/32)], 1)
        GPIO.output (leds[(int) (k/32):], 0)



finally:
    print ("Finally!")
    GPIO.output(dac, 0)
    GPIO.cleanup()