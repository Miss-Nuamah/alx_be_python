class Calculator:
    """Simple calculator demonstrating staticmethod and classmethod."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print calculation_type then return the product of a and b."""
        print(cls.calculation_type)
        return a * b


