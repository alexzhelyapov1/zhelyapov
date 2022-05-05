import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np
import time

#----------------------Pins---------------------------
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0] * len (dac)
comp = 4
troyka = 17

#---------------------Modes---------------------------
GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT)
GPIO.setup (comp, GPIO.IN)
GPIO.output(dac, 0)

# Перевод в двоичную форму числа х. Заполняет массив number
def dec2bin(x, number):
    t = x
    for i in range (7, -1, -1):
        number[i] = t % 2
        t >>= 1

# Преобразователь аналогового сигнала в цифровой. 
# Возвращает значение в диапазоне от 0 до 256
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
    vals = np.array([]) #массив для записи полученных значений
    time_of_start = time.time() #время начала измерений
    k = 0 #переменная для хранения возвращаемого значения

    #-----------Зарядка конденсатора--------------------------
    GPIO.output (troyka, GPIO.HIGH)
    while k <= 256 * 0.90:
        k = adc_new()
        vals = np.append (vals, k)
        GPIO.output(dac, 0)
        time.sleep (0.01)

    time_of_mid = time.time() #момент начала разрядки конденсатора
    
    #-----------Разрядка конденсатора-------------------------
    GPIO.output (troyka, GPIO.LOW)
    while k >= 256 * 0.03:
        k = adc_new()
        vals = np.append(vals, k)
        GPIO.output(dac, 0)
        time.sleep (0.01)


    time_of_end = time.time() #время окончания измерений

    #----------------Запись в файл----------------------------
    with open ("data.txt", 'w') as data:
        for i in range (len(vals)):
            data.write(str(vals[i]) + '\n')
    with open("settings.txt", 'w') as set:
        set.write("Общее время эксперимента:\n")
        set.write(str(time_of_end - time_of_start) + '\n')
        set.write("Время зарядки:\n")
        set.write(str(time_of_mid - time_of_start) + '\n')
        set.write("Время периода:\n")
        set.write(str((time_of_end - time_of_start) / len(vals)) + '\n')
        set.write("Средняя частота дискретизации:\n")
        set.write(str(len(vals) / (time_of_end - time_of_start)) + '\n')
        

    #---------------Вывод графика-----------------------------
    plt.title('Процесс разряда и разряда конденсатора')
    plt.xlabel('Время, c')
    plt.ylabel('Возвращаемое значение, из 256')
    plt.plot(vals)
    plt.show()

finally:
    print ("Finally!")
    GPIO.output(dac, 0) #очистка значений на всех пинах
    GPIO.cleanup()
