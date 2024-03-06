# Floating Point Arithmetic

# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

first = float(input('==> Enter the first number: '))
second = float(input('==> Enter the second number. '))

# print(f'==> {num1} + {num2} = {float(num1) + float(num2)}')
# print(f'==> {num1} - {num2} = {float(num1) - float(num2)}')
# print(f'==> {num1} * {num2} = {float(num1) * float(num2)}')
# print(f'==> {num1} / {num2} = {float(num1) / float(num2)}')
# print(f'==> {num1} // {num2} = {float(num1) // float(num2)}')
# print(f'==> {num1} % {num2} = {float(num1) % float(num2)}')
# print(f'==> {num1} ** {num2} = {float(num1) ** float(num2)}')

def calculate(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '//':
            return num1 // num2
        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f'{first} {operator} {second}'
    result = calculate(first, second, operator)
    print(f'==> {operation} = {result}')