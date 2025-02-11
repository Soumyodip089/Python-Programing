#Write a program to input a single digit(n) and print a 3 digit number created as <n(n+1)(n+2)> e.g., if you input 7, then it should print 789. Assume that the input digit is in range 1-7
n = int(input("Enter a single digit (1-7): "))
if 1 <= n <= 7:
    num = int(f"{n}{n+1}{n+2}")
    print(f"The 3-digit number is: {num}")
else:
    print("Invalid input. Please enter a digit between 1 and 7.")