file = open("day6/input.txt", "r")
times = file.readline().replace(" ","")[5::]
records =  file.readline().replace(" ","")[9::]

def check_win(button, race_time=int(times), record=int(records)):
    distance = (race_time - button)*button
    return distance > record

def reduce_range(button_range):
    curr = button_range[0]
    while not check_win(curr):
        curr += 10
    button_range[0] = curr-10
    button_range[1] = int(times)-button_range[0]+20 #to make sure max is included
    return button_range

r = reduce_range([1, int(times)])
for race in range(r[0],r[1]):
    if not check_win(race):
        r[0] += 1
    else:
        break
for race in range(r[1], r[0], -1):
    if not check_win(race):
        r[1] -= 1
    else:
        break
print(r[1]-r[0]+1)
