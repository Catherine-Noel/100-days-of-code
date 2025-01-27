import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_start = 'Pick you fighter.... Rock, Paper, or Scissors?:\n'
choice= input(' Enter R, P, or S\n').capitalize

my_pick = random.randrange(1,3)

if my_pick == 1: # Rock
    print("I pick... rock!")
elif my_pick == 2: # Paper
    print("I pick... paper!")
elif my_pick == 3: # Scissors
    print("I pick... scissors!")
else:
    print("Error!")

