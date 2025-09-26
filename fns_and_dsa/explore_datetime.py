from datetime import datetime, timedelta
# Get the current date and time

def display_current_datetime():
    """Display the current date and time in a readable format."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

current_date = display_current_datetime()
print(f"Current Date and Time: {current_date}")

number_of_days = int(input("Enter number of days to add to the current date: "))

def calculate_future_date(days):
    """Calculate the date after adding a certain number of days to the current date."""
    now = datetime.now()
    future_date = now + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")

print(f"Date after {number_of_days} days: {calculate_future_date(number_of_days)}") 

