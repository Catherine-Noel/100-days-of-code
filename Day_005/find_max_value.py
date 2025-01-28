#Don't use max()


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = student_scores[0]

for i in student_scores:
    if i > high_score : # If this score is more then the current high score:
        high_score = i # Make current score the high score and

print(f'The highest score is {high_score}') #print result
