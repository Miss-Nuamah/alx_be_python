class Book:
    """Base class representing a book."""
    
    def __init__(self, title: str, author: str):
        """Initialize a book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author


class EBook(Book):
    """Class representing an electronic book."""
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an ebook with title, author and file size.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): Size of the ebook file in MB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, Size: {self.file_size}MB"


class PrintBook(Book):
    """Class representing a physical printed book."""
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a print book with title, author and page count.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): Number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"


class Library:
    """Class representing a library that can store different types of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self.books = []
    
    def add_book(self, book: Book):
        """Add a book to the library.
        
        Args:
            book (Book): Instance of Book, EBook, or PrintBook to add
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("Library Contents:")
        for book in self.books:
            print(str(book))