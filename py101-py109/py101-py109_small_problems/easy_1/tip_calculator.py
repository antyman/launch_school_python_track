# Tip Calculator

# Tip Calculator

# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid number.

# Inputs: bill amount, tip rate
# Outputs: Tip, Bill total amount

bill_amount = float(input('==> Please input the amount of the bill, before tax and tip. '))
tip_rate = float(input('==> How much would you like to tip? Eg. "15" if you\'d like to tip 15%. '))

tip_amount = bill_amount * (tip_rate / 100)
bill_total = bill_amount + tip_amount

print(f'==> At {tip_rate}% tip, you should tip ${tip_amount:.2f}, for a total of ${bill_total:.2f}, excluding tax.')