# easy_1_odd_numbers.py

# Odd Numbers

# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Original + Bonus Questions
# for i in range(1, 100, 2):
#     print(i)

# Further Exploration:
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.
while True:
    try:
        start_num = int(input('==> Please input an integer to start with. '))
    except ValueError:
        print('==> Input must be an integer. Please try again. ')
        continue
    else:
        break

while True:
    try:
        end_num = int(input('==> Please input an integer to end with that is larger than the starting number. '))
    except ValueError:
        print('==> Input must be an integer. Please try again. ')
        continue
    else:
        if start_num >= end_num:
            print('==> Ending integer must be greater than the starting integer. ')
            continue
        break

for number in range(start_num, end_num + 1):
    if number % 2 == 1:
        print(number)
