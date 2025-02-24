#3.Write a python program to create a list using for loop which consist square of the integers 1 through 50

squares = []
for i in range(1, 51):
    squares.append(i ** 2)
print("List of squares of integers 1 through 50:")
print(squares)
