with open("settings_test.txt", 'w') as set:
    set.write(str(5.29385623) + '\n')
    # set.write(str(7.29385623) + '\n')
with open("settings_test.txt", 'r') as file:
    x = file.read()
    # y = float(file.readline())
print (x)
# print (y)