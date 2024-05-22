# Recursion training

list_of_numbers = [1, 18, 4, 35, 16, 32]

def largest_recursive(numbers):
    if len(numbers) == 1:
        return numbers[0] # The base case would be if there is only 1 number in the list.
    else:
        other_numbers = largest_recursive(numbers[1:])
        return max(numbers[0], other_numbers) 
    # Learned the max() function on: https://www.programiz.com/python-programming/methods/built-in/max

largest_number = largest_recursive(list_of_numbers)
print(f'List of numbers: {list_of_numbers}.')
print(f'The largest number in the list is: {largest_number}.')

list_of_numbers = [1, 2, 4, 8, 16, 32]
index_num = 3 # Same as 1 + 2 + 4 + 8.

def adding_numbers_to_index(numbers, index):
    if index < 0:
        return 0
    elif index >= len(numbers):
        return sum(numbers) # Any index number given higher than len just gives the total.
    else:
        return numbers[index] + adding_numbers_to_index(numbers, index - 1) # Working back to number 1.

result = adding_numbers_to_index(list_of_numbers, index_num)
print(f'List of numbers: {list_of_numbers}.')
print(f'Adding up the numbers to index: {index_num}. \nResult: {result}.')