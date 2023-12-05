file = open("day5/input.txt", "r")
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

seed_soil = fill_map([])
soil_fertilizer = fill_map([])
fertilizer_water = fill_map([])
water_light = fill_map([])
light_temp = fill_map([])
temp_humid = fill_map([])
humid_location = fill_map([])

minimum = []
for seed in seeds:
    curr = int(seed)
    for d in [seed_soil, soil_fertilizer, fertilizer_water,water_light,light_temp,temp_humid,humid_location]:
        for mapping in d:
            if mapping[1] <= curr < mapping[1]+mapping[2]:
                curr = mapping[0] + (curr-mapping[1])
                break
    minimum.append(curr)
print(min(minimum))

