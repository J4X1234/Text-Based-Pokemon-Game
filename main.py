class Pokemon:
    def __init__(self, name, type, hp, atk, defense, spd, movesList):
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
        txt += "Defense: " + str(self.defense) + "\n"
        txt += "Speed: " + str(self.speed) + "\n"
        txt += "Is Asleep: " + str(self.isAsleep) + "\n"
        txt += "Is Burned: " + str(self.isBurned) + "\n"
        txt += "Is Poisoned: " + str(self.isPoisoned) + "\n"
        return txt

    def displayStatus(self):
        txt = ""
        txt += f"Name: {self.name}\n"
        txt += f"HP: {self.currentHp}/{self.maxHp}\n"
        if self.isAsleep: txt += "asleep\n"
        if self.isBurned: txt += "burned\n"
        if self.isPoisoned: txt += "poisoned\n"
        return txt


class Move:
    def __init__(self, name, type, acc, power, special_action):
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
        return txt


AllPokemon = []
AllMoves = []
pokemon1 = None
pokemon2 = None


def loadPokemonFile():
    with open("pokemon.txt", "r") as infile:
        lines = infile.read().strip().split("\n")
        for line in lines:
            values = line.split()
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


def loadDefaultMoves():
    # Simplified version with hardcoded data for now
    AllMoves.extend([
        Move("tackle", "normal", 100, 40, "none"),
        Move("tail-whip", "normal", 100, 0, "lowers defense"),
        Move("growl", "normal", 100, 0, "lowers attack"),
        Move("scratch", "normal", 100, 40, "none"),
        Move("ember", "fire", 100, 40, "burn"),
        Move("vine-whip", "grass", 100, 45, "none"),
        Move("absorb", "grass", 100, 20, "heal half damage"),
        Move("hypnosis", "psychic", 60, 0, "sleep"),
        Move("water-gun", "water", 100, 40, "none"),
        Move("leer", "normal", 100, 0, "lowers defense"),
        Move("poison-sting", "poison", 100, 15, "poison")
    ])


def getMove(moveName):
    for m in AllMoves:
        if m.name == moveName:
            return m
    print(f"Move '{moveName}' not found.")
    return None


def choose2Pokemon():
    global pokemon1, pokemon2
    for i in range(len(AllPokemon)):
        p = AllPokemon[i]
        print(i, "-", p.name)
    choice1 = int(input("Choose the first Pokémon (enter the index): "))
    pokemon1 = AllPokemon[choice1]
    choice2 = int(input("Choose the second Pokémon (enter the index): "))
    pokemon2 = AllPokemon[choice2]


def chooseAttack(attacker):
    print(f"\nEnter a move for {attacker.name} to perform (enter the index):")
    for i in range(len(attacker.movesList)):
        print(i, "-", attacker.movesList[i])
    choice = int(input(": "))
    moveName = attacker.movesList[choice]
    move = getMove(moveName)
    return move


def attack(attacker, target, move):
    if move is None:
        print(f"{attacker.name}'s attack failed.")
        return

    print(f"\n{attacker.name} used {move.name}!")
    damage = move.power  # Very basic damage system
    target.currentHp -= damage
    if target.currentHp < 0:
        target.currentHp = 0
    print(target.displayStatus())


def main():
    loadPokemonFile()
    loadDefaultMoves()
    choose2Pokemon()

    print("\nStarting Battle!\n")
    print(pokemon1.displayStatus())
    print(pokemon2.displayStatus())

    while pokemon1.currentHp > 0 and pokemon2.currentHp > 0:
        move1 = chooseAttack(pokemon1)
        attack(pokemon1, pokemon2, move1)
        if pokemon2.currentHp <= 0:
            print(f"{pokemon2.name} has fainted!")
            break

        move2 = chooseAttack(pokemon2)
        attack(pokemon2, pokemon1, move2)
        if pokemon1.currentHp <= 0:
            print(f"{pokemon1.name} has fainted!")
            break

    print("\nBattle over!")


if __name__ == "__main__":
    main()
