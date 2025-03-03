#12.Write a Python program to print the sum of series 1^3 + 2^3 + 3^3 + 4^3 + .......+ n^3 till n-th term. N is the value given by the user.

n = int(input("Enter the value of N: "))
sum_of_series = sum(i**3 for i in range(1, n + 1))
print(f"Sum of the series 1^3 + 2^3 + ... + {n}^3 = {sum_of_series}")
