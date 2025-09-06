numbers = [10 ,20, 80, 40, 50]
max_num = numbers[0]

for num in numbers:
    print(num)
    if  num > max_num:
        max_num = num

print(f"largest number is: {max_num}")

