import datetime

# Get the current date and time
now = datetime.datetime.now()

def display_current_datetime():
    """Display the current date and time in a readable format."""
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
current_date = display_current_datetime()
print(f"Current Date and Time: {current_date}")

number_of_days = int(input("Enter number of days to add: "))

def calculate_future_date(days):
    """Calculate the date after adding a certain number of days to the current date."""
    future_date = now + datetime.timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")
print(f"Date after {number_of_days} days: {calculate_future_date(number_of_days)}") 

