# 10.Write a python program to copy content from one file to another

source_file = open("file.txt", "r")
destination_file = open("file1.txt", "w")
content = source_file.read()
destination_file.write(content)
source_file.close()
destination_file.close()
print("Content copied successfully!")
