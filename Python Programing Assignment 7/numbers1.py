# Write a python program that creates a list of numbers from 1 to 20 that are divisible by 4

divisible_by_4 = []
for num in range(1, 21):
    if num % 4 == 0:
        divisible_by_4.append(num)

print(divisible_by_4)