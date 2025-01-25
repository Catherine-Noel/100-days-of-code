print("Welcome to the tip calculator!")

bill = int(input("What was the total bill? $"))
tip_rate = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


pay_amount = float((bill * tip_rate / 100 ) + bill) / people
rounded_pay_amount = round(pay_amount,2)

print(f'Each person should pay: ${rounded_pay_amount}')

