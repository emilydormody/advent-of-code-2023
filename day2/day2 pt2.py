
file = open("games.txt", "r")

def check_round(game):
    r = 0
    g = 0
    b = 0
    for rd in range(1,len(game)):
        game[rd] = game[rd].split(",")
        for cubes in game[rd]:
            if cubes[-3:] == "red":
                if int(cubes[0:3].strip()) > r:
                       r = int(cubes[0:3].strip())
            elif cubes[-5:] == "green":
                if int(cubes[0:3].strip()) > g:
                       g = int(cubes[0:3].strip())
            elif cubes[-4:] == "blue":
                 if int(cubes[0:3].strip()) > b:
                       b = int(cubes[0:3].strip())
    return r*b*g

sum = 0
for i in range(100):
    game = file.readline().strip()
    game = "|".join(game.split(";"))
    game = "|".join(game.split(":"))

    game = game.split("|")
    sum += check_round(game)
print(sum)


    
