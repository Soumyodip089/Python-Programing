#1.Write a python program to input two list and create third list which contains all elements of the first elements followed by all elements of second list.

l1 = input("Please enter a list : ").split()
l2 = input("Please enter a list : ").split()
l3 = l1 + l2
print(type(l3),l3)