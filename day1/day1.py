file = open("input1.txt", "r")
line = file.readline()

sum = 0
while line != "":
    lst = [char for char in line if char.isnumeric()]
    calib = lst[0]+lst[-1]
    sum += int(calib)
    line = file.readline()

print("Calibration sum:", sum)