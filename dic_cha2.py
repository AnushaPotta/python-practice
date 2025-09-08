student = {
    "name" : "Carter",
    "Maths" : 75,
    "Science" : 70,
    "English" : 80
}

print(f"Student name is: {student['name']}")

avg = (student["Maths"] + student["English"] + student["Science"])/3

student["avg_score"] = avg

for key, value in student.items():
    print(f"{key}: {value}")