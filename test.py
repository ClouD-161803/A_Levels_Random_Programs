import random

x = random.randint(0000,9999)

while x != guess:
    guess = int(input("Enter a 4 digit number: "))

    guessarray = []

    for digit in str(guess):
        guessarray.append(digit)

    for i in range(1,5):