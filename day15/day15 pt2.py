file = open("day15/input.txt", "r")
lines = file.readline().split(",")

def hash(word):
    curr = 0
    for i in word:
        curr += ord(i)
        curr *= 17
        curr = curr % 256
    return curr

box_lst = [{} for x in range(256)]
for word in lines:
    if word[-2] == "=":
        code = hash(word[0:len(word)-2:])
        box_lst[code][word[0:len(word)-2:]] = word[-1]
    elif word[-1] == "-":
        code = hash(word[0:len(word)-1:])
        if word[0:len(word)-1:] in box_lst[code].keys():
            del box_lst[code][word[0:len(word)-1:]]
total = 0
for b in range(len(box_lst)):
    box = box_lst[b]
    keys = list(box.keys())
    for i in range(len(keys)):
        total += (i+1)*int(box[keys[i]])*(b+1)
print(total)