#5.Write a python program to input any string and count number of uppercase and lowercase letters.

string = input("Enter a string: ")

uppercase_count = sum(1 for char in string if char.isupper())
lowercase_count = sum(1 for char in string if char.islower())

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")

