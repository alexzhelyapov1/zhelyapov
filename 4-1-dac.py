import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * len (dac)
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)


try:
    while True:
        a = input ("Print digit pls\n")
        if not a.isdigit() or int(a) > 255 or int(a) < 0:
            if a == 'q':
                break
            print ("Wrong digit")
            continue
        x = int(a)
        print("Expected voltage =", 3.3 * x / 256)
        for i in range (7, -1, -1):
            number[i] = x % 2
            x >>= 1
        # Тестовый вывод
        print (number)

        GPIO.output (dac, number)
        # time.sleep(3)


finally:
    print ("Finally!")
    GPIO.output(dac, 0)
    GPIO.cleanup()