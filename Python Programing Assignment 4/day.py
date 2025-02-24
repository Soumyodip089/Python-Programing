#2. Write a python program to read todays date only date Part from user Then display how many days are left in the current month.

import calendar
from datetime import datetime
date_str = input("Enter today's date (in DD-MM-YYYY format): ")
date = datetime.strptime(date_str, "%d-%m-%Y")
month = date.month
year = date.year
total_days = calendar.monthrange(year, month)[1]
days_left = total_days - date.day
print(f"There are {days_left} days left in the current month.")
