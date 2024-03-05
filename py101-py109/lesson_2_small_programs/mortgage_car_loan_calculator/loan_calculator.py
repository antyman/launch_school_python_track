# Required information:
# 1. Loan amount
# 2. Annual percentage rate (APR)
# 3. Loan duration (years)
# With above information, calculate:
# --- monthly interest rate ---
# --- loan duration in months ---
# calculation formula: m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount (from user input)
# j = monthly interest rate (converted from
# n = loan duration in months


# Pseudocode
# Request loan amount from user. Later step, deal with formatting variations.
# Request APR from user. Later step, deal with formatting variations.
# Request loan duration from user.

def prompt(message):
    print(f'==> {message}')

def input_error(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False


prompt('Welcome to the mortgage/car loan calculator!')

# Collect loan amount information and error check.
prompt('Please provide the loan amount (eg. 100000). ')
loan_amount = input()

while input_error(loan_amount):
    prompt("Must enter a positive number. ")
    loan_amount = input()

# Collect APR information and error check.
prompt(('Please provide the annual percentage rate (APR). '
        'For example, input "5" for 5% APR, "4.5" for 4.5% APR. '))
apr = input()

while input_error(apr):
    prompt("Must enter a positive number. ")
    apr = input()

# Collect duration in years and error check.
prompt('Please provide the duration of your loan in years. ')
duration_years = input()

while input_error(duration_years):
    prompt(" Must enter a positive number. ")
    duration_years = input()

monthly_int_rate = float(apr) / 12 / 100
duration_months = float(duration_years) * 12
loan_amount = float(loan_amount)

# Checking values

monthly_payment = loan_amount * (monthly_int_rate / (1 - (1 + monthly_int_rate) ** (duration_months * -1)))

print(f'Your monthly payment: ${monthly_payment:,.2f}')
