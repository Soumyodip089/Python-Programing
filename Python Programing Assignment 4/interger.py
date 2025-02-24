#7.Write a python program to accept a integer number and find the followings:
#i.Sum of all digit
#ii.The largest digit of a given number.
#iii.Count the number of digits in given number.
#iv.The difference between greatest and smallest digits presents in the number.
#v.The frequency of digits presents in given number.

def calculate_digit_properties(num):
    num_str = str(num)
    sum_of_digits = 0
    largest_digit = 0
    smallest_digit = 9
    digit_frequency = {}
    num_digits = len(num_str)
    for digit in num_str:
        digit_int = int(digit)
        sum_of_digits += digit_int
        if digit_int > largest_digit:
            largest_digit = digit_int
        if digit_int < smallest_digit:
            smallest_digit = digit_int
        if digit_int in digit_frequency:
            digit_frequency[digit_int] += 1
        else:
            digit_frequency[digit_int] = 1
    digit_difference = largest_digit - smallest_digit
    print("Sum of all digits:", sum_of_digits)
    print("Largest digit:", largest_digit)
    print("Smallest digit:", smallest_digit)
    print("Number of digits:", num_digits)
    print("Difference between greatest and smallest digits:", digit_difference)
    print("Frequency of digits:")
    for digit, frequency in digit_frequency.items():
        print(f"{digit}: {frequency}")
num = int(input("Enter an integer number: "))
calculate_digit_properties(num)
