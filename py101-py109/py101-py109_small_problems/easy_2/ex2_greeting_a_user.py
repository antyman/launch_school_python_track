# # greeting a user

# Greeting a user

# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

def greeting():
        user_name = input('What is your name? ')
        if user_name.endswith('!'):
            return f'HELLO {user_name.upper()} WHY ARE WE YELLING?'
        else:
            return f'Hello, {user_name}.'


print(greeting())
