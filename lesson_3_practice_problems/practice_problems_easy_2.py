# Question 1: Write two distinct ways of reversing the list without mutating the original list.

# Copy Code
# numbers = [1, 2, 3, 4, 5]
# Hint 1
# Hint 2

# Answer:

# Method 1 - Slicing
# reverse = numbers[::-1]
# print(numbers)
# print(reverse)

# Method 2 - Only works because the original sequence was already sorted. If the original list was not sorted, eg. [1, 2, 4, 3], it would sort and reverse, which would not have solved this problem.
# reverse2 = sorted(numbers, reverse = True)
# print(numbers)
# print("fefef", reverse2)

# Method 3
# reverse3 = list(reversed(numbers))
# print(numbers)
# print(reverse3)


# Question 2: Given a number and a list, determine whether the number is included in the list.

# Copy Code
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False
number2 = 95 # True

# Answer:
# print(number1 in numbers)
# print(number2 in numbers)


# Question 3: Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101,

# Hint

# print(42 in range(10,101))
# print(100 in range(10,101))
# print(101 in range(10,101))



# Question 4: Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2, so that the list becomes [1, 2, 4, 5].


# Answer:
# lst = [1, 2, 3, 4, 5]
# lst.pop(2)
# print(lst)

# Other answer:
# del lst[2]
# print(lst)

# Question 5: How would you verify whether the data structures assigned to the variables numbers and table are of type list?

# Copy Code
# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# Answer (per LS, this answer has potential issues):
# print(type(numbers) is list)
# print(type(table) is list)

# Answer 2:
# print(isinstance(numbers, list))
# print(isinstance(table, list))


# Question 6: Back in the stone age (before CSS), we used spaces to align things on the screen. If we have a 40-character wide table of Flintstone family members, how can we center the following title above the table with spaces?

# Copy Code
# title = "Flintstone Family Members"

# Answer:
# print(title.center(40))



# Question 7: Write a one-liner to count the number of lower-case t characters in each of the following strings:

# Copy Code
# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# Answer:
# print(statement1.count('t'))
# print(statement2.count('t'))

# Question 8: Determine whether the following dictionary of people and their age contains an entry for 'Spot':

# Copy Code
# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# Answer:
# print('Spot' in ages)

# Question 9: We have most of the Munster family in our ages dictionary:

# Copy Code
# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
# Add entries for Marilyn and Spot to the dictionary:

# Copy Code
# additional_ages = {'Marilyn': 22, 'Spot': 237}

# all_ages = ages | additional_ages
# ages.update(additional_ages)

# print(ages)




