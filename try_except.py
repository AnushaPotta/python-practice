import math

try:
    num = float(input("Enter a number: "))
    if num < 0:
        print("Enter a positive number")
    else:
        print(f"Sqrt is: {math.sqrt(num)}")
except ValueError:
    print("Enter a valid number")
