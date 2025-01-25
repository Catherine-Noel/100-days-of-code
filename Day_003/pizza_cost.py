print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").capitalize()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").capitalize()
extra_cheese = input("Do you want extra cheese? Y or N: ").capitalize()
price = 0

if extra_cheese == 'Y':
    price = 1
else:
    pass
if size == 'S':
    price += 15
    if pepperoni == 'Y':
        price += 2
elif size == 'M':
    price += 20
    if pepperoni == 'Y':
        price += 3
elif size == 'L':
    price += 25
    if pepperoni == 'Y':
        price += 3
else:
    print('There was an error!')



print(price)
