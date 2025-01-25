print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('Would you like to go left or right?\n')
answer = input('     Please Enter Your Response: L or R     :\n').capitalize()
if answer == 'L':
    print('You find yourself on a beach...swim it wait?\n')
    answer = input('     Please Enter Your Response: S or W\n').capitalize()
    if answer == 'W':
        print('As the sunsets you see a glimmer in the distance drawing your eye to three doors...a red door, a yellow door, and a blue door. Which door do you take?\n ')
        answer = input('     Please Enter Your Response: R, Y or B     :\n').capitalize()
        if answer == 'R':
            print('Flames engulfed you when you opened the door ... game over!\n')
        if answer == 'B':
           print('Beasts flooded the island and tore you apart ... game over!\n')
        if answer == 'Y':
            print('You found the gold!\n')
    else:
        print('You discovered a new species of carnivorous fish by becoming dinner ... game over!\n')
else:
    print('You found a hole... and unfortunately fell in... game over!\n')