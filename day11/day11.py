file = open("day11/input.txt", "r")
grid = [line.strip("\n") for line in file.readlines()]
galaxies = []
x_offset = 0
y_offset = 0
y_blanks = []

new = [[] for x in range(len(grid[0]))]
for x in range(len(grid)):
    for y in range(len(grid[0])):
        new[y].append(grid[x][y])
for line in range(len(grid)):
    if len(set(new[line])) == 1:
        y_blanks.append(line)
for x in range(len(grid)):
    y_offset = 0
    if len(set(grid[x])) == 1:
        x_offset += 1
    for y in range(len(grid[0])):
        if y in y_blanks:
            y_offset += 1
        if grid[x][y] == "#":
            galaxies.append((x+x_offset, y+y_offset))

total = 0
for x in range(len(galaxies)):
    coord1 = galaxies[0]
    for coord2 in galaxies[1::]:
        total += abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1]))
    galaxies = galaxies[1::]
print(total)
