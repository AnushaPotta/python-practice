with open("students.txt", "w") as f:
    f.write("Alice\nCarter\nConner")


with open("students.txt", "r") as f:
    content = f.readlines()
    print(content)

with open("students.txt", "a") as f:
    f.write("\nJhonny")
    
    
with open("students.txt", "r") as f:
   
    new_content = f.readlines()
    print(new_content)
    

