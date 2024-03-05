# easy_1_how_big_is_the_room.py

# How big is the room?

# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# Further Exploration: Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

def main():
    print('==> Welcome to the room size calculator.')
    measurement = measurement_type()
    length = room_length()
    width = room_width()
    if measurement == "m":
        square_meters = round(length * width, 2)
        square_feet = round(square_meters * 10.7639, 2)
        print(f'==> The room is {square_meters:,} square meters, or {square_feet:,} square feet. ')
    elif measurement == "f":
        square_feet = round(length * width, 2)
        square_meters = round(square_feet / 10.7639, 2)
        print(f'==> The room is {square_feet:,} square feet, or {square_meters:,} square meters. ')

def measurement_type():
    while True:
        choice = input('==> Would you like to work with meters (m) or feet (f)? ')
        if choice.lower() == "m" or choice.lower() == "f":
            return choice.lower()
        else:
            print('==> Invalid input. Please try again.')

def room_length():
    while True:
        length_input = input('==> Please input the length of the room in meters. ')
        try:
            length_input = float(length_input)
            if length_input <= 0:
                print('==> Your input must be a positive number. Please try again.')
                continue
        except ValueError:
            print('==> Invalid input. Please try again.')
            continue
        else:
            return length_input

def room_width():
    while True:
        width_input = input('==> Please input the width of the room in meters. ')
        try:
            width_input = float(width_input)
            if width_input <= 0:
                print('==> Your input must be a positive number.')
                continue
        except ValueError:
            print('==> Your input must be a positive number. ')
            continue
        else:
            if width_input <= 0:
                print('==> Please make sure your input is positive. ')
                continue
            return width_input

main()