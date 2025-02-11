#Write a program to take a 3-digit number and then print the reversed number. That is, if you input 123, the program should print 321
num = int(input("Enter a 3-digit number: "))
reversed_num = int(str(num)[::-1])
print("The reversed number is:", reversed_num)