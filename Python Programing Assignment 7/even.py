#4.Write a python program to swap list elements with even and locations

def swap_even_odd_elements(input_list):
    for i in range(0, len(input_list) - 1, 2):
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
user_input = input("Enter the elements of the list: ")
input_list = list(map(int, user_input.split()))
print("Original list:", input_list)
swap_even_odd_elements(input_list)
print("Modified list:", input_list)
