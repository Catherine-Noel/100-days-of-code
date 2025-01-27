import random

bet = input('Lets play a game... would you like heads or tails?\n').capitalize #get user input
coin_flip = random.random()
tailsmoney = 100

if coin_flip > 0.5:  
    print('Coin landed on Heads!\n')
    if bet  == 'HEADS':
        print('You Win!\n')
    else:
        print('You lose!\n')
else:
    print('Coin landed on Tails!\n')
    if bet   == 'TAILS':
        print('You Win!\n')
    else:
        print('You lose!\n')


