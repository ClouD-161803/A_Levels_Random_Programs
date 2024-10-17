factorCount = 0
continue_ = True

while continue_:
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Not greater than 1")
        num = int(input("Enter a number: "))
    else:
        for x in range(1, num+1):
            div = num / x
            rounded = round(div)
            if div == rounded:
                factorCount += 1

    if factorCount == 2:
        print("Is prime")
    else:
        print("Is not prime")

    cont = int(input("Enter \"0\" if you want to stop, \"1\" if you want to enter another number:\n"))
    if cont == 0:
        continue_ = False
    elif cont == 1:
        continue_ = True
    else:
        print("Invalid selection")