
highest = 0
f = open("aoc1.txt", 'r')
#Cargo = the cargo each elve carries with them
cargo = 0
for line in f:
    if line == '\n':
        if cargo > highest:
            highest = cargo
        cargo = 0
    else:
        cargo += int(line.strip('\n'))

print(highest)
