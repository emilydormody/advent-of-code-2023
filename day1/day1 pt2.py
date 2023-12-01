file = open("input1.txt", "r")
line = file.readline()

numbers = {"one":1,"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "zero":0 }

def has_digit(char):
    if char > 0 and char < len(line)-1:
        digit = line[char-1]+line[char]+line[char+1]
        if digit in numbers.keys():
            return numbers[digit]
    if char > 0 and char < len(line) - 2:
        digit = line[char-1]+line[char]+line[char+1]+line[char+2]
        if digit in numbers.keys():
            return numbers[digit]
    if char > 1 and char < len(line) - 2:
        digit = line[char-2]+line[char-1]+line[char]+line[char+1]+line[char+2]
        if digit in numbers.keys():
            return numbers[digit]
    return -1


sum = 0
while line != "":
    lst = []
    for char in range(len(line)):
        if line[char].isnumeric():
            lst.append(line[char])
        if has_digit(char) >= 0:
            lst.append(has_digit(char))
    calib = str(lst[0])+str(lst[-1])
    print(line, calib)
    sum += int(calib)
    line = file.readline()

print("Calibration sum:", sum)