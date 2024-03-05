# # practice_problems_easy_3.py

# Question 1: Write two different ways to remove all of the elements from the following list:

# Copy Code
# numbers = [1, 2, 3, 4]

# Answer:

# Method 1:

# while numbers:
#     numbers.pop()

# print(numbers)

# Method 2:

# numbers.clear()

# print(numbers)

# Question 2: What will the following code output?

# Copy Code
# print([1, 2, 3] + [4, 5])
# Try to answer without running the code.

# Answer:


# Question 3: What will the following code output?

# Copy Code
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)
# Try to answer without running the code.

# Answer:
# The code will print "hello there". Strings are immutable so the only way to change the value of str1 is to reassign it. When we do str2 = str1, we are pointing str2 to the same memory location as the original string. Reassigning str2 change sthe memory location that the str2 variable points to, and does not affect the value of str1.

# Question 4: What will the following code output?

# Copy Code
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)
# Try to answer without running the code.

# Answer:
# [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# copy() make a shallow copy, which means both my_list1 and my_list2 point to the same set of integers and dictionaries. In line 3, when we replace the value of 'first', the change shows up on my_list1 as well.


# Question 5 The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?

# Copy Code
# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False
# Try to come up with two different solutions.

# Answer:

# Method 1:

# def is_color_valid(color):
#     return color in ["blue", "green"]

# Method 2:
# def is_color_valid(color):
#     return color == "blue" or color == "green"