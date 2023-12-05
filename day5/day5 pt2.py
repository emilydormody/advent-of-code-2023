file = open("input.txt", "r")
seeds = file.readline().split()[1::]

file.readline()

def fill_map(lst):
    print(file.readline())
    line = file.readline().split()
    while line != []:
        lst.append([int(line[0]), int(line[1]), int(line[2])])
        line = file.readline().split()
    print(lst)
    return lst

def check_location(loc):
    for i in range(0, len(seeds), 2):
        if int(seeds[i]) <= loc < int(seeds[i])+int(seeds[i+1]):
            return True
    return False

seed_soil = fill_map([])
soil_fertilizer = fill_map([])
fertilizer_water = fill_map([])
water_light = fill_map([])
light_temp = fill_map([])
temp_humid = fill_map([])
humid_location = fill_map([])

minimum = []
for location in range(0,199602917): # previous solution
    curr = location
    for d in [humid_location, temp_humid,light_temp,water_light,fertilizer_water,soil_fertilizer, seed_soil]:
        for mapping in d:
            if mapping[0] <= curr < mapping[0]+mapping[2]:
                curr = mapping[1] + (curr-mapping[0])
                break
    if check_location(curr, seeds):
        print(location)
        break

