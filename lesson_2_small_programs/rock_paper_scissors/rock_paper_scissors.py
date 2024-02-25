# rock_paper_scissors.py

# Game flow:
# 1. The user makes a choice
# 2. The computer makes a choice
# 3. The winner is displayed

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    prompt(f'You chose {player}, computer chose {computer}.')

    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt('Do you want to play again (y/n)? ')
    answer = input().lower()
    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt('Please enter "y" or "n". ')
        answer = input().lower()

    if answer[0] == 'n':
#         break


# Alternate loop if for some reason we wanted to avoid using a "break" to break the loop.
# answer = 'yes'

# while answer[0] == 'y':

#     prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
#     choice = input()
#     while choice not in VALID_CHOICES:
#         prompt("That's not a valid choice.")
#         choice = input()

#     computer_choice = random.choice(VALID_CHOICES)

#     display_winner(choice, computer_choice)

#     prompt('Do you want to play again (y/n)? ')
#     answer = input().lower()
#     while True:
#         if answer.startswith('y') or answer.startswith('n'):
#             break

#         prompt('Please enter "y" or "n". ')
#         answer = input().lower()
