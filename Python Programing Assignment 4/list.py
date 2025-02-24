#10.Write a python program to create a list of numbers in the range 1 to 10 Then delete all the even numbers from the list and print the final list.

numbers = list(range(1, 11))
print("Original List:")
print(numbers)
numbers = [num for num in numbers if num % 2 != 0]
print("\nFinal List (after deleting even numbers):")
print(numbers)
