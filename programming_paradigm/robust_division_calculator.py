def safe_divide(numerator, denominator):
    """
    Safely performs division between two numbers.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        float: Result of the division
        
    Raises:
        ValueError: If inputs are not numeric
        ZeroDivisionError: If denominator is zero
    """
    try:
        # Convert inputs to float to handle both int and float inputs
        num = float(numerator)
        den = float(denominator)
        
        # Check for division by zero
        if den == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
            
        # Perform division
        return num / den
    
    except ValueError:
        raise ValueError("Both inputs must be numeric values")
    except ZeroDivisionError as e:
        raise e