class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python", 300)
b2 = Book("Java", 250)

print(b1)         # Output: Python (300 pages)
print(b1 + b2)    # Output: 550

