file = open("day9/input.txt")

line = file.readline().split()
result = None
def get_extra(line):
    if len(set(line)) == 1 and line[0] == 0:
        return 0
    else:
        next_line = []
        for i in range(len(line)-1):
            next_line.append(line[i+1]-line[i])
        return line[-1]+get_extra(next_line)

sum = 0
while line != []:
    line = [int(x) for x in line]
    sum += get_extra(line)
    line = line = file.readline().split()

print(sum)