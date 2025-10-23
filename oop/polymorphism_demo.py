import math

class Shape:
    """Base class for geometric shapes."""
    
    def area(self):
        """Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This is an abstract method that must be implemented by derived classes.
        """
        raise NotImplementedError("Area calculation must be implemented by derived classes")


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius: float):
        """Initialize a circle with radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2


