# easy_1_sum_or_product_of_consecutive_integers.py

# Sum or Product of Consecutive Integers

# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Please find Further Exploration task below the Original Program.

# --- Original Program ---

def collect_integer():
    while True:
        chosen_int = input('==> Please enter an integer greater than 0. ')

        try:
            chosen_int = int(chosen_int)
            if chosen_int <= 0:
                print('==> Input must be greater than 0.')
            else:
                return chosen_int
        except ValueError:
            print('==> Input must be an integer.')

def sum_or_product():
    while True:
        choice = input('==> Enter "s" to compute the sum, '
                       'or "p" to compute the product. ')

        if choice.lower() == "s" or choice.lower() == "p":
            return choice.lower()
        else:
            print('==> Invalid input. Please try again.')
            continue

def calc_sum(chosen_int):
    sum = 0
    for number in range(1, chosen_int + 1):
        sum += number
    return sum

def calc_product(chosen_int):
    product = 1
    for number in range(1, chosen_int + 1):
        product *= number
    return product

def main():
    ending_int = collect_integer()
    operation = sum_or_product()

    if operation == "s":
        sum_total = calc_sum(ending_int)
        print(f'The sum of the integers between 1 and '
              f'{ending_int} is {sum_total:,}.')
    else:
        product_total = calc_product(ending_int)
        print(f'The product of the integers between 1 and '
              f'{ending_int} is {product_total:,}.')

main()


# --- Further Exploration ---

# Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?



# def collect_input():
#     while True:
#         chosen_ints = input('==> Please input a list of integers separated '
#                             'by a space. For example, "1 2 3 7". ')
#         chosen_ints = chosen_ints.split(" ")
#         try:
#             list_in_integers = convert_to_int(chosen_ints)
#         except ValueError:
#             print('==> Inputs must be integers. Please try again.')
#             continue
#         return list_in_integers

# def convert_to_int(list):
#     converted_list = []
#     for item in list:
#         converted_list.append(int(item))
#     return(converted_list)

# def sum_or_product():
#     while True:
#         choice = input('==> Enter "s" to compute the sum, '
#                        'or "p" to compute the product. ')

#         if choice.lower() == "s" or choice.lower() == "p":
#             return choice.lower()
#         else:
#             print('==> Invalid input. Please try again.')

# def calc_sum(list):
#     sum = 0
#     for item in list:
#         sum += item
#     return sum

# def calc_product(list):
#     product = 1
#     for item in list:
#         product *= item
#     return product

# def main():
#     integer_list = collect_input()
#     operation = sum_or_product()

#     if operation == "s":
#         sum_total = calc_sum(integer_list)
#         print(f'The sum of the integers in list '
#               f'{integer_list} is {sum_total:,}.')
#     else:
#         product_total = calc_product(integer_list)
#         print(f'The product of the integers in list '
#               f'{integer_list} is {product_total:,}.')

# main()