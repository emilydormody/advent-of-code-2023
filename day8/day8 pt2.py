import math
file = open("day8/input.txt")

directions = file.readline().strip("\n")
direction_dict = {}
file.readline()

def traverse(curr, i):
    if i == "L":
        return direction_dict[curr][0]
    elif i == "R":
        return direction_dict[curr][1]

line = file.readline().split()
ghosts = []
while line != []:
    line[2] = line[2].strip("(").strip(",")
    line[3] = line[3].strip(")").strip(",")
    direction_dict[line[0]] = (line[2], line[3])
    if line[0].endswith("A"):
        ghosts.append(line[0])
    line = file.readline().split()

steps = [None for x in range(len(ghosts))]
for ghost in range(len(ghosts)):
    i = -1
    total = 0
    while True:
        i += 1
        if i == len(directions):
            if ghosts[ghost].endswith("Z"):
                steps[ghost] = total
                break
            i = 0
        ghosts[ghost] = traverse(ghosts[ghost], directions[i])
        total += 1

print(math.lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5]))


