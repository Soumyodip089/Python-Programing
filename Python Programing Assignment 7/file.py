#5. Write a python program to create and write to a file in python

fi = input('Enter a filename: ')

if open(fi, 'r').readable():
    file= open(fi,'r')
    data=file.read()
    print('File contains: ')
    print(data)
    file.close()
else:
    print(f"File '{fi}' not found or cannot be read.")
    
 