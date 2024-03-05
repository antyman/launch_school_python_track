# # easy_1_utf-16_string_value.py

# UTF-16 String Value

# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

def utf16_value(string):
    utf_sum = 0
    for char in string:
        utf_sum += ord(char)
    return utf_sum


print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)