
highest1 = 0
highest2 = 0
highest3 = 0
f = open("aoc1.txt", 'r')
#Cargo = the cargo each elve carries with them
cargo = 0
for line in f:
    if line == '\n':
        if cargo > highest1:
            highest3 = highest2
            highest2 = highest1
            highest1 = cargo
        elif cargo > highest2:
            highest3 = highest2
            highest2 = cargo
        elif cargo > highest3:
            highest3 = cargo

        cargo = 0
    else:
        cargo += int(line.strip('\n'))

print(highest1+highest2+highest3)
