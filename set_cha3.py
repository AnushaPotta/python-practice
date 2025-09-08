#Find students who study all 3 subjects.

#Find students who study Math but not Science.

#Find students who study at least one subject.

#Count how many unique students are there in total.

math = {"Alice", "Bob", "Charlie", "David"}
science = {"Charlie", "Eve", "Alice", "Frank"}
english = {"George", "Bob", "Alice", "Helen"}


print(math & science & english)

print(math - science)

print(math | science | english)

print(len(math | science | english))

