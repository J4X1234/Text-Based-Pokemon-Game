class Pokemon:
    def __init__(self,name,type,hp,atk,defense,spd,movesList):
        self.name = name
        self.type = type
        self.maxHp = int(hp)
        self.currentHp = int(hp)
        self.attack = int(atk)
        self.defense = int(defense)
        self.speed = int(spd)
        self.movesList = movesList
        self.isAsleep = False
        self.isBurned = False
        self.isPoisoned = False

    def displayInfo(self):
        txt = ""
        txt += "Name: " + self.name + "\n"
        txt += "Type: " + self.type + "\n"
        txt += "Max HP: " + str(self.maxHp) + "\n"
        txt += "Current HP: " + str(self.currentHp) + "\n"
        txt += "Attack: " + str(self.attack) + "\n"
        txt += "Defense:" + str(self.defense) + "\n"
        txt += "Speed: " + str(self.speed) + "\n"
        txt += "Is Asleep: " + str(self. isAsleep) + "\n"
        txt += "Is Burned: " + str(self. isBurned) + "\n"
        txt += "Is Poisoned: " + str(self. isPoisoned) + "\n"
        return txt

    def displayStatus(self):
        txt = ""
        txt += f"Name: {self.name}{"\n"}"
        txt += f"HP: {str(self.currentHp)}/{str(self.maxHp)}{"\n"}"
        if self.isAsleep:txt += "asleep\n"
        if self.isBurned:txt += "burned\n"
        if self.isPoisoned:txt += "Poisened\n"
        return txt

class Move:
    def __init__(self,name,type,acc,power,special_action):
        self.name = name
        self.type = type
        self.accuracy = int(acc)
        self.power = int(power)
        self.specialAction = special_action

    def displayInfo(self):
        txt = ""
        txt += "Name: " + self.name + "\n"
        txt += "Type: " + self.type + "\n"
        txt += "Accuracy: " + str(self.accuracy) + "\n"
        txt += "Power: " + str(self.power) + "\n"
        txt += "Special Action: " + self.specialAction + "\n"

AllPokemon = []
AllMoves = []
pokemon1 = None
pokemon2 = None

def loadPokemonFile():
    infile = open("pokemon.txt", "r")
    txt = infile.read()
    lines = txt.split("\n")
    for line in lines:
        values = line.split(" ")
        name = values[0]
        type = values[1]
        maxHp = values[2]
        attack = values[3]
        defense = values[4]
        speed = values[5]
        move1 = values[6]
        move2 = values[7]
        
        movesList = [move1, move2]
        p = Pokemon(name, type, maxHp, attack, defense, speed, movesList)
        AllPokemon.append(p)

def getMove(moveName):
    for m in AllMoves:
        if m.name == moveName:
            return m

def choose2Pokemon():
    global pokemon1
    global pokemon2
    for i in range(len(AllPokemon)):
        p = AllPokemon[i]
        print(i,p.name)

    choice1 = int(input("Choose the first pokemon (enter the index): "))
    pokemon1 = AllPokemon[choice1]
    choice2 = int(input("Choose the second pokemon (enter the index): "))
    pokemon1 = AllPokemon[choice2]

def chooseAttack(attacker):
    print("Enter a move for ",attacker," to perform (enter the index)")
    for i in range(len(attacker.movesList)):
        print(i, attacker.movesList[i])
    choice = int(input(': '))
    moveName = attacker.movesList[choice]
    move = getMove(moveName)
    return move

def attack(attacker, target, move):
    target.currentHp -= 5
    if target.currentHp < 0:
        target.currentHp = 0
    print(attacker,' used ',move.name)