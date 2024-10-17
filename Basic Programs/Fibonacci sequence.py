n1 = 0
n2 = 1
Num = int(input("Enter how many numbers of the series you want: "))
if Num == 0:
    print("At least one number required")
elif Num == 1:
    print(0)
else:
    i = 0
    print(n1)
    print(n2)
    while i < Num - 2:
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
        i += 1