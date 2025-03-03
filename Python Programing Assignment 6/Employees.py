#8.Write a Python program to count the number of employees earning more than 1 lakh per annum

employees = {"Soumyodip": 95000,"Saptak": 120000,"Preetam": 105000,"Vishal": 98000,"Akash": 150000}
high_earners = sum(1 for salary in employees.values() if salary > 100000)
print(f"Number of employees earning more than ₹1,00,000 per annum: {high_earners}")