from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
display_current_datetime()

def calculate_future_date():
    day_to_add = int(input("Enter the number of days to add to the current date: "))
    c_date = datetime.now()
    future_date = c_date + timedelta(days=day_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

calculate_future_date()
