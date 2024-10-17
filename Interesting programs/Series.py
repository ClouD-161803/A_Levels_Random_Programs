import sys

print("This algorithm can evaluate series written in one of the following forms:")
print("   n           "+"n             "+"n")
print("A: ∑"+"(r)     "+"B: ∑"+"(r^2)     "+"C: ∑"+"(r^3)")
print("  r=k         "+"r=k           "+"r=k")
print(" ")

choice = input("Enter \"A\", \"B\" or \"C\": ")

if choice != "A" and choice != "B" and choice != "C" and choice != "a" and choice != "b" and choice != "c" :
    sys.exit("Invalid selection")
else:
    n = int(input("Enter a positive integer for n: "))
    k = int(input("Enter a positive integer for k: "))
    print(" ")

def A():
    if k == 1:
        result = 0.5*n*(n+1)
        return result
    elif k > 1:
        result = (0.5*n*(n+1)) - (0.5*(k-1)*(k))
        return result
    else:
        print("Invalid input")

def B():
    if k == 1:
        result = ((1/6)*n*(n+1)*(2*n+1))
        return result
    elif k > 1:
        result = ((1/6)*n*(n+1)*(2*n+1) - (1/6)*(k-1)*(k)*(2*k-1))
        return result
    else:
        print("Invalid input")

def C():
    if k == 1:
        result = ((1/4)*(n**2)*((n+1)**2))
        return result
    elif k > 1:
        result = ((1/4)*(n**2)*((n+1)**2) - (1/4)*((k-1)**2)*(k**2))
        return result
    else:
        print("Invalid input")

if k > n:
    print("Argument error: k cannot be greater than n")
elif k < 0 or n < 0:
    print("Invalid input: n and k have to be positive integers")
else:
    if choice == "A" or choice == "a":
        ans = A()
        print("Answer: "+str(ans))
    elif choice == "B" or choice == "b":
        ans = B()
        print("Answer: "+str(ans))
    elif choice == "C" or choice == "c":
        ans = C()
        print("Answer: "+str(ans))