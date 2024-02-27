# rock_paper_scissors.py

# Game flow:
# 1. The user makes a choice
# 2. The computer makes a choice
# 3. The winner is displayed

import random

VALID_USER_CHOICES = ['rock', 'r', 'paper', 'p', 'scissors', 'sc', 'lizard', 'l', 'spock', 'sp']
COMPUTER_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard':   ['paper', 'spock'],
    'spock':    ['rock', 'scissors'],
}

def prompt(message):
    print(f'==> {message}')

def convert_to_full(player):
    if player == 'r':
        return 'rock'
    elif player == 'p':
        return 'paper'
    elif player == 'sc':
        return 'scissors'
    elif player == 'l':
        return 'lizard'
    elif player == 'sp':
        return 'spock'
    else:
        return player

def display_choices(player, computer):
    if player != computer:
        prompt(f'You chose {player}, computer chose {computer}.')
    else:
        prompt(f'You chose {player}, computer also chose {computer}.')

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def determine_winner(player, computer):
    did_player_win = player_wins(player, computer)

    if did_player_win is True:
        scoreboard['player'] += 1
        return "player"
    elif player == computer:
        scoreboard['tie'] += 1
        return "tie"
    else:
        scoreboard['computer'] += 1
        return "computer"

def display_round_winner(string):
    if string == "player":
        prompt("You win this round!")
    elif string == "computer":
        prompt("Computer wins this round!")
    else:
        prompt("It's a tie!")

def display_score():
    prompt(f"Player: {scoreboard['player']}. Computer: {scoreboard['computer']}. "
           f"Ties: {scoreboard['tie']}.")

# Welcome message
prompt('Welcome to Rock, Paper, Scissors, Lizard, Spock.\n'
       'Best of 5 wins the match. Good luck.')

# Loop to continue playing
while True:
    round_count = 1
    scoreboard = {'player': 0, 'computer': 0, 'tie': 0}

    while True:
        prompt(f'--- Round {round_count} ---')
        prompt(f'Choose one: {", ".join(COMPUTER_CHOICES)}.')
        prompt('You may also input the first letter in each choice, '
                'or the first two letters for "scissors" and "spock".')
        choice = input().lower()
        while choice not in VALID_USER_CHOICES:
            prompt("That's not a valid choice.")
            choice = input()
        choice = convert_to_full(choice)

        computer_choice = random.choice(COMPUTER_CHOICES)
        display_choices(choice, computer_choice)

        winner = determine_winner(choice, computer_choice)
        display_round_winner(winner)

        # calculate_score(winner)
        display_score()

        round_count += 1

        # Stop playing once any player reaches 3 points,
        # which guarantees that they win the Best of 5 match.
        if scoreboard['player'] == 3:
            prompt("Congratulations! You've won the match!")
            break
        elif scoreboard['computer'] == 3:
            prompt("Computer won the match. Better luck next time.")
            break

    prompt("That was a good game. Do you want to play again (y/n)? ")
    answer = input().lower()
    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt('Please enter "y" or "n". ')
        answer = input().lower()

    if answer[0] == 'n':
        prompt("We look forward to seeing you again.")
        break
