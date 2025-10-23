def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers and returns appropriate messages.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        str: Error message if operation fails
        float: Result of division if successful
    """
    try:
        # Try to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Attempt division
        result = num / den
        return result
        
    except ValueError:
        return "Error: Both inputs must be numeric values"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"