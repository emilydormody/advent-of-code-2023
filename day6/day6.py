file = open("day6/input.txt", "r")
times = file.readline().split()[1::]
records = file.readline().split()[1::]

def check_win(button, race_time, record):
    distance = (race_time - button)*button
    return distance > record


total = 1
for t in range(len(times)):
    ways = 0
    for race in range(1,int(times[t])):
        if check_win(race, int(times[t]), int(records[t])):
            ways += 1
    total *= ways

print(total)