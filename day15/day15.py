file = open("day15/input.txt", "r")
lines = file.readline().split(",")

def hash(word):
    curr = 0
    for i in word:
        curr += ord(i)
        curr *= 17
        curr = curr % 256
    return curr


total = 0
for word in lines:
    total += hash(word)
print(total)