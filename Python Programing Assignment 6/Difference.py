#6.Write a python program to find the difference between greatest and smallest digits presents in the number.

num = int(input("Enter an integer number: "))
digits = [int(d) for d in str(abs(num))]


print("Greatest  digit:", max(digits))
print("Smallest  of digits:", min(digits))