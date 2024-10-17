import math
a = 0
b = 1
x = float(input("Enter the base of the power tower: "))
n = int(input("Enter how many iterations you want: "))
while a < n:
    b = x**b
    print(b)
    a += 1