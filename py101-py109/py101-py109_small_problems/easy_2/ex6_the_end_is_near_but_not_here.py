# The End Is Near But Not Here

# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.


def penultimate(string):
    words = string.split()
    return words[-2]

def middle(string):
    words_list = string.split()
    list_length = len(words_list)
    middle_word = words_list[(list_length // 2)]
    return middle_word

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(middle('launch school is yellow purple great'))