#Write a Python program to input 3 numbers and check all are same or not
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 == num2 == num3:
    print("All three numbers are the same.")
else:
    print("The numbers are not the same.")