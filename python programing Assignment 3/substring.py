# Write  a program to print the number of occurrencs of a substring into a line
Line=input('Enter a line:')
substring=input('Enter a substring:')
count=Line.count(substring)
print(f'The substring {substring} occurs {count} times in the line')