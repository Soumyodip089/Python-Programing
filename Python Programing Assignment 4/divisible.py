#8.Write a python program that creates a list of numbers from 1 to 20 that are divisible by 4.

numbers = []
for i in range(1, 21):
    if i % 4 == 0:
        numbers.append(i)
print("Numbers from 1 to 20 that are divisible by 4:")
print(numbers)
