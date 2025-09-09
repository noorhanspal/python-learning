# book.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True   # Private attribute

    # Getter
    def is_available(self):
        return self.__available

    # Setter
    def set_availability(self, status):
        self.__available = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.__available else 'Not Available'}"
