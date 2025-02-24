#3.Write a program to check the given string is palindrome or not
string= input('Enter a String:')
string= string.replace(" ","").lower()
if string==string[::-1]:
    print('The string is palinedrome')
else:
    print('The string is not palindrome')