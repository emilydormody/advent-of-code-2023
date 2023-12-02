RED = 12
GREEN = 13
BLUE = 14

file = open("games.txt", "r")

def check_round(game):
    for r in range(1,len(game)):
        game[r] = game[r].split(",")
        for cubes in game[r]:
            if cubes[-3:] == "red" and int(cubes[0:3].strip()) > RED:
                return False
            elif cubes[-5:] == "green" and int(cubes[0:3].strip()) > GREEN:
                return False
            elif cubes[-4:] == "blue" and int(cubes[0:3].strip()) > BLUE:
                return False
    return True

sum = 0
for i in range(100):
    game = file.readline().strip()
    game = "|".join(game.split(";"))
    game = "|".join(game.split(":"))

    game = game.split("|")
    if check_round(game):
        sum += i+1
print(sum)


    
