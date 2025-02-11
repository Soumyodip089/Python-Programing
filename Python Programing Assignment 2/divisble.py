#Write a program to take two numbers and print if the first number is fully divisible by second number or not
a=int(input("Enter the first number:"))
b=int(input("Enter the second number"))
if(b==0):
    print("The denominator should not be zero")
elif(a%b==0):
    print("The 1st no. is fully divisible by 2nd no.")
else:
    print("The 1st no. is  not fully divisible by 2nd no.")