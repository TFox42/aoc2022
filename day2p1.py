# declare the worth of every factor per match

rock = 1
paper = 2
scissors = 3

win = 6
loss = 0
draw = 3

f = open("aoc.txt", 'r')

score = 0

for line in f:
    match = line.strip('\n').split(" ")
    enemy = match[0]
    player = match[1]
    
    if player ==  'X':
        score += rock
        if enemy == 'A':
            score += draw
        elif enemy == 'C':
            score += win
    elif player == 'Y':
        score += paper
        if enemy == 'A':
            score += win
        elif enemy == 'B':
            score += draw
    elif player == 'Z':
        score += scissors
        if enemy == 'B':
            score += win
        elif enemy == 'C':
            score += draw
        
print(score)
    
