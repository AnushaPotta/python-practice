book = {
    "title" : "Harry Potter",
    "author" : "J.K Rowling",
    "year" : 2007

}

print(f"Author of the book is {book['author']}")

book["genre"] = "fiction"

for key, value in book.items():
    print(f"{key}: {value}")