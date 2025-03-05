#7. Write a python program to append data to and exisiting file

fi = input("Enter a filename: ")
data = input("Enter new data to be entered: ")
file = open(fi,'a')
file.write(data + "\n")
file.close()
print(f"Data append to {fi} succesfully")

