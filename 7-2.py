import numpy as np
import matplotlib.pyplot as plt

with open("data.txt") as file:
    array = [float (row.strip()) for row in file]
with open("settings.txt") as file:
    time_of_charging = float (file.readline())
    time_all = float (file.readline())
print (time_all)
vals = np.array(array)
time = np.linspace(0, time_all, len(vals))

fig, ax = plt.subplots()
plt.title('Процесс разряда и разряда конденсатора', fontsize=16, fontweight= "bold")
plt.xlabel('Время, c', fontsize=14, fontstyle= "italic")
plt.ylabel('Напряжение, В', fontsize=14, fontstyle= "italic")
plt.plot (time, vals, 'r')
plt.text (5, 0.3, "Время зарядки  = " + str(int(time_of_charging)) + ' c', color = "blue")
plt.text (5, 0.2, "Время разрядки = " + str(int(time_all - time_of_charging)) + ' c', color = "green")
plt.xlim ((-0.1 * int(time_all), int(time_all) * 1.1))
plt.ylim ((-max(vals)*0.1, max(vals) + max(vals)*0.1))

ax.minorticks_on()
ax.grid(which='major', color = 'k', linewidth = 0.5)
ax.grid(which='minor', color = 'k', linestyle = ':', linewidth = 0.5)



plt.savefig('graph.svg')
plt.show()