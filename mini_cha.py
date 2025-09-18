import math, random

score = 0

for i in range(5):
    num = random.randint(1,10)
    choice = random.choice(["square", "sqrt"])
    print(f'Your question: {choice} of {num}')
    if choice == "square":
        result = num ** 2
    elif choice == "sqrt":
        result = math.sqrt(num)
    input_ans = float(input("Enter your answer: "))
    if input_ans == result:
        score += 1
        print(f"Yay, U got it right! Your score is {score}")
    else:
        print(f"Sorry, wrong answer! Correct answer was {result}.Your score is {score}")


print(f"Your score: {score}")

print(f"Quiz is done and your score will be saved to the file! Please enter your name")


name = input("Enter your name: ")

with open("quiz_score.txt", "a") as f:
    f.write(f"{name} score is: {str(score)}\n")





