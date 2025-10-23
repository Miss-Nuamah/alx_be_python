class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a new book."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, title, author):
        """Add a new book to the library."""
        book = Book(title, author)
        self._books.append(book)
        return f"Added: {book}"
    
    def check_out_book(self, title):
        """Check out a book from the library."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"Checked out: {book}"
        return "Book not available"
    
    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f"Returned: {book}"
        return "Book not found or already returned"
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            return "\n".join(str(book) for book in available_books)
        return "No books available"