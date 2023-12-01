file = open("input1.txt", "r")
line = file.readline()

numbers = {"one":1,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0 }

sum = 0
while line != "":
    lst = [char for char in line if char.isnumeric()]
    calib = lst[0]+lst[-1]
    sum += int(calib)
    line = file.readline()

print("Calibration sum:", sum)