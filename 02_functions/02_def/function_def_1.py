# Write a function is_palindrome(text) that checks if a string is a palindrome
# (reads the same forwards and backwards).
# The function should return True or False.
def sum_even(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total


# example
print(sum_even([1, 2, 3, 4, 5, 6]))
# def1
