person = ("Emma", 30, "Sanfrancisco")

name = person[0]
age = person[1]
city = person[2]

print(f"{name} is {age} years old and lives in {city}.")

if name in person:
    print(True)