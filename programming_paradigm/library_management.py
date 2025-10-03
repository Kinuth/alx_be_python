class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def __repr__(self):
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"
    def return_book(self):
        self._is_checked_out = False
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self.books.append(book)

    
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return book
        return None

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return book
        return None

    def list_available_books(self):
        return [book for book in self.books if not book._is_checked_out]