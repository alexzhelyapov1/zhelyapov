def dec2bin(x, number):
    for i in range (7, -1, -1):
        number[i] = x % 2
        x >>= 1
    print(number)

dec2bin(7)