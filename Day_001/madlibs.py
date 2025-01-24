import random


plural_noun =  input('Give me a plural noun! Examples: balloons, mountains, chairs, pencils, clouds, ducks, robots, books, stars\n')
noun =  input('Give me a noun! Examples: castle, umbrella, backpack, rainbow, guitar, pancake, spaceship, trophy, mirror\n')
food = input('What is your favorite food? Examples: pizza, tacos, ice cream, popcorn, spaghetti, pickles, chocolate, apples, cake\n')
animal = input('What is your favorite animal? Examples: tiger, elephant, penguin, dolphin, lizard, kangaroo, flamingo, monkey, shark\n')
number = input('What is your favorite number? Examples: 3, 10, 42, 7, 100, 5, 13, 1, 23\n')
color = input('What is your favorite color? Examples: red, purple, neon green, glittery gold, navy blue, turquoise, black, rainbow \n')
emotion = input('Give me an emotion! Examples: excited, scared, happy, frustrated, curious, nervous, surprised, silly, thrilled\n')


story_number =  random.randrange(1,3)

print('Welcome to my madlibs story creator!  Simply answer the prompts and I will tell you a story!')

if story_number == 1:
    print(f'The Robot Factory\nIn the factory, I saw {plural_noun} coming out of a {color} {noun}. The robots ate {food} and looked like a {animal}. After {number} tests, I felt {emotion} about the invention.')
elif story_number == 2:
    print(f'The Great Escape\nI was eating {food} near a {color} (noun) when I saw a group of {plural_noun} running toward me. They were being chased by a {animal}! It took me {number} minutes to hide behind a tree, feeling (emotion) the whole time.')
elif story_number == 3:
    print(f'A Day of Chaos\nOut of nowhere, a {animal} appeared, holding a {color} (noun) in its mouth. It ran past a pile of {plural_noun} and snatched my {food}! It took {number} tries to catch it, and by the end, I felt completely (emotion).')
else:
    print('oh no things are not right... ')
