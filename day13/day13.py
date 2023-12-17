file = open("day13/day13.txt", "r")
line = file.readline().strip("\n")

def check_horizontal(lst, y=1):
    for i in range(0,len(lst)-1):
        if lst[i] == lst[i+1]:
            for x in range(len(lst)):
                if i-x < 0 or i+1+x >= len(lst):
                    return (i+1)*y
                elif lst[i-x] != lst[i+1+x]:
                    break
    return -1
            

total = 0
while line != "":
    block = []
    while line != "":
        block.append(line)
        line = file.readline().strip("\n")
    h = check_horizontal(block, y=100)
    if h > 0:
        total += h
        print(total, end=" ")
    new = [[] for x in range(len(block[0]))]
    for x in range(len(block)):
        for y in range(len(block[0])):
            new[y].append(block[x][y])
    h = check_horizontal(new)
    if h > 0:
        total += h
        print(total, end=" ")

    line = file.readline().strip("\n")

print(total)