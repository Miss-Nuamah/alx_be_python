class Book:
    """A class representing a book."""
    
    def __init__(self, title: str, author: str, year: int):
        """Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """Return a string representation of the book.
        
        Returns:
            str: Book information in format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return the official string representation of the book.
        
        Returns:
            str: String that could be used to recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"