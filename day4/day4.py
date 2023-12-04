file = open("cards.txt", "r")

line = file.readline()[9::]

total = 0
while line != "":
    wins = line[0:30:].split()
    numbers = line[32::].split()
    print(wins)
    num_wins = 0
    for n in numbers:
        if n in wins:
            num_wins += 1
    if num_wins > 0:
        total += 2**(num_wins-1)
    line = file.readline()[9::]

print("Total score:", total)