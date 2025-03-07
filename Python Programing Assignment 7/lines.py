#8. Write a program to write the follwing line

filename='file.txt'
lines= ['Apending a new line to the file','file handling is a essential skill']
with open (filename,'w')as file:
    for line in lines:
        file.write(line + '\n')
print(f'line written to {filename} succesfully')

