# student.py
from member import LibraryMember

class Student(LibraryMember):
    def borrow_book(self, book):
        if book.is_available():
            book.set_availability(False)
            print(f"Student {self.name} borrowed {book.title}")
        else:
            print(f"Sorry {self.name}, {book.title} is not available.")

