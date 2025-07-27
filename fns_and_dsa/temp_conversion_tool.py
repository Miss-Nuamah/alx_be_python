# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    Formula: (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Get user input for temperature
        temp_input = input("Enter the temperature value: ").strip()
        if not temp_input.replace(".", "", 1).isdigit() and not (
            temp_input.startswith("-") and temp_input[1:].replace(".", "", 1).isdigit()
        ):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp_value = float(temp_input)
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value:.2f}°C is {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value:.2f}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
