# library.py
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def show_books(self):
        print("\n📚 Library Collection:")
        for book in self.books:
            print(book)
