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

game_states = ['Rock', 'Paper', 'Scissors']
player_choice = input('Pick you fighter.... Rock, Paper, or Scissors?:\n')


random_pick = random.choice(game_states) #Rock = 0, Paper = 1, Scissors = 2

if player_choice == random_pick:
    print(f'We both picked {random_pick}.... It was a tie!')

elif player_choice == "Rock": #Player picked Rock
    if random_pick == "Paper": #Paper covers Rock
        print(f'I picked Paper\n{paper}\nI Win!')
    elif random_pick == "Scissors":#Rock breaks Scissors
        print(f'I picked Scissors\n{scissors}\nYou Win!')

elif player_choice == "Scissors": #Player picked Scissors
    if random_pick == "Paper": #Scissors cut paper
        print(f'I picked Paper\n{paper}\nYou Win!') 
    elif random_pick == "Rock":#Rock breaks Scissors
        print(f'I picked Rock\n{rock}\nI Win!')

elif player_choice == "Paper": #Player picked Paper
    if random_pick == "Rock":  #Paper covers Rock
        print(f'I picked Rock\n{rock}\nYou Win!')
    elif random_pick == "Scissors":  #Scissors cut paper
        print(f'I picked Scissors\n{scissors}\nI Win!')

