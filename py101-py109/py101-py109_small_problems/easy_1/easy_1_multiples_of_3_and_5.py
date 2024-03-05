# easy_1_multiples_of_3_and_5.py

# Multiples of 3 and 5

# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# 1. Get integer input from user.
# 2. Determine multiples of 3 between 1 and integer.
# 3. Determine multiples of 5 between 1 and integer, dedupe.
# 4. Sum


def get_int():
    while True:
        integer = input('==> Please input an integer greater than 0. ')
        try:
            integer = int(integer)
            if integer <= 0:
                print('Input must be an integer greater than 0. Please try again.')
                continue
            return integer
        except ValueError:
            print('Input must be an integer greater than 0. Please try again.')

def multi(int):
    list = []
    for i in range(1, int + 1):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)

    return list

def compute_sum(list):
    total = 0
    for i in list:
        total += i
    return total

def multisum(int):
    list = multi(int)
    return compute_sum(list)

def main():
    user_int = get_int()
    print(multisum(user_int))


main()


# Derek Truong (other student) solution is exceptional!
# Comprehension
# def multisum(num):
#     multiples = [x for x in range(1, num+1) if x % 3 == 0 or x % 5 == 0]
#     return sum(multiples)