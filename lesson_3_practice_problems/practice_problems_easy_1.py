# practice_problems_easy_1

#Question 1: Will the code below raise an error?

# Copy Code
# numbers = [1, 2, 3]
# numbers[6] = 5

# Answer:

# Yes. Python won't allow creating new values to a list with the indexing syntax, and requires consecutive numbers as indices (no gaps).


# Question 2: How can you determine whether a given string ends with an exclamation mark (!)?

# Copy Code
# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# Answer:

# str1.endswith('!')


# Question 3: Starting with the string:

# Copy Code
# famous_words = "seven years ago..."
# Show two different ways to put the expected "Four score and " in front of it.
# famous_words_pre = "Four score and "

# method_1 = famous_words.replace('s', famous_words_pre + "s", 1)
# method_2 = famous_words_pre + famous_words
# method_3 = f'Four score and {famous_words}'

# print(method_1)
# print(method_2)
# print(method_3)


# Question 4: Using the following string, create a new string that contains all lowercase letters except for the first character, which should be capitalized.

# Copy Code
# munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

# Answer:
# print(munsters_description.capitalize())


# Question 5: Starting with the string:

# Copy Code
# munsters_description = "The Munsters are creepy and spooky."
# Return a new string that swaps the case of all of the letters:

# Copy Code
# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# Answer:
# print(munsters_description.swapcase())

# Question 6: Determine whether the name Dino appears in the strings below -- check each string separately:

# Copy Code
# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# Answer:
# print("Dino" in str1)
# print("Dino" in str2)

# Question 7: How can we add the family pet, "Dino", to the following list?

# Copy Code
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# Answer:
# flintstones.append('Dino')
# print(flintstones)


# Question 8: In the previous problem, our first answer added 'Dino' to the list like this:

# Copy Code
# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.

# Answer:
# flintstones.insert(6, "Dino")
# flintstones.insert(7, "Hoppy")

# flintstones.extend(['Dino', 'Floppy'])

# print(flintstones)


# Question 9: Return a new version of this sentence that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

# Copy Code
# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected return value:
# # => 'Few things in life are as important as '

# Answer:
# print(advice[0:advice.find('house')])

# Better answer:
# print(advice.split("house")[0])



# Question 10: Replace the word "important" with "urgent" in this string:

# Copy Code
# advice = "Few things in life are as important as house training your pet dinosaur."

# Answer:

# print(advice.replace('important', 'urgent'))
