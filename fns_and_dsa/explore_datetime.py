# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return the datetime object for reuse


def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date,
    and prints it in the format YYYY-MM-DD.
    """
    try:
        days_to_add = int(input("Enter the number of days to add: ").strip())
        future_date = current_date + timedelta(days=days_to_add)
        print(f"The date after {days_to_add} days will be: {future_date.strftime('%Y-%m-%d')}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")
        return None


def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate and display a future date
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
