#5.Write a python program to print first n odd numbers in descending order.

n = int(input("Enter a integer: "))
odd_numbers = []
for i in range(n):
    odd_numbers.append(2*(n-i) - 1)
print("First", n, "odd numbers in descending order:")
print(odd_numbers)
