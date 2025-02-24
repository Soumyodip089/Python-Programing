#3.Write a python program to check number and then check is it positive negative or zero.

num = float(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")