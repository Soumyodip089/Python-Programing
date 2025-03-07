#9. Write a python program to read a file line by line

#filename = input('Enter the file name: ')
#try:
    #file = open(filename, 'r')
    #for line in file:
        #print(line.strip())  
    #file.close()  
#except FileNotFoundError:
    #print(f'File {filename} not found.')


with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
