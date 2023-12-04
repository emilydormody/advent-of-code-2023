file = open("cards.txt", "r")

line = file.readline()[9::]

total = 0
while line != "":
    wins = line[0:30:].split()
    numbers = line[32::].split()
    card_length = len(wins)+len(numbers)
    num_wins = 0
    if len(set(wins+numbers)) < card_length:
        num_wins = card_length - len(set(wins+numbers))
    if num_wins > 0:
        total += 2**(num_wins-1)
    line = file.readline()[9::]

print("Total score:", total)