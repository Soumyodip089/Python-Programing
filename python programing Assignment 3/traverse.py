#Write a program that traverse through an input string and prints its characters in different lines two character per line
input_str = input('Enter a string:')
for i in range (0,len(input_str),2):
    print(input_str[i:i+2])
    