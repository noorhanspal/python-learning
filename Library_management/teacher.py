# teacher.py
from member import LibraryMember

class Teacher(LibraryMember):
    def borrow_book(self, book):
        if book.is_available():
            book.set_availability(False)
            print(f"Teacher {self.name} borrowed {book.title} (priority given to teachers).")
        else:
            print(f"Sorry {self.name}, {book.title} is not available.")
