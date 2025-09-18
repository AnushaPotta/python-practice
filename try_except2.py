
try:
    num1 = float(input("Enter the dividend: "))

    num2 = float(input("Enter the divisor: "))

    result = num1/num2

    print(result)

except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Enter only numbers")

except Exception as e:
    print("There seems to be a problem! try gain")
    print("Error detail:", e)








