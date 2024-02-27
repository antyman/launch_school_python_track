# rock_paper_scissors.pygi

import json
import random

with open('rps_messages.json', 'r') as file:
    MESSAGES = json.load(file)

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

def messages(message):
    return prompt(MESSAGES[message])

def convert_to_full(player):
    if player == 'r':
        return 'rock'
    if player == 'p':
        return 'paper'
    if player == 'sc':
        return 'scissors'
    if player == 'l':
        return 'lizard'
    if player == 'sp':
        return 'spock'
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
        return 'player'
    if player == computer:
        scoreboard['tie'] += 1
        return 'tie'

    scoreboard['computer'] += 1
    return 'computer'

def display_round_winner(string):
    if string == 'player':
        messages('player_wins_round')
    elif string == 'computer':
        messages('computer_wins_round')
    else:
        messages('tie')

def display_score():
    prompt(f'Player: {scoreboard["player"]}. Computer: {scoreboard["computer"]}. '
           f'Ties: {scoreboard["tie"]}.')

messages('welcome')

# Loop to continue playing
while True:
    round_count = 1
    scoreboard = {'player': 0, 'computer': 0, 'tie': 0}

    while True:
        prompt(f'--- Round {round_count} ---')
        prompt(f'Choose one: {", ".join(COMPUTER_CHOICES)}.')
        messages('input_alternative')
        choice = input().strip().lower()
        while choice not in VALID_USER_CHOICES:
            messages('invalid_choice')
            choice = input().strip().lower()
        choice = convert_to_full(choice)

        computer_choice = random.choice(COMPUTER_CHOICES)
        display_choices(choice, computer_choice)

        winner = determine_winner(choice, computer_choice)
        display_round_winner(winner)
        display_score()

        round_count += 1

        # Stop playing once any player reaches 3 points,
        # which guarantees that they win the Best of 5 match.
        if scoreboard['player'] == 3:
            messages('player_wins_match')
            break
        if scoreboard['computer'] == 3:
            messages('computer_wins_match')
            break

    messages('play_again')
    answer = input().strip().lower()
    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break

        messages('retry_play_again')
        answer = input().strip().lower()

    if answer[0] == 'n':
        messages('goodbye')
        break
