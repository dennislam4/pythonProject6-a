# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-26-2022
# Description: Recursive function that takes a list of numbers as a parameter and returns the max value in the list.

def list_max(numbers):
    """Recursive function that finds the maximum value in given num_list."""
    first_element = numbers[0]

    if len(numbers) == 1:
        return first_element
    elif len(numbers) > 1:
        maximum_value = list_max(numbers[1:])
        if first_element > maximum_value:
            maximum_value = first_element
        return maximum_value
