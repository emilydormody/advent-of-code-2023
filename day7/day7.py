file = open("day7/input.txt", "r")
score_dict = {}
def rank_card(line):
    set_length = len(set(line[0]))
    score_dict[line[0]] = int(line[1])
    if set_length == 1:
        rank[0].append(line[0])
    elif set_length == 2:
        for card in line[0]:
            if line[0].count(card) == 4:
                rank[1].append(line[0])
                return
        rank[2].append(line[0])
    elif set_length == 3:
        for card in line[0]:
            if line[0].count(card) == 3:
                rank[3].append(line[0])
                return
        rank[4].append(line[0])
    elif set_length == 4:
        rank[5].append(line[0])
    else:
        rank[6].append(line[0])

line = file.readline().split()
rank = [[] for x in range(7)]
while line != []:
    line[0] = line[0].replace("A", "Z")
    line[0] = line[0].replace("K", "Y")
    line[0] = line[0].replace("Q", "X")
    line[0] = line[0].replace("J", "W")
    line[0] = line[0].replace("T", "V")
    rank_card(line)
    line = file.readline().split()


for c in range(len(rank)):
    rank[c] = sorted(rank[c])

print(rank)
curr = 1
total = 0
for c in range(len(rank)-1, -1, -1):
    for cards in rank[c]:
        total+= score_dict[cards]*curr
        print(total, curr, score_dict[cards])
        curr += 1
print(total)
        


