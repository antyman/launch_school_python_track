# easy_1_even_numbers.py

# Even Numbers

# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

for number in range(1, 100):
    print(number) if number % 2 == 0 else None

# Bonus answer
for number in range(2, 100, 2):
    print(number)