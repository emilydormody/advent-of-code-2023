file = open("day8/input.txt")

directions = file.readline()
direction_dict = {}
file.readline()

def traverse(curr, i):
    if i == "L":
        return direction_dict[curr][0]
    elif i == "R":
        return direction_dict[curr][1]

line = file.readline().split()
while line != []:
    line[2] = line[2].strip("(").strip(",")
    line[3] = line[3].strip(")").strip(",")
    direction_dict[line[0]] = (line[2], line[3])
    line = file.readline().split()


steps = 0
curr = "AAA"
i = 0
while True:
    if i == len(directions)-1:
        i = 0
    curr = traverse(curr, directions[i])
    steps += 1
    i += 1
    if curr == "ZZZ":
        break

print(steps)

