#9.Write a Python Program to Create a dictionary whose keys are month name and whose values are number of days in the corresponding month

month_days = {
    "January": 31,
    "February": 28, 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
print("Month Days Dictionary:")
for month, days in month_days.items():
    print(f"{month}: {days} days")
