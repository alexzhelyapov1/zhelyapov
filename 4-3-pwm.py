import RPi.GPIO as GPIO
import time

pin = 22
GPIO.setmode (GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)

try:
    while True:
        a = input ("Print digit pls\n")
        if not a.isdigit() or int(a) > 100 or int(a) < 0:
            if a == 'q':
                break
            print ("Wrong digit")
            continue
        x = int(a)
        print("Expected voltage =", 3.3 * x / 100)
        p.start(x)
    p.stop()




finally:
    print ("Finally!")
    GPIO.output(pin, 0)
    GPIO.cleanup()