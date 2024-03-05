# practice_problems_hard_1.py

# Question 1: Will the following functions return the same results?

# def first():
#     return {
#         'prop1': "hi there",
#     }

# def second():
#     return
#     {
#         'prop1': "hi there",
#     }

# print(first())
# print(second())

# Answer: The first will return the dict, the second will return None



# Question 2: What does the last line in the following code output?

# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list)
# print(dictionary)


# Answer:
# [1, 2]
# {'first': [1, 2]}
# num_list is a reference to the original dictionary so appending to num_list modifies the list within the dictionary.



# Question 3: Given the following similar sets of code, what will each code snippet print?

# A:

# def mess_with_vars(one, two, three):
#     one = two
#     two = three
#     three = one

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # one is: ["one"]
# print(f"two is: {two}") # two is: ["two"]
# print(f"three is: {three}") # three is: ["three"]


# B:

# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # one is: ["one"]
# print(f"two is: {two}") # two is: ["two"]
# print(f"three is: {three}") # three is: ["three"]


# C:

# def mess_with_vars(one, two, three):
#     one = ["two"]
#     two = ["three"]
#     three = ["one"]

# one = ["one"]
# two = ["two"]
# three = ["three"]

# mess_with_vars(one, two, three)

# print(f"one is: {one}") # one is: ["two"]
# print(f"two is: {two}") # two is: ["three"]
# print(f"three is: {three}") # three is: ["one"]

# Explanation: There's variable shadowing occuring in all three pieces of code, so the variables within the functions are not the same as the ones made outside of the function. In code set C, the function modifies the content of the list directly. Since lists in Python are mutable and passed by reference, the changes are reflected outside of the function.



# Question 4:

# Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

# Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:


# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break

    # return True

# Help Ben fix his code.

# def is_an_ip_number(str):
#     if str.isdigit():
#         number = int(str)
#         return 0 <= number <= 255
#     return False

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             return False

#     return True

# print(is_dot_separated_ip_address('192.168.0.1'))


# Question 5

# What do you expect to happen when the greeting variable is referenced in the last line of the code below?

# Answer: Error because the variable is not initialized. "NameError"