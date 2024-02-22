# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Added json config file in lieu of prompt function to improve flexibility and internationalization.
# def prompt(message): 
#     print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang="en"):
    return MESSAGES[lang][message]

print('Please select a language:\n"en": English; "fr": French; "de": German; "es": Spanish')

# Check for appropriate language selection.
while True:
    LANGUAGE = input()
    if LANGUAGE in ["en", "fr", "de", "es"]:
        break
    print('Invalid input. Please select from the following:\n"en": English; "fr": French; "de": German; "es": Spanish')

print(messages('welcome', LANGUAGE))

while True:
    # Ask the user for the first number.
    print(messages('first_number', LANGUAGE))
    number1 = input()

    while invalid_number(number1):
        print(messages('invalid_number', LANGUAGE))
        number1 = input()

    # Ask the user for the second number.
    print(messages('second_number', LANGUAGE))
    number2 = input()

    while invalid_number(number2):
        print(messages('invalid_number', LANGUAGE))
        number2 = input()

    # Ask the user what operation they'd like to perform.

    print(messages('operation', LANGUAGE))
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        print(messages('operation_selection', LANGUAGE))
        operation = input()

    match operation:
        case '1': # '1' represents addition
            output = float(number1) + float(number2)
        case '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3': # '3' represents multiplcation
            output = float(number1) * float(number2)
        case '4': # '4' represents division
            output = float(number1) / float(number2)

    print(messages('result', LANGUAGE), output)
    print(messages('repeat', LANGUAGE))
    answer = input()
    if answer.lower() != 'yes':
        break