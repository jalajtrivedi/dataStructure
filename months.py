def get_days_in_month(month):
    # Check if the input month is valid
    if month < 1 or month > 12:
        return "Invalid month number. Please enter a number between 1 and 12."

    # Use conditional statements to determine the number of days in each month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28  # Assuming it's not a leap year

# Get user input
try:
    month = int(input("Enter a month number (1-12): "))
    days = get_days_in_month(month)
    print(f"Number of days: {days}")
except ValueError:
    print("Invalid input. Please enter a valid month number (1-12).")
