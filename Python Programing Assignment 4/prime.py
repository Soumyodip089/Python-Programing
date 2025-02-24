#6.Write a python program that searches for prime numbers from 15 through 25

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in range(15, 26) if is_prime(num)]
print("Prime numbers from 15 through 25:")
print(prime_numbers)
