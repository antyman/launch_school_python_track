# easy_1_isnt_it_odd.py

# Isn't it Odd?

# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# Input: one integer
# Output: Boolean, True if the number's absolute value is odd.

def is_odd(input):
    return abs(input) % 2 == 0

# Test cases
print(is_odd(-1))
print(is_odd(42))
print(is_odd(0))
print(is_odd(5))