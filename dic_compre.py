
#Create a dictionary where the keys are numbers from 1 to 10, 
# and the values are "Even" if the number is even and "Odd" if the number is odd.


dic_comprehen = {key: ("Even" if key % 2 == 0 else "Odd") for key in range(1, 11) }

print(dic_comprehen)