file = open("cards.txt", "r")

line = file.readline()[9::]
cards_count = [1 for x in range(187)]
total = 0
curr = 0
while line != "":
    wins = line[0:30:].split()
    numbers = line[32::].split()
    num_wins = 0
    for n in numbers:
        if n in wins:
            num_wins += 1
    if num_wins > 0:
        for i in range(cards_count[curr]):
            start = curr + 1
            for card in range(num_wins):
                cards_count[start] += 1
                start += 1
    line = file.readline()[9::]
    curr += 1
    print(cards_count)

print("Total score:", sum(cards_count))