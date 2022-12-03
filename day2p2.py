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
        score += loss
        if enemy == 'A':
            score += scissors
        elif enemy == 'C':
            score += paper
        elif enemy == 'B':
            score += rock
    elif player == 'Y':
        score += draw
        if enemy == 'A':
            score += rock
        elif enemy == 'B':
            score += paper
        elif enemy == 'C':
            score += scissors
    elif player == 'Z':
        score += win
        if enemy == 'B':
            score += scissors
        elif enemy == 'C':
            score += rock
        elif enemy == 'A':
            score += paper
        
print(score)
    
