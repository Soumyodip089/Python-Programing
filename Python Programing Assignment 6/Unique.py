#1.Write a python program to input 3 numbers from user and check these are unique numbers or not

def check_unique_number():
    num1 = int(input("Enter first no: "))
    num2 = int(input("Enter second no: "))
    num3 = int(input("Enter third no: "))

    if num1 != num2 and num2 != num3 and num1 != num3:
        print("The numbers are unique.")
    else:
        print("The numbers are not unique")

check_unique_number()