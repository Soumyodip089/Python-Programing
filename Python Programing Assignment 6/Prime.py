#7.Write a python program that searches for prime numbers from 15 through 25.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 15 and 25:")
for num in range(15, 26):
    if is_prime(num):
        print(num, end=" ")