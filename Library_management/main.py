# main.py
from book import Book
from library import Library
from student import Student
from teacher import Teacher

# Create Library
library = Library()

# Create Books
b1 = Book("Python Basics", "Guido van Rossum", "101")
b2 = Book("OOPS in Python", "Rossum", "102")

# Add Books
library.add_book(b1)
library.add_book(b2)

# Create Members
s1 = Student("Noor", "S01")
t1 = Teacher("Simran", "T01")

# Borrowing
s1.borrow_book(b1)
t1.borrow_book(b2)

# Show all books
library.show_books()
