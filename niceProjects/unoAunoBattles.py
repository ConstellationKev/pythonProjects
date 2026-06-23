from random import randint
import os
from time import sleep

defend_hp = 0
damage = 0
energy1 = randint(1, 40)
energy2 = randint(1, 40)

health1 = randint(1, 150)
health2 = randint(1, 150)

# slowly prints letters from text
# Thanks to a friend (I can't find his replit account :( ) for the idea, it is very useful! 
# btw "tp" means typewriter_print (i do not want to type those long words out)
def tp(text, interval):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(interval)
    print("\n")

def defend(defend_hp, energy):
    if energy >= 3:
        defend_hp = randint(10, 15)
        print(f"\nYou defended! PLUS {defend_hp} HEALTH")
        energy -= 3
        return defend_hp, energy
    else:
        print("\nYou don't have enough energy.")
        return defend_hp, energy


def sword_slash(damage, energy):
    if energy >= 5:
        print("\nYou used sword slash!")
        damage = 15
        energy -= 5
        return damage, energy
    else:
        print("\nYou don't have enough energy.")
        return damage, energy


def sword_poke(damage):
    print("\nYou used sword poke!")
    damage = 2
    return damage


def super_slash(damage, energy):
    if energy >= 10:
        print("\nYou used super slash!")
        damage = 32
        energy -= 10
        return damage, energy
    else:
        print("\nYou don't have enough energy.")
        return damage, energy

def resign(player, resign_win):
    print(f"\nPlayer {player} has resigned from the game.")
    print(f"\nPlayer {resign_win} won the battle!")
    exit("Game Over")

tp("Welcome to the Uno A Uno Battles!!!\n", 0.05)
sleep(1)
tp("This is a two player game where the two players fight in an imaginary arena. Each player has abilities to fight the other\n", 0.07)
sleep(2)
tp("HOWEVER\n", 0.1)
sleep(1)
tp("This is a BIG however\n", 0.07)
sleep(2)
tp("The health and energy of each player is randomized :)", 0.05)
tp("One player may have 1 health and 40 energy while the other can have 150 health and 1 energy :)\n", 0.06)
sleep(2)
print("--------------------------")
print("Choose who is player 1 and who is player 2 between you and your friend")
sleep(1)
while True:
    nxt = input("Press enter once you are done choosing")
    if nxt == "":
        break
    else:
        print("Please press only enter please")
tp("Enjoy ;)", 0.1)

while True: 
    print("-----------------------------------------------------")

    print(f"\n\nPlayer 1 has {health1} health and {energy1} energy")

    print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")

    attack = input("""
\nPlayer 1, what attack do you want to do?

(1) SWORD SLASH (15 damage) (5 energy) 
(2) SWORD POKE (2 damage) (0 energy) 
(3) SUPER SLASH (32 damage) (10 energy) 
(4) DEFEND (Heals random amount of health) (3 energy)
(5) You can also resign  
""").lower().rstrip()
    if attack == "1":
        damage, energy1 = sword_slash(damage, energy1)
        health2 -= damage
        print(f"\n\nPlayer 1 has {health1} health and {energy1} energy")
    elif attack == "2":
        damage = sword_poke(damage)
        health2 -= damage
        print(f"\n\nPlayer 1 has {health1} health and {energy1} energy")
    elif attack == "3":
        damage, energy1 = super_slash(damage, energy1)
        health2 -= damage
        print(f"\n\nPlayer 1 has {health1} health and {energy1} energy")
    elif attack == "4":
        defend_hp, energy1 = defend(defend_hp, energy1)
        health1 += defend_hp
        print(f"\n\nPlayer 1 has {health1} health and {energy1} energy")
    elif attack == "5":
        player = "1"
        resign_win = "2"
        resign(player, resign_win)
    else:
        print("You gave an invalid answer")

    if health2 <= 0:
        print("Player 2 died!")
        print("Player 1 WON!!!")
        exit("Game Over")


    print("-----------------------------------------------------")


    print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")

    attack = input("""
\nPlayer 2, what attack do you want to do? 
(1) SWORD SLASH (15 damage) (5 energy) 
(2) SWORD POKE (2 damage) (0 energy) 
(3) SUPER SLASH (32 damage) (10 energy) 
(4) DEFEND (Heals random amount of health) (3 energy)
(5) You can also resign
""").lower().rstrip()
    if attack == "1":
        damage, energy2 = sword_slash(damage, energy2)
        health1 -= damage
        print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")
    elif attack == "2":
        damage = sword_poke(damage)
        health1 -= damage
        print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")
    elif attack == "3":
        damage, energy2 = super_slash(damage, energy2)
        health1 -= damage
        print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")
    elif attack == "4":
        defend_hp, energy2 = defend(defend_hp, energy2)
        health2 += defend_hp
        print(f"\n\nPlayer 2 has {health2} health and {energy2} energy")
    elif attack == "5":
        player = "2"
        resign_win = "1"
        resign(player, resign_win)
    else:
        print("You gave an invalid answer")

    if health1 <= 0:
        print("Player 1 died!\n")
        print("Player 2 WON!!!")
        exit("Game Over")

    sleep(3)
    os.system("clear")