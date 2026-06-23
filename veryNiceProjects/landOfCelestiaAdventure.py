from random import randint, choice
from time import sleep
import sys


# slowly prints letters from text
# Thanks to a friend (I can't find his replit account :( ) for the idea, it is very useful! 
def typewriter_print(text, interval):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(interval)
    print("\n")


divider = "----------------------------------------"
typewriter_print("Welcome to the Land of Celestiaterra Adventure Game!", 0.08)
print(divider)
energy = randint(40, 45)
astrocoins = randint(20, 25)
classesingame = [
    "hunter", "archer", "bandit", "wizard", "spearman", "swordsman"
]
hunter = [
    "Rifle Shot(3 energy)(40 damage)", "Rifle Smack(0 energy)(10 damage)",
    "Rifle Headshot(15 energy)(95 damage)"
]
hunterdamage = {"Rifle Shot": 40, "Rifle Smack": 10, "Rifle Headshot": 95}
hunterenergycosts = {
    "Rifle Shot": 4,
    "Rifle Smack": 0,
    "Rifle Headshot": 15
}
hunterhealth = 210
archer = [
    "Bow and arrow(3 energy)(35 damage)", "Bow and arrow Headshot(12 energy)(75 damage)",
    "Bow Smack(0 energy)(10 damage)", "Arrow Smack(2 energy)(15 damage)",
    "Shotgun Attack(8 energy)(50 damage)", "Minigun Attack(9 energy)(60 damage)"
]
archerdamage = {
    "Bow and arrow": 35,
    "Bow and arrow Headshot": 75,
    "Bow Smack": 10,
    "Arrow Smack": 15,
    "Shotgun Attack": 50,
    "Minigun Attack": 60
}
archerenergycosts = {
    "Bow and arrow": 3,
    "Bow and arrow Headshot": 12,
    "Bow Smack": 0,
    "Arrow Smack": 2,
    "Shotgun Attack": 8,
    "Minigun Attack": 9
}
archerhealth = 210
bandit = ["Dagger Slash(6 energy)(40 damage)", "Boomerang Throw(9 energy)(60 damage)"]
banditdamage = {"Dagger Slash": 40, "Boomerang Throw": 60}
banditenergycosts = {"Dagger Slash": 6, "Boomerang Throw": 9}
bandithealth = 210
wizard = [
    "Staff Smack(0 energy)(10 damage)", "Water Spell(8 energy)(50 damage)",
    "Fire Spell(9 energy)(60 damage)", "Electric Spell(10 energy)(70 damage)",
    "Slam Against A Wall Spell(9 energy)(65 damage)", "Meteor Shower(15 energy)(95 damage)"
]
wizarddamage = {
    "Staff Smack": 10,
    "Water Spell": 50,
    "Fire Spell": 60,
    "Electric Spell": 70,
    "Slam Against A Wall Spell": 65,
    "Meteor Shower": 95
}
wizardenergycosts = {
    "Staff Smack": 0,
    "Water Spell": 8,
    "Fire Spell": 9,
    "Electric Spell": 10,
    "Slam Against A Wall Spell": 9,
    "Meteor Shower": 15
}
wizardhealth = 195
spearman = ["Spear Stab(7 energy)(55 damage)", "Spear Swing(6 energy)(45 damage)"]
spearmandamage = {"Spear Stab": 55, "Spear Swing": 45}
spearmanenergycosts = {"Spear Stab": 7, "Spear Swing": 6}
spearmanhealth = 210
swordsman = [
    "Sword Stab(7 energy)(50 damage)", "Sword Slash(6 energy)(45 damage)", "Sword Poke(3 energy)(20 damage)"
]
swordsmandamage = {"Sword Stab": 50, "Sword Slash": 45, "Sword Poke": 20}
swordsmanenergycosts = {"Sword Stab": 7, "Sword Slash": 6, "Sword Poke": 3}
swordsmanhealth = 205
dev = ["Ultimate Laser(1 energy)(10000000000000 damage)"]
devdamage = {"Ultimate Laser": 10000000000000}
devenergycosts = {"Ultimate Laser": 1}
devhealth = 1000000000000000000000000000000000000000
sleep(1)
print(
    f"Description: In this game there is a currency called AstroCoins. You have {astrocoins} AstroCoins right now, you can use it to trade items from traders throughout the journey. There will also be energy for battling and for different purposes. You have {energy} energy right now. In this game, you can also choose to be different characters with different abilities for battling. Cool right? Below are descriptions of the characters. (Please read carefully)")
print(divider)
sleep(2)
while True:
    idk = input("Press enter if you're done reading")
    if idk == "":
        break
    else:
        print("Invalid response, please press only 'enter'")
        continue
print(divider + "\n" + divider)
sleep(2)
print(f"""
In this game there is a HUNTER that has these abilities:
{hunter}

And this much health: [ {hunterhealth} ]
""")
print(divider)
print(f"""In this game there is an ARCHER that has these abilities:
{archer}

And this much health: [ {archerhealth} ]
""")
print(divider)
print(f"""
In this game there is a BANDIT that has these abilities:
{bandit}

And this much health: [ {bandithealth} ]
""")
print(divider)
print(f"""
In this game there is a WIZARD that has these abilities:
{wizard}

And this much health: [ {wizardhealth} ]
""")
print(divider)
print(f"""
In this game there is a SPEARMAN that has these abilities:
{spearman}

And this much health: [ {spearmanhealth} ]
""")
print(divider)
print(f"""
In this game there is a SWORDSMAN that has these abilities:
{swordsman}

And this much health: [ {swordsmanhealth} ]
""")
print(divider)
sleep(3)
while True:
    whatclass = input(
        "What character do you want to be?: "
    ).lower().rstrip()

    if whatclass == "hunter":
        print(divider)
        print(
            f"You are a {whatclass} and have {hunterhealth} health. Your attacks are {hunter}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "archer":
        print(divider)
        print(
            f"You are a {whatclass} and have {archerhealth} health. Your attacks are {archer}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "wizard":
        print(divider)
        print(
            f"You are a {whatclass} and have {wizardhealth} health. Your attacks are {wizard}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "spearman":
        print(divider)
        print(
            f"You are a {whatclass} and have {spearmanhealth} health. Your attacks are {spearman}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "bandit":
        print(divider)
        print(
            f"You are a {whatclass} and have {bandithealth} health. Your attacks are {bandit}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "swordsman":
        print(divider)
        print(
            f"You are a {whatclass} and have {swordsmanhealth} health. Your attacks are {swordsman}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    elif whatclass == "dev":
        print(divider)
        print(
            f"You are a {whatclass} and have {devhealth} health. Your attacks are {dev}."
        )
        print(f"You have {energy} energy.")
        print(divider)
        break
    else:
        print("That is not a class avaliable in this game.")
        continue

if whatclass == "hunter":
    your_health = hunterhealth
elif whatclass == "archer":
    your_health = archerhealth
elif whatclass == "wizard":
    your_health = wizardhealth
elif whatclass == "spearman":
    your_health = spearmanhealth
elif whatclass == "bandit":
    your_health = bandithealth
elif whatclass == "swordsman":
    your_health = swordsmanhealth
elif whatclass == "dev":
    your_health = devhealth


# This is the battle function where you fight an enemy, it includes you attacking or defending and the enemy fighting back.
# How to perform: energy, your_health = battle(energy, your_health)
def battle(energy, your_health):
    print(divider)
    print("Prepare to fight...")
    enemyhealth = randint(190, 210)
    print(f"You have {your_health} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You died.")
            print(divider)
            sys.exit("Game ended")
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You died.")
            print(divider)
            sys.exit("Game ended")

    return energy, your_health


# The first event that might happen
# How to perform: astrocoins, energy, your_health = event1(astrocoins, energy, your_health)
def event1(astrocoins, energy, your_health):
    sleep(3)
    typewriter_print("""


You wake up in a prison cell. Your head hurts, you don't know where you are. After a while, you slowly regain your consciousness.""",
                     0.07)
    sleep(2.5)
    typewriter_print("""
  Then you remember.""", 0.1)
    sleep(2)
    print("""
Your name is Zayden

You are in the magical world of Celestiatera, land in the skies. Something bad has happened, the Cosmic Gem had stopped working, and the thing it was imprisoning... had escaped and is causing chaos in the world. You tried to stop him but failed and got imprisoned in this cell.""")
    sleep(2)
    print(divider)
    typewriter_print("You have to get out of this cell, you try to find something to smash your way out.", 0.08)
    money_found = "no"
    while True:
        sleep(2)
        print(divider)
        whattodo = input(
            "Where do you want to look? Under your bed (b), behind your closet (c), or in your sink (s)? ").lower().rstrip()
        if whattodo == "b":
            typewriter_print("You look under your bed.", 0.1)
            sleep(2)
            print("You don't find anything but some dust and spider webs.")
            continue
        elif whattodo == "c":
            typewriter_print("You look behind your closet.", 0.1)
            sleep(2)
            print("You found a Pickaxe! You can use it to break through the stone walls!")
            break
        elif whattodo == "s":
            typewriter_print("You look in the sink.", 0.1)
            sleep(2)
            if money_found == "no":
                print("You found some AstroCoins! I don't know how they got in the sink.")
                money_found = "yes"
                astrocoins += randint(5, 10)
                print(f"You have {astrocoins} AstroCoins now.")
                sleep(1)
                print("But you still can't get out of this cell...")
                continue
            else:
                print("You see nothing but an ordinary sink...")
                continue
        else:
            print("That is not an option.")
            continue
    print("You use the pickaxe the break the walls.")
    sleep(1)
    print("CRASH!!!")
    event2(astrocoins, energy, your_health)


# The second event that might happen
# How to perform: event2(astrocoins, energy, your_health)
def event2(astrocoins, energy, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""

You slowly creep out of the hole in the wall. Woah, it is 3 layers of stone. You see a pine forest in not far away and go towards it. You wish you don't get caught by one of the evil soliders. Let's see if you are lucky or not.

""", 0.07)
    fatechooser = ["caught", "not caught"]
    sleep(1)
    while True:
        apple = input("You turn your head, and you see an apple not far from you, do you choose to go pick it up?(yes/no) ").lower().rstrip()
        if apple == "yes":
            sleep(0.5)
            print('You pick up the apple, and for some reason, it says "Chess Is Fun" carved on the side of it.')
            energy += 5
            sleep(2)
            print("You eat the apple anyways and it gives you 5 energy!")
            sleep(1.5)
            print(f"You have {energy} energy now")
            sleep(1)
            print("But, you picking up that apple gave you a bigger chance of being caught...")
            fatechooser.append("caught")
            break
        elif apple == "no":
            sleep(0.5)
            print(
                "You didn't waste your time on picking up that apple, you have a better chance of not being caught...")
            fatechooser.append("not caught")
            break
        else:
            print("You gave an invalid answer")
            continue
    sleep(2)
    print("...")
    sleep(1.5)
    fate = choice(fatechooser)
    if fate == "caught":
        typewriter_print("Oh no! You got caught by one of the guards!", 0.08)
        sleep(1)
        while True:
            choicemade = input("You you want to bribe them (b) or fight (f)? ").lower().rstrip()
            if choicemade == "b":
                print("You try to bribe the guard.")
                sleep(1)
                print("The guard takes 5 AstroCoins and lets you pass.")
                astrocoins -= 5
                print(f"You have {astrocoins} astrocoins right now.")
                break
            elif choicemade == "f":
                energy, your_health = battle(energy, your_health)
                print("You won the battle, you go further into the woods")
                break
            else:
                print("That is not an option.")
                continue
    else:
        typewriter_print("Fortunately, you did not get caught by guards, you successfully get into the woods.", 0.08)
    event3(energy, your_health, astrocoins)


# The third event that might happen
# How to perform: event3(energy, your_health)
def event3(energy, your_health, astrocoins):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    typewriter_print("""

You venture out into the woods. Not far from you, you see two signs.

""", 0.08)
    sleep(2)
    typewriter_print("You walk towards the signs", 0.09)
    sleep(3.5)
    typewriter_print("""
You see a wizard sitting on a green stone next to the signs and you notice the signs have cloth covered over them.

""", 0.07)
    sleep(2)
    print(divider)
    typewriter_print("You go and ask the wizard how to get out of the forest.", 0.08)
    sleep(2)
    print(divider)
    print("Wizard: Greetings, you want to get out of this forest right?")
    sleep(3)
    print(divider)
    print("Wizard: Okay, I have two signs here, you can only uncover one and that will give you a path.")
    sleep(3.5)
    print(divider)
    done = False
    while done == False:
        choicemade = input("Wizard: What sign do you choose to uncover?(1/2) ").rstrip()
        if choicemade == "1":
            print(divider)
            print(
                "Wizard: Okay, the first sign says: You go forward 1 mile and you will see a lake. Next to it, is a little hut, inside is a traveler. He will give you a path to fulfill your greatest desire.")
            sleep(2.5)
            typewriter_print("You go towards the travelers hut.", 0.1)
            done = True
            event4(energy, your_health, astrocoins)
        elif choicemade == "2":
            print(divider)
            print(
                "Wizard: Okay, the second sign says: Turn right and go forward half a mile and you would find a village, there are people in there who can help you")
            sleep(2.5)
            typewriter_print("You go towards the village.", 0.1)
            done = True
            villiage(energy, astrocoins, your_health)
        else:
            print("That is an invalid option")
            continue

"""
--------------------------------
_________________________________

This is the Cloud Kingdom path
_________________________________
--------------------------------
"""

# The fourth event that might happen
# How to perform: event4(energy, your_health)
def event4(energy, your_health, astrocoins):
    sleep(2)
    print(divider)
    typewriter_print("""

You are walking in the woods towards the hut

""", 0.08)
    sleep(2)
    typewriter_print("Suddenly, you see a bush tremble in front of you and a person jumps out!", 0.08)
    sleep(1.5)
    print("Person: Give me all your money now!")
    typewriter_print("Looks like it is a robber.", 0.09)
    while True:
        choicemade = input("Do you choose to try to negotiate (n) or fight (f)?  ").rstrip().lower()
        if choicemade == "n":
            sleep(1)
            print(divider)
            print("What do you want to say: ")
            while True:
                say1 = input("""
  Zayden: Why should I?! What are you doing here? (a)

  Zayden: Ha! I would like to see you try! (b)
  """).lower().rstrip()
                if say1 == "a":
                    sleep(2)
                    print(divider)
                    print(
                        "Person: I don't think you would even care, I am here to defeat the evil being of Celestiaterra! I kind of lost all my money on my way here so I can't buy stuff. Now give out all your money and get out of the way!")
                    sleep(4)
                    print(divider)
                    print(
                        "Zayden: Wait, you said you want to defeat the evil being? I'm here for that too! Hey, do you want to come with me on my journey? We help each other out?")
                    sleep(3)
                    print(divider)
                    print("Person: Really? That would be great! My name is Foliage, what about yours?")
                    sleep(2)
                    print(divider)
                    print("Zayden: I'm Zayden, nice to meet you.")
                    sleep(2)
                    print(divider)
                    typewriter_print(
                        "Zayden and Foliage continues their journey. Also, Zayden gave Foliage a sandwich to eat. :)",
                        0.07)
                    break
                elif say1 == "b":
                    sleep(2)
                    print(divider)
                    print("Person: Oh you are taunting me huh?! Well look closely here I come!")
                    energy, your_health = battle(energy, your_health)
                    sleep(2)
                    print(divider)
                    print("The person limps across the path")
                    sleep(2)
                    print(divider)
                    print("Zayden: Ha! Now you see my power!")
                    sleep(3)
                    print(divider)
                    print(
                        "Person: Ugh I was here to defeat the evil being! I got robbed so I can't buy stuff. I guess it is my fate to die here.")
                    sleep(2)
                    print(divider)
                    print(
                        "Zayden: Wait what? I'm here to defeat the evil being too! My name is Zayden do you want to travel together?")
                    sleep(2)
                    print(divider)
                    print("Person: Really? That's great!")
                    sleep(2)
                    print(divider)
                    typewriter_print(
                        "Zayden and Foliage continues their journey. Also, Zayden gave Foliage a sandwich to eat. :)",
                        0.07)
                    break
                else:
                    print("You gave an invalid answer.")
                    continue
        elif choicemade == "f":
            energy, your_health = battle(energy, your_health)
            sleep(2)
            print(divider)
            typewriter_print("The person lies on the floor.", 0.08)
            sleep(2)
            print(divider)
            print("Zayden: Who are you?! And why are here robbing people?")
            sleep(3)
            print(divider)
            print(
                "Person: My name is Foliage, I'm here to defeat the evil being! I lost my money so I can't buy stuff. I guess it is my fate to die here.")
            sleep(2)
            print(divider)
            print("Zayden: I'm here to defeat the evil being too! My name is Zayden do you want to travel together?")
            sleep(2)
            print(divider)
            print("Person: Really? That's great!")
            sleep(2)
            print(divider)
            typewriter_print(
                "Zayden and Foliage continues their journey. Also, Zayden gave Foliage a sandwich to eat. :)", 0.07)
            break
        else:
            print("That is an invaid answer")
            continue
        break
    event5(energy, astrocoins, your_health)


# The fifth event that might happen
# How to perform: event5(energy, astrocoins, your_health)
def event5(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    typewriter_print("""

Thunder cracks above your heads

You walk with Foliage a bit more but see a dark tunnel in your path.

""", 0.06)
    sleep(1.5)
    print("Foliage: This is bad, what should we do to get past?")
    sleep(1.5)
    print(divider)
    while True:
        option = input("Do you want to go into the tunnel (t) or try to go around it (a): ").lower().rstrip()
        if option == "t":
            sleep(1)
            print("""

  You and Foliage walk into the cave.

  """)
            sleep(2)
            print("Zayden: It is very dark in here.")
            sleep(1.5)
            print(divider)
            print("Foliage: Yeah.")
            sleep(2)
            print(divider)
            print("Voice: ZAYDEN...")
            sleep(1.5)
            print(divider)
            print("Zayden: WOAH WHAT WAS THAT?!")
            sleep(1.5)
            print(divider)
            print("""Cloud Guardian: I am the Guardian of the Cloud Kingdom!

  """)
            sleep(1.5)
            print(
                "Cloud Guardian: You have entered the borders of the Cloud Kingdom, turn back or you will be punished...")
            sleep(2)
            print(divider)
            print(
                "Zayden: I'm here to destroy the evil being released into the world, I will NOT turn back for the sake of Celestiaterra!")
            sleep(2)
            print(divider)
            print("Cloud Guardian: This was your choice...")
            sleep(2)
            print(divider)
            typewriter_print("BOOM!", 0.4)
            sleep(1.5)
            print(divider)
            print("Foliage: Oh no I think the tunnel is falling! Rocks are falling down!")
            sleep(1.5)
            print(divider)
            typewriter_print("RUN", 0.5)
            sleep(1.5)
            print(divider)
            actions = 5
            while actions > 0:
                rocks_fall = choice(["l", "r"])
                move = input("Quick! What do you do?! Move left (L) or Move right (R): ").rstrip().lower()
                if move == rocks_fall:
                    typewriter_print("""

  You dodged a falling rock!

  """, 0.1)
                    actions -= 1
                elif move != rocks_fall:
                    typewriter_print("""

  You didn't dodge a falling rock and gets hit.

  """, 0.1)
                    your_health -= 7
                    sleep(1)
                    if your_health <= 0:
                        your_health = 0
                        sleep(1)
                        typewriter_print("You died of the falling rocks.", 0.2)
                        sys.exit("Game ended")
                    print(f"You have {your_health} health right now")
                    actions -= 1

                if your_health <= 0:
                    your_health = 0
                    sleep(1)
                    typewriter_print("You died of the falling rocks.", 0.2)
                    sys.exit("Game ended")
            sleep(2)
            print("You got out of the cave alive. You sit next to a tree with Foliage")
            print(divider)
            sleep(1)
            print("Foliage: That was close. Wait what is that shiny thing over there?")
            sleep(2)
            print(divider)
            typewriter_print("You and Foliage go and see what that shiny thing is.", 0.08)
            sleep(2)
            print(divider)
            typewriter_print("""It is a scroll  

Next to it is a note""", 0.07)
            print(divider)
            typewriter_print("Hi, I'm that Wizard on that stone, next to the 2 signs. Remeber me?", 0.07)
            sleep(1)
            print(divider)
            typewriter_print("Every time you successfully get out of a disaster, I will send you a Reward Scroll.", 0.07)
            sleep(1)
            print(divider)
            typewriter_print("What you guys are doing will benefit Celestiaterra a lot, I will help you as much as I can.", 0.07)
            energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
            sleep(1)
            print(divider)
            typewriter_print("Thunder booms above your head. You receive your rewards and continue to the hut. You now know that the Cloud Kingdom is against you.", 0.07)
            break

        elif option == "a":
            sleep(1)
            print("""
            
You and Foliage walk a path around the cave.

""")
            sleep(2)
            print("Zayden: I see some storm clouds forming.")
            sleep(1.5)
            print(divider)
            print("Foliage: That can't be good...")
            sleep(2)
            print(divider)
            print("CRACK! ZAP!")
            sleep(1)
            print(divider)
            print("A lightning bolt zaps the ground in front of you and a gladiator with a spear appears.")
            sleep(2)
            print(divider)
            print("Gladiator: YOU SHALL NOT PASS THE BORDER OF THE CLOUD KINGDOM.")
            sleep(1.5)
            print(divider)
            print("Foliage: Yes we can, and you can't stop us!")
            sleep(1)
            energy, your_health = battle(energy, your_health)
            sleep(2)
            print(divider)
            print("The gladiator tumbles to the ground and disintegrates into bits of electricity.")
            sleep(2)
            print(divider)
            print("BOOM!")
            sleep(1)
            typewriter_print("OH NO! Dodge the lightning!", 0.09)
            sleep(1)
            for _ in range(3):
                print(divider)
                strikes = choice(["1", "2", "3", "4"])
                while True:
                    dodging = input("Where do you want to dodge!     Up (1)     Down (2)     Left (3)    Right (4)").rstrip()
                    if dodging == "1" or "2" or "3" or "4":
                        if dodging == strikes:
                            print("Oh no! You got struck by lightning! You lose 15 health.")
                            your_health -= 15
                            print(f"You have {your_health} health right now")
                            if your_health <= 0:
                                your_health = 0
                                typewriter_print("You died of lightning", 0.09)
                                sys.exit("Game Ended")
                            break
                        else:
                            print("""
                        
You didn't get hit by lightning""")
                            break
                    else:
                        print("You gave an invaid answer")
                        continue
            sleep(2)
            typewriter_print("You survived.", 0.1)
            sleep(1)
            print(divider)
            print("You sit on a stone next to Foliage.")
            sleep(2)
            print(divider)
            print("Foliage: Looks like we're in the Cloud Kingdom.")
            sleep(1.5)
            print(divider)
            print("Zayden: Yeah, wait, what is that shiny thing over there?")
            typewriter_print("You and Foliage go and see what that shiny thing is.", 0.08)
            sleep(2)
            print(divider)
            typewriter_print("""It is a scroll  

Next to it is a note""", 0.07)
            print(divider)
            typewriter_print("Hi, I'm that Wizard on that stone, next to the 2 signs. Remeber me?", 0.07)
            sleep(1)
            print(divider)
            typewriter_print("Every time you successfully get out of a disaster, I will send you a Reward Scroll.", 0.07)
            sleep(1)
            print(divider)
            typewriter_print("What you guys are doing will benefit Celestiaterra a lot, I will help you as much as I can.", 0.07)
            energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
            sleep(1)
            print(divider)
            typewriter_print("Thunder booms above your head. You receive your rewards and continue on the path. Now being more cautious.", 0.07)
            event6(energy, astrocoins, your_health)
            break

        else:
            print("That is an invalid option")
            continue
    event7(energy, astrocoins, your_health)

#The 6th event that might happen     How to perform: Simply, event6()
def event6(energy, astrocoins, your_health):
    sleep(2)
    typewriter_print("""
    
    You and Foliage come to a lake, you have to cross it to get to the hut.
    
    """, 0.08)
    sleep(1)
    typewriter_print("But, you have to find some materials to make a boat...", 0.08)
    sleep(2)
    print(divider)
    print("You have to find: Hammer, 10 Wood, 50 nails, and a big log.")
    looked_there1 = "no"
    looked_there2 = "no"
    while looked_there1 == "no" or looked_there2 == "no":
        print(divider)
        while True:
            look = input(
                "Where do you want to look: Up in a tree (1), in a rabbit hole (2), inside a tree (3), underground (4), or under a boulder (5). ").rstrip()
            if look == "1":
                print("You look up a tree...")
                sleep(2)
                print("You find nothing but a bird nest.")
                break
            elif look == "2":
                print("You look in a rabbit hole...")
                sleep(2)
                print("You see nothing but some spider webs.")
                break
            elif look == "3":
                if looked_there1 == "no":
                    print("You look inside a tree...")
                    sleep(2)
                    print("You find a big log and 10 wood!")
                    looked_there1 = "yes"
                    break
                elif looked_there1 == "yes":
                    print("You already looked here.")
                    break
            elif look == "4":
                print("You look underground...")
                sleep(2)
                print("You see nothing but drit and some worms.")
                break
            elif look == "5":
                if looked_there2 == "no":
                    print("You look under a boulder...")
                    sleep(2)
                    print("You find a hammer and 50 nails! I don't know how they got there...")
                    looked_there2 = "yes"
                    break
                elif looked_there2 == "yes":
                    print("You already looked here.")
                    break
            else:
                print("You gave an invalid answer.")
                continue
    sleep(2)
    print(divider)
    typewriter_print("You build a boat to cross the river!", 0.08)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)

#The 7th event that might happen (meeting the traveler)
#How to perform: event7(energy, astrocoins, your_health)
def event7(energy, astrocoins, your_health):
    sleep(2)
    typewriter_print("""
    
You and Foliage see a hut in the distance. You guys walk toward it.

""", 0.07)
    sleep(2)
    typewriter_print("You guys knock on the door of the hut.", 0.08)
    sleep(1.5)
    print(divider)
    print("Traveler: *opens door* Greetings, what do you guys want?")
    sleep(2)
    print(divider)
    print("Zayden: We are here to find a path to destroy the evil being.")
    sleep(1.5)
    print(divider)
    print("Traveler: Ah, heros of Cellestiaterra, come inside.")
    sleep(2)
    print(divider)
    typewriter_print("You guys go into the hut and sit down on chairs.", 0.08)
    sleep(2)
    print(divider)
    print("Traveler: So, I have a anceint scroll from a prophet: Go up a mountain, a battle awaits, a power may be destroyed, once and for all. Into fire, one shall go, or underground to restore what was not.")
    sleep(3)
    print(divider)
    print("Foliage: Thank you very much! We got to get going.")
    sleep(2)
    print(divider)
    print("Traveler: No, thank you for helping Celestiaterra. Good luck on your journey.")
    event8(energy, astrocoins, your_health)

#Eighth event that might happen
#How to perform: event8(energy, astrocoins, your_health)
def event8(energy, astrocoins, your_health):
    sleep(2)
    typewriter_print("""
    
You and Foliage come out of the hut.

""", 0.08)
    sleep(2)
    print("""
    
Foliage: Where is that mountain, I can't see it.

""")
    sleep(2)
    print("I shall show you how.")
    print(divider)
    sleep(1.5)
    print("Zayden: WHY ARE THERE VOICES JUST COMING OUT OF NOWHERE!")
    sleep(2)
    print(divider)
    typewriter_print("POOF!", 0.09)
    sleep(2)
    print("Wizard: It is I, greetings.")
    sleep(1.5)
    print(divider)
    print("Zayden: Oh it's you! Could you show us the way please?")
    sleep(2)
    print(divider)
    print("Wizard: That's what I'm here for, here is what your're supposed to do.")
    sleep(2)
    print(divider)
    print("Wizard: See that huge cloud up there?")
    sleep(1.5)
    print("        You are supposed to shoot it down with a bow made of Celestial Oak.")
    sleep(2)
    print(divider)
    print("""Wizard: Okay, I will give you that bow if you answer this question correctly:
    
""")
    sleep(2)
    while True:
        question = input(""" What did the apple you saw when you escaped the cell, say? 
        
Flutes Are Sacred (1)

Chess Is Fun (2)

Don't Eat Me (3)

Never Cut Down Trees (4)

The Cosmic Gem Is Green (5)

""").rstrip()   
        if question == "2":
            sleep(3)
            print("Wizard: Correct! Yes, I do like chess, here is the bow.")
            break
        elif question == "1" or question == "3" or question == "4" or question == "5":
            sleep(3)
            print("Wizard: I'm sorry, that is the wrong answer I will need to take 2 of your energy, but you will still get the bow.")
            your_health -= 3
            break
        else:
            print("You gave an invalid answer")
            continue
    if your_health <= 0:
        your_health = 0
        print(divider)
        print("You died, better luck next time.")
        print(divider)
        sys.exit("Game Ended")
    sleep(1.5)
    print(divider)
    print("Wizard: Now you've gottten the bow you have to shoot down the cloud.")
    sleep(1.5)
    print(divider)
    while True:
        strength = choice(["1", "2", "3"])
        draw_back = input("How long do you pull back your arrow? Strength 1 (1) Strength 2 (2) Strength 3 (3)").rstrip()
        if draw_back == "1" or draw_back == "2" or draw_back == "3":
            if draw_back == strength:
                typewriter_print("You hit the cloud! You see the mountain!", 0.08)
                break
            else:
                print("You missed your shot, try again.")
                continue
        else:
            print("You gave an invalid answer")
            continue
    sleep(1.5)
    print(divider)
    print("Wizard: Good, now the mountain is in sight, my job is done here. I will see you guys later.")
    sleep(2)
    print(divider)
    typewriter_print("The Wizard dissolves into light and dissapears.", 0.08)
    print(divider)
    sleep(1)
    print("Foliage: Good work! Now we see the mountain, let's go toward it!")
    sleep(2)
    print(divider)
    print("Zayden: Yes, let's go.")
    event9(energy, astrocoins, your_health)
        
#Ninth event that might happen
#How to perform: event9(energy, astrocoins, your_health)
def event9(energy, astrocoins, your_health):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    typewriter_print("""
    
Foliage and Zayden arrive at the bottom of the mountain with clouds surrounding it

""",0.07)
    sleep(1)
    print("Foliage: This mountain is so high and steep, how are we supposed to get up?")
    sleep(2)
    print(divider)
    print("Zayden: I know! let's use the mountain goats over there, but we have to tame them first.")
    sleep(2)
    print(divider)
    tamed = 0
    while tamed < 5:
        sleep(2)
        print(divider)
        needs = choice(["Apples", "Water", "A ride", "Wheat", "Carrots"])
        print(f"""The goat needs {needs}
        
""")
        while True:
            print(divider)
            sleep(1.5)
            taming = input("""What do you do?
            
Feed apples (1)

Give water (2)

Ride it (3)

Feed wheat (4)

Feed carrots (5)

    """).rstrip()
            if taming == "1" or taming == "2" or taming == "3" or taming == "4" or taming == "5":
                if needs == "Apples" and taming == "1":
                    print("You feed the goat apples, it likes you a bit more!")
                    tamed += 1
                    break
                elif needs == "Water" and taming == "2":
                    print("You give the goat water, it likes you a bit more!")
                    tamed += 1
                    break
                elif needs == "A ride" and taming == "3":
                    print("You give the goat a ride, it likes you a bit more!")
                    tamed += 1
                    break
                elif needs == "Wheat" and taming == "4":
                    print("You feed the goat wheat, it likes you a bit more!")
                    tamed += 1
                    break
                elif needs == "Carrots" and taming == "5":
                    print("You feed the goat carrots, it likes you a bit more!")
                    tamed += 1
                    break
                else:
                    print("You don't give what the goat wants, it dislikes you a little.")
                    tamed -= 1
                    break
            else:
                print("You gave an invalid answer.")
                continue
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    print("Zayden: Yes! We got ourselves goats, now let's get to the top of the mountain.")
    event10(energy, astrocoins, your_health)

#The 10th event that might happen, MINIBOSS TIME!!!
#How to perform: event10(energy, astrocoins, your_health)
def event10(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Foliage arrive at the top of the tall mountain, thunder CRACKS and lighting FLASHES

""", 0.07)
    sleep(1.5)
    typewriter_print("BOOM!!!", 0.05)
    sleep(1.5)
    print(divider)
    typewriter_print("A HUGE figure made up of dark clouds, lighting, and wind appear in front of them", 0.07)
    sleep(3)
    print(divider)
    print("Cloud Guardian: I am the Cloud Guardian! You shall not pass this final trial to defeat the evil being, unless you prove yourself worthy.")
    sleep(4)
    print(divider)
    print("Zayden: We will, and this is for the good of Celestiaterra!")
    sleep(3)
    print(divider)
    print("Cloud Guardian: You have great bravery, but let me remind you, if you do not defeat me, you will get locked up by the evil soldiers.")
    sleep(4)
    print("                Are you ready?")
    sleep(3)
    print("Foliage: Yes! Let's do this!")


    sleep(2)
    print(divider)
    print("Prepare to fight, MINIBOSS TIME...")
    sleep(2)
    enemyhealth = 400
    print(f"You have {your_health} health")
    sleep(1.5)
    print(divider)
    print(f"The Cloud Guardian has {enemyhealth} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        foliage_attack = randint(10, 60)
        sleep(2)
        print(divider)
        print(f"Foliage dealed {foliage_attack} damage to the Cloud Guardian!")
        enemyhealth -= foliage_attack

        if enemyhealth <= 0:
            print(divider)
            print("You and Foliage defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
            

    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)

    sleep(3.5)
    print(divider)
    print("Cloud Guardian: Seems like, you two are the chosen ones, you guys are worthy. I shall let you guys pass.")
    wizard_choose(energy, astrocoins, your_health)

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#When you uncover the 2nd sign and come to the village
#How to perform: villiage(energy, astrocoins, your_health)
def villiage(energy, astrocoins, your_health):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    typewriter_print("""
    
You go to the village

""", 0.09)
    sleep(1.5)
    typewriter_print("""
Zayden arrives at the village, there are shopping huts here and there and people walking around.

""", 0.07)
    sleep(1.5)
    typewriter_print("You see a person with a navy blue hood walking around weirdly, you go and ask him what is up.", 0.08)
    sleep(2)
    print(divider)
    while True:
        say1 = input("""What do you choose to say:
        
Hi, why are you walking around weirdly? (1)

Hey! What are you doing!? You're so weird. (2)

""").rstrip()
        if say1 == "1":
            sleep(2)
            print(divider)
            print("Ember: My name is Ember, what are you doing?")
            sleep(1.8)
            print(divider)
            while True:
                say2 = input("""What do you want to say:
                
I'm secretly going to defeat the evil being (1)

Um, I can't tell you right now. (2)

""").rstrip()
                if say2 == "1":
                    sleep(2)
                    print(divider)
                    print("Ember: Oh really? I am here to do that too, all I need is a path and guidance. ")
                    sleep(2)
                    print(divider)
                    print("Zayden: My name is Zayden, want to be a little team or something?")
                    sleep(2)
                    print(divider)
                    print("Ember: Sure! Now we only need a path and guidance.")
                    break
                elif say2 == "2":
                    sleep(2)
                    print(divider)
                    print("Ember: Oh, well, I can't help you or tell you anything then, bye.")
                    sleep(2)
                    print(divider)
                    typewriter_print("Well that didn't end well, try again.", 0.08)
                    continue
                else:
                    print("""You gave an invalid answer
                    
""")
                    continue
            break
        elif say1 == "2":
            sleep(2)
            print(divider)
            print("Person: You are so rude! Bye forever!")
            sleep(2)
            print(divider)
            typewriter_print("Well that didn't end well, try again.", 0.08)
            continue
        else:
            print("""You gave an invalid answer
            
""")
            continue

    sleep(2)
    done = "no"
    while done == "no":
        walk_where = input("""
        
You hear that there is a librarian and a blacksmith that might have information, do you want to go find the librarian (l) or the blacksmith (b) ?""").lower().rstrip()
        if walk_where == "l":
            sleep(1)
            print(divider)
            typewriter_print("""
            
You go and find the librarian

""", 0.08)
            sleep(2)
            typewriter_print("You and Ember go inside the library.", 0.08)
            sleep(1.5)
            print(divider)
            print("Librarian: Hello! Welcome to the Villiage Library!")
            sleep(2)
            print(divider)
            print("Ember: Librarian, do you have any books about...")
            sleep(2)
            print("       defeating evil?")
            sleep(2.5)
            print(divider)
            print("Librarian: Let's talk in my office.")
            sleep(1.8)
            print(divider)
            typewriter_print("You and Ember go into the librarian's office.", 0.08)
            sleep(2)
            print(divider)
            print("Librarian: You guys are trying to defeat the evil being, right? I have a scroll that will help you succeed.")
            sleep(3.5)
            print(divider)
            print("Scroll: Inside mist you may go, under rocks you could travel. Row in a sea of water, you shall find your path to justice.")
            sleep(4.3)
            print(divider)
            print("Librarian: I already kind of decoded this message, you are supposed to go to the Aqua Kingdom and go inside a waterfall.")
            sleep(3.7)
            print(divider)
            print("Zayden: Thank you so much! We need to get going.")
            sleep(2)
            print(divider)
            print("Librarian: Good luck on your journey.")
            sleep(1)
            done = "yes"
            aqua1(energy, astrocoins, your_health)
        elif walk_where == "b":
            sleep(1)
            print(divider)
            typewriter_print("""
            
You go and find the blacksmith

""", 0.08)
            sleep(2)
            typewriter_print("You and Ember go inside blacksmith shop.", 0.08)
            sleep(1.5)
            print(divider)
            print("Clank! Clack! Clank!")
            sleep(1.8)
            print(divider)
            print("Ember: Hello? Blacksmith?")
            sleep(2.5)
            print("Blacksmith: Oh yes? What do you need?")
            sleep(2)
            print(divider)
            print("Zayden: We need a quick talk please.")
            sleep(2)
            print(divider)
            print("Blacksmith: Oh sure, come in my workshop when I'm done making this ninja star.")
            sleep(2.5)
            print(divider)
            typewriter_print("You and Ember go into the blacksmith's workshop.", 0.08)
            sleep(2)
            print(divider)
            print("Blacksmith: So, what do you guys need?")
            sleep(2)
            print(divider)
            print("Zayden: We need a way to defeat the evil being.")
            sleep(4.3)
            print(divider)
            print("Blacksmith: Oh, you have came. There was this masked figure that told me to tell two people to go to the Inferno Kingdom to help defeat the evil being. That's all I got.")
            sleep(4.5)
            print(divider)
            print("Zayden: Thanks very much! We need to continue our journey.")
            sleep(2)
            print(divider)
            print("Blacksmith: Safe travels!")
            sleep(1)
            done = "yes"
            fire1(energy, astrocoins, your_health)
        else:
            print("You gave an invalid answer")



"""
--------------------------------
_________________________________

This is the Aqua Kingdom path
_________________________________
--------------------------------
"""

#first event that may happen
#how to perform: aqua1(energy, astrocoins, your_health)
def aqua1(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
You and Ember arrive at the Great Moat of the Aqua Kingdom.

""", 0.07)
    sleep(1.5)
    print("Ember: Ugh I hate water, how are we supposed to get to the main land?")
    sleep(2.5)
    print(divider)
    lucky_or_not = choice(["no", "yes", "yes"])
    if lucky_or_not == "yes":
        print("Zayden: Um, oh look! There is a canoe over there! We are so lucky!")
        sleep(2)
        print(divider)
        typewriter_print("Zayden and Ember get into the canoe.", 0.08)
        sleep(1)
        print(divider)
        print("Oh no, what if this flips and...")
        sleep(2)
        print(divider)
        print("Zayden: Oh it won't trust me. Let's start rowing.")
        sleep(2)
        print(divider)
    elif lucky_or_not == "no":
        print("Zayden: I think we need to construct a boat.")
        sleep(2)
        print(divider)
        print("You have to find: stone, 10 planks of wood, iron bars, and a big log.")
        looked_there1 = "no"
        looked_there2 = "no"
        while looked_there1 == "no" or looked_there2 == "no":
            print(divider)
            while True:
                look = input("Where do you want to look: Up in a coconut tree (1), in a crab hole (2), inside a pile of leaves (3), in the water (4), or in the sand (5). ").rstrip()
                if look == "1":
                    print("You look up a coconut tree...")
                    sleep(2)
                    print("You find nothing but a lot of coconuts")
                    break
                elif look == "2":
                    print("You look in a crab hole...")
                    sleep(2)
                    print("You see a small fish, guess it's their lunch.")
                    break
                elif look == "3":
                    if looked_there1 == "no":
                        print("You look inside a pile of leaves...")
                        sleep(2)
                        print("You find a stone and a big log!")
                        looked_there1 = "yes"
                        break
                    elif looked_there1 == "yes":
                        print("You already looked here.")
                        break
                elif look == "4":
                    print("You look in the water...")
                    sleep(2)
                    print("You see nothing but sand and more sand.")
                    break
                elif look == "5":
                    if looked_there2 == "no":
                        print("You look in the sand...")
                        sleep(2)
                        print("You find 10 planks of wood and iron bars! There must be people littering here.")
                        looked_there2 = "yes"
                        break
                    elif looked_there2 == "yes":
                        print("You already looked here.")
                        break
                else:
                    print("You gave an invalid answer.")
                    continue
        sleep(2)
        print(divider)
        typewriter_print("You build a boat to cross the Great Moat!", 0.08)
        sleep(1)
        print(divider)
    print("Suddenly, a HUGE wave and 5 waterspouts start forming on the water!")
    sleep(2)
    print(divider)
    print("Ember: THIS MOAT IS ENCHANTED!!! QUICK! ROW!")
    sleep(1.9)
    for _ in range(3):
        while True:
            print(divider)
            rowing = input("Where do you want to row! Forward (1), left (2), or right (3) ")
            chance_of_striking = choice(["1", "2", "3"])
            if rowing == "1" or rowing == "2" or rowing == "3":
                if rowing == chance_of_striking:
                    print(divider)
                    print("You got hit!")
                    sleep(1)
                    your_health -= 5
                    break
                else:
                    print(divider)
                    print("You didn't get hit")
                    sleep(1.5)
                    break
            else:
                print("You gave an invalid answer")
                continue
    sleep(2)
    if your_health <= 0:
        your_health = 0
        print("You died in the Great Moat")
        sys.exit("Game Ended")
    print(divider)
    print(f"""
    
You have {your_health} health right now.

""")
    sleep(1.5)
    print("You got to the other side of the moat.")
    sleep(2)
    print(divider)
    print("Ember: OH MY GOODNESS, WE GOT OUT ALIVE WHOOOOOO! Oh wait, why is there a shiny thing coming down from the sky.")
    sleep(3.5)
    print(divider)
    typewriter_print("You and Ember go and see what that is.", 0.08)
    sleep(1)
    print(divider)
    typewriter_print("""It is a scroll  

Next to it is a note""", 0.07)
    print(divider)
    typewriter_print("Hi heros, I'm that Wizard on that stone, next to the 2 signs.", 0.07)
    sleep(1)
    print(divider)
    typewriter_print("Every time you successfully get out of a disaster, I will send you a Reward Scroll to help you.", 0.07)
    sleep(1)
    print(divider)
    typewriter_print("What you guys are doing are very awesome and will benefit Celestiaterra a lot, I will help you as much as I can.", 0.07)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    aqua2(energy, astrocoins, your_health)
        
#the second event that might happen
#how to perform: aqua2(energy, astrocoins, your_health)
def aqua2(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
You and Ember walk off the beach, a soft breeze blows by, you see a village in the distance.

""", 0.08)
    sleep(1.5)
    while True:
        path_chose = input("Do you choose to go toward the village (1) or try to go around it (2)? ")
        if path_chose == "1":
            sleep(1)
            print(divider)
            typewriter_print("You and Ember walk toward the village.", 0.08)
            sleep(1)
            print(divider)
            print("Ember: Um, Zayden, why does this village look so... abandoned?")
            sleep(3)
            print(divider)
            typewriter_print("SUDDENLY, the village disappears in sight and gets replaced by walls of water.", 0.07)
            sleep(1)
            print(divider)
            print("Ember: Oh no, this is really really bad!")
            sleep(2)
            print(divider)
            print("Aqua Guardian: HA HA HA! You guys are so foolish to venture into my kingdom!")
            sleep(2)
            print(divider)
            print("Zayden: Your kingdom? Your the Aqua Guardian!")
            sleep(1.9)
            print(divider)
            print("Aqua Guardian: Yes, I am, and I created this water maze for you guys! If you guys can't complete it in 7 tries, it will collapse on you. Good luck! HA HA HA!")
            sleep(3)
            print(divider)
            counter = 0
            correct_ways = [str(randint(1,2)), str(randint(1,2)), str(randint(1,2))]
            player_ways = []
            done_correctly = "no"
            while counter < 7: 
                while True:
                    turn1 = input("Do you want to turn left (1) or right (2)? ")
                    if turn1 == "1" or turn1 == "2":
                        player_ways.append(turn1)
                        break
                    else:
                        print("You gave an invalid answer")
                        continue
                sleep(0.7)
                print(divider)
                while True: 
                    turn2 = input("Do you want to turn left (1) or right (2)? ")
                    if turn2 == "1" or turn2 == "2":
                        player_ways.append(turn2)
                        break
                    else:
                        print("You gave an invalid answer")
                        continue
                sleep(0.7)
                print(divider)
                while True:
                    turn3 = input("Do you want to turn left (1) or right (2)? ")
                    if turn3 == "1" or turn3 == "2":
                        player_ways.append(turn3)
                        break
                    else:
                        print("You gave an invalid answer")
                        continue
                counter += 1

                if player_ways == correct_ways:
                    print("You finished the maze correctly!")
                    done_correctly = "yes"
                    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
                    break
                else:
                    print("That are not the correct turns.")

            sleep(2)
            if done_correctly == "no":
                print(divider)
                typewriter_print("The water collapses on Zayden and Ember, you lose 12 health.", 0.08)
                your_health -= 12
                if your_health <= 0:
                    your_health = 0
                    print("You died in the maze.")
                    sys.exit("Game Ended")
            break
        elif path_chose == "2":
            sleep(1)
            print(divider)
            typewriter_print("You and Ember walk around the village into a jungle.", 0.07)
            sleep(1)
            print(divider)
            print("Zayden: This jungle looks so creepy, I feel like something is-")
            sleep(2)
            print(divider)
            print("Aqua Guardian: WELCOME visitors to the Perish Jungle! I am the Aqua Guardian.")
            sleep(2)
            print(divider)
            print("Ember: What do you want?!")
            sleep(1.7)
            print(divider)
            print("Aqua Guardian: I will ask you a series of questions and you need to answer each one correctly, or else... heh heh heh, you'll see.")
            sleep(3)
            print(divider)
            question1 = input("What did the text on the apple outside of the prison cell say? ").lower().rstrip()
            if question1 == "chess is fun":
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered correctly.")
                print(divider)
                sleep(2)
            else:
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered incorrectly, I shall take away 5 of your health!")
                print(divider)
                sleep(2.5)
                your_health -= 5
                print(f"You have {your_health} health now.")
                print(divider)
                sleep(2)
            question2 = input("How many waterspouts did I send to kill you? Hee hee hee. ").lower().rstrip()
            if question2 == "5" or question2 == "five":
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered correctly.")
                print(divider)
                sleep(2)
            else:
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered incorrectly, I shall take away 10 of your health!")
                print(divider)
                sleep(2.5)
                your_health -= 10
                print(f"You have {your_health} health now.")
                print(divider)
                sleep(2)
            print("What color hood did Ember wear when you saw him?")
            sleep(2)
            print(divider)
            print("Ember: Oh I know, it is- ")
            sleep(1.5)
            print(divider)
            question3 = input("Aqua Guardian: Hush, or I'm going to end both of you. ").lower().rstrip()
            if question3 == "navy blue":
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered correctly.")
                print(divider)
                sleep(2)
            else:
                sleep(2)
                print(divider)
                print("Aqua Guardian: You answered incorrectly, I shall take away 10 of your health!")
                print(divider)
                sleep(2.5)
                your_health -= 10
                print(f"You have {your_health} health now.")
                print(divider)
                sleep(2)
            sleep(1)
            if your_health <= 0:
                your_health = 0
                print("You died from the questions of doom.")
                sys.exit("Game Ended")
            print("Aqua Guardian: Nice, you survived. I will leave you in peace for now. FOR NOW.")
            sleep(2.5)
            print(divider)
            print("Ember: Phew!")
            aqua3(energy, astrocoins, your_health)
            break
        else:
            print("You gave an invalid answer")
            continue
    #event here

#the third event that might happen
#how to perform: aqua3(energy, astrocoins, your_health)
def aqua3(energy, astrocoins, your_health):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember goes deep into the jungle.

""", 0.08)
    sleep(1)
    typewriter_print("There is a creek down a little hill.", 0.08)
    sleep(1)
    print(divider)
    print("Ember: Ah finally I need some water.")
    sleep(1.7)
    print(divider)
    print("Zayden: NO WAIT- ")
    sleep(1)
    print(divider)
    typewriter_print("SLASH!!! Hungry piranhas come and bite onto Ember!", 0.08)
    sleep(1)
    print(divider)
    print("Ember: HELP!")
    energy, your_health = battle(energy, your_health)
    sleep(2)
    print(divider)
    typewriter_print("HERE COMES ANOTHER ONE WATCH OUT", 0.08)
    energy, your_health = battle(energy, your_health)
    sleep(3)
    print(divider)
    print("Ember: I am so sorry! Thank you so much!")
    sleep(2)
    print(divider)
    print("Zayden: No problem, just listen to me next time okay? I have water bottles.")
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    typewriter_print("Zayden and Foliage got out of the jungle.", 0.08)
    aqua4(energy, astrocoins, your_health)


#fourth event that might happen
#how to perform: aqua4(energy, astrocoins, your_health)
def aqua4(energy, astrocoins, your_health):
    sleep(2)
    typewriter_print("""
    
Zayden and Ember come to a waterfall, 

""", 0.08)
    sleep(1)
    print("Ember: We are suppsoed to go into the waterfall? That's what the librarian said.")
    sleep(2.1)
    print(divider)
    print("Zayden: I suppose?")
    sleep(3)
    print(divider)
    print("Wizard: Hello! I will help you!")
    sleep(1.9)
    print(divider)
    while True:
        hard_or_easy = input("""What do you want to say:
        
May you please help us get past this waterfall? Thank you very much! (1)

Help us! Get this waterfall away! (2)

""").rstrip()
        if hard_or_easy == "1":
            sleep(2)
            print("Wizard: Yes! That is what I'm here for! You have to repeat after my spells. Take your time. But you can also skip.")
            sleep(3)
            print(divider)
            while True:
                skip = input("Do you want to skip for 5 astrocoins? Yes (y) No (n) ").lower().rstrip()
                if skip == "n":
                    print(divider)
                    print("Zayden: Okay, let's start.")
                    sleep(1.5)
                    print(divider)
                    spell1()
                    break
                elif skip == "y":
                    print(divider)
                    print("Wizard: Okay, you'll skip the questions, I'll have to take 5 astrocoins.")
                    astrocoins -= 5
                    break
                else:
                    print("You gave an invalid answer")
                    continue
            break

        elif hard_or_easy == "2":
            sleep(2)
            print("Wizard: Okay. Repeat after my spells.")
            sleep(1.7)
            print(divider)
            spell1_()
            break
        else:
            print("You gave an invalid answer")
            continue
    sleep(2)
    print(divider)
    typewriter_print("Woosh! The water suddenly stops and the rocks roll aside, showing a tunnel inside the waterfall.", 0.05)
    sleep(1.5)
    print(divider)
    print("Ember: Thank you so much wizard!")
    sleep(1.7)
    print(divider)
    print("Wizard: No problem, see you soon.")
    sleep(1.7)
    print(divider)
    typewriter_print("The wizard dissolves into air and dissapears.", 0.08)
    sleep(1)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    aqua5(energy, astrocoins, your_health)



#the spells you need to say  
def spell1():
    spellone = input("""
    
MiSt goNE, roCks PaRt. sUn warMs WeT lAnd. 

""").rstrip()
    if spellone == "MiSt goNE, roCks PaRt. sUn warMs WeT lAnd.":
        sleep(2)
        print(divider)
        print("Wizard: The first spell is correct!")
        sleep(2)
        spell2()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1()

def spell2():
    spell2 = input("""
    
pArTnERs gO oN haRD TrIaLs, aNd FaCe thE fIercest wAVES.

""").rstrip()
    if spell2 == "pArTnERs gO oN haRD TrIaLs, aNd FaCe thE fIercest wAVES.":
        sleep(2)
        print(divider)
        print("Wizard: The second spell is correct!")
        sleep(2)
        spell3()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1()

def spell3():
    spell3 = input("""
    
bLazEs oF DeAtH, wHom shALl exTiNguIsh. CaOHs IN tHE LaND cOuld be STOppEd.

""").rstrip()
    if spell3 == "bLazEs oF DeAtH, wHom shALl exTiNguIsh. CaOHs IN tHE LaND cOuld be STOppEd.":
        sleep(2)
        print(divider)
        print("Wizard: The third spell is correct!")
        sleep(2)
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1()


#the hard spells you need to say  
def spell1_():
    spellone = input("""
    
MiSt goNE, roCks PaRt. sUn warMs WeT lAnd. 

""").rstrip()
    if spellone == "MiSt goNE, roCks PaRt. sUn warMs WeT lAnd.":
        sleep(2)
        print(divider)
        print("Wizard: The first spell is correct!")
        sleep(2)
        spell2_()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1_()

def spell2_():
    spell2 = input("""
    
pArTnERs gO oN haRD TrIaLs, aNd FaCe thE fIercest wAVES.

""").rstrip()
    if spell2 == "pArTnERs gO oN haRD TrIaLs, aNd FaCe thE fIercest wAVES.":
        sleep(2)
        print(divider)
        print("Wizard: The second spell is correct!")
        sleep(2)
        spell3_()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1_()

def spell3_():
    spell3 = input("""
    
bLazEs oF DeAtH, wHom shALl exTiNguIsh. CaOHs IN tHE LaND cOuld be STOppEd.

""").rstrip()
    if spell3 == "bLazEs oF DeAtH, wHom shALl exTiNguIsh. CaOHs IN tHE LaND cOuld be STOppEd.":
        sleep(2)
        print(divider)
        print("Wizard: The third spell is correct!")
        sleep(2)
        spell4_()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1_()

def spell4_():
    spell4 = input("""
    
yOu sHalL UsE mOre BeTTEr mAnnErS, aNd ChOsE yoUr wOrDs WiSelY.

""").rstrip()
    if spell4 == "yOu sHalL UsE mOre BeTTEr mAnnErS, aNd ChOsE yoUr wOrDs WiSelY.":
        sleep(2)
        print(divider)
        print("Wizard: The fourth, um ... spell is correct!")
        sleep(2)
        spell5_()
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1_()

def spell5_():
    spell5 = input("""
    
hA Ha hEE hEe HeH hEh hEH, i hAvE TrIckEd yOu, pLeAse bE mORe PoLiTe nExT TImE.

""").rstrip()
    if spell5 == "hA Ha hEE hEe HeH hEh hEH, i hAvE TrIckEd yOu, pLeAse bE mORe PoLiTe nExT TImE.":
        sleep(2)
        print(divider)
        print("Wizard: The fifth, lesson is done")
        sleep(2)
    else:
        sleep(2)
        print("Wizard: That is incorrect, we will have to restart.")
        print(divider)
        spell1_()

#the fifth event that might happen
#how to perform: aqua5(energy, astrocoins, your_health)
def aqua5(energy, astrocoins, your_health):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    print("""
    
Zayden and Ember enter the cave, there are shiney crystals here and there.

""", 0.07)
    sleep(1)
    print("Ember: Ooh! Nice crystals! Could we take some as money?")
    sleep(2)
    print(divider)
    while True:
        take_crystals = input("Do you want to take some crystals? Yes (y) or No (n) ").lower().rstrip()
        if take_crystals == "y":
            sleep(1)
            print(divider)
            typewriter_print("You and Ember take some crystals.", 0.08)
            sleep(1)
            print(divider)
            print("You gained 10 AstroCoins!")
            astrocoins += 10
            sleep(1.2)
            print(divider)
            print(f"You have {astrocoins} AstroCoins now!")
            sleep(2)
            print(divider)
            print("Suddenly")
            sleep(1)
            print("SOME OF THE CRYSTALS SEEMED TO HAVE COME ALIVE!!!")
            sleep(2.1)
            print(divider)


            print("Prepare to fight...")
            enemyhealth = randint(150, 170)
            print(f"You have {your_health} health")
            while enemyhealth > 0:
                sleep(1)
                print(divider)
                print(f"You have {energy} energy")
                if whatclass == "hunter":
                    print(f"Your attacks are {hunter}.")
                elif whatclass == "archer":
                    print(f"Your attacks are {archer}.")
                elif whatclass == "wizard":
                    print(f"Your attacks are {wizard}.")
                elif whatclass == "spearman":
                    print(f"Your attacks are {spearman}.")
                elif whatclass == "bandit":
                    print(f"Your attacks are {bandit}.")
                elif whatclass == "swordsman":
                    print(f"Your attacks are {swordsman}.")
                elif whatclass == "dev":
                    print(f"Your attacks are {dev}.")
                print(f"The enemy's health is {enemyhealth}")
                attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
                if whatclass == "hunter":
                    if attack == "rifle shot":
                        if energy >= hunterenergycosts.get("Rifle Shot"):
                            energy -= hunterenergycosts.get("Rifle Shot")
                            enemyhealth -= hunterdamage.get("Rifle Shot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "rifle smack":
                        if energy >= hunterenergycosts.get("Rifle Smack"):
                            energy -= hunterenergycosts.get("Rifle Smack")
                            enemyhealth -= hunterdamage.get("Rifle Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "rifle headshot":
                        if energy >= hunterenergycosts.get("Rifle Headshot"):
                            energy -= hunterenergycosts.get("Rifle Headshot")
                            enemyhealth -= hunterdamage.get("Rifle Headshot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "archer":
                    if attack == "bow and arrow":
                        if energy >= archerenergycosts.get("Bow and arrow"):
                            energy -= archerenergycosts.get("Bow and arrow")
                            enemyhealth -= archerdamage.get("Bow and arrow")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "bow and arrow headshot":
                        if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                            energy -= archerenergycosts.get("Bow and arrow Headshot")
                            enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "bow smack":
                        if energy >= archerenergycosts.get("Bow Smack"):
                            energy -= archerenergycosts.get("Bow Smack")
                            enemyhealth -= archerdamage.get("Bow Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "arrow smack":
                        if energy >= archerenergycosts.get("Arrow Smack"):
                            energy -= archerenergycosts.get("Arrow Smack")
                            enemyhealth -= archerdamage.get("Arrow Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "shotgun attack":
                        if energy >= archerenergycosts.get("Shotgun Attack"):
                            energy -= archerenergycosts.get("Shotgun Attack")
                            enemyhealth -= archerdamage.get("Shotgun Attack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "minigun attack":
                        if energy >= archerenergycosts.get("Minigun Attack"):
                            energy -= archerenergycosts.get("Minigun Attack")
                            enemyhealth -= archerdamage.get("Minigun Attack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "wizard":
                    if attack == "staff smack":
                        if energy >= wizardenergycosts.get("Staff Smack"):
                            energy -= wizardenergycosts.get("Staff Smack")
                            enemyhealth -= wizarddamage.get("Staff Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "water spell":
                        if energy >= wizardenergycosts.get("Water Spell"):
                            energy -= wizardenergycosts.get("Water Spell")
                            enemyhealth -= wizarddamage.get("Water Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "fire spell":
                        if energy >= wizardenergycosts.get("Fire Spell"):
                            energy -= wizardenergycosts.get("Fire Spell")
                            enemyhealth -= wizarddamage.get("Fire Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "electric spell":
                        if energy >= wizardenergycosts.get("Electric Spell"):
                            energy -= wizardenergycosts.get("Electric Spell")
                            enemyhealth -= wizarddamage.get("Electric Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "slam against a wall spell":
                        if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                            energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                            enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "meteor shower":
                        if energy >= wizardenergycosts.get("Meteor Shower"):
                            energy -= wizardenergycosts.get("Meteor Shower")
                            enemyhealth -= wizarddamage.get("Meteor Shower")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "bandit":
                    if attack == "dagger slash":
                        if energy >= banditenergycosts.get("Dagger Slash"):
                            energy -= banditenergycosts.get("Dagger Slash")
                            enemyhealth -= banditdamage.get("Dagger Slash")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "boomerang throw":
                        if energy >= banditenergycosts.get("Boomerang Throw"):
                            energy -= banditenergycosts.get("Boomerang Throw")
                            enemyhealth -= banditdamage.get("Boomerang Throw")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "spearman":
                    if attack == "spear stab":
                        if energy >= spearmanenergycosts.get("Spear Stab"):
                            energy -= spearmanenergycosts.get("Spear Stab")
                            enemyhealth -= spearmandamage.get("Spear Stab")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "spear swing":
                        if energy >= spearmanenergycosts.get("Spear Swing"):
                            energy -= spearmanenergycosts.get("Spear Swing")
                            enemyhealth -= spearmandamage.get("Spear Swing")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "swordsman":
                    if attack == "sword stab":
                        if energy >= swordsmanenergycosts.get("Sword Stab"):
                            energy -= swordsmanenergycosts.get("Sword Stab")
                            enemyhealth -= swordsmandamage.get("Sword Stab")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "sword slash":
                        if energy >= swordsmanenergycosts.get("Sword Slash"):
                            energy -= swordsmanenergycosts.get("Sword Slash")
                            enemyhealth -= swordsmandamage.get("Sword Slash")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "sword poke":
                        if energy >= swordsmanenergycosts.get("Sword Poke"):
                            energy -= swordsmanenergycosts.get("Sword Poke")
                            enemyhealth -= swordsmandamage.get("Sword Poke")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "dev":
                    if attack == "ultimate laser":
                        if energy >= devenergycosts.get("Ultimate Laser"):
                            energy -= devenergycosts.get("Ultimate Laser")
                            enemyhealth -= devdamage.get("Ultimate Laser")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if attack == "d":
                    print("You defended! You gained 20 health!")
                    your_health += 20
                    energy -= 3

                if your_health <= 0:
                    your_health = 0
                    print(divider)
                    print("You died.")
                    print(divider)
                    sys.exit("Game ended")
                elif enemyhealth <= 0:
                    print(divider)
                    print("You defeated the enemy! You gained some health and energy")
                    print(divider)
                    your_health += 110
                    energy += 15
                    print(f"You have {your_health} health and {energy} energy")
                    break

                sleep(2)
                enemy_attack = randint(10, 55)
                if whatclass == "hunter":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "archer":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "wizard":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "spearman":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "bandit":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "swordsman":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "dev":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")

                if your_health <= 0:
                    your_health = 0
                    print(divider)
                    print("You died.")
                    print(divider)
                    sys.exit("Game ended")
            sleep(2)
            print(divider)
            print("HERE COMES ANOTHER ONE!!!")
            sleep(2)
            print(divider)


            print("Prepare to fight... again...")
            enemyhealth = randint(150, 170)
            print(f"You have {your_health} health")
            while enemyhealth > 0:
                sleep(1)
                print(divider)
                print(f"You have {energy} energy")
                if whatclass == "hunter":
                    print(f"Your attacks are {hunter}.")
                elif whatclass == "archer":
                    print(f"Your attacks are {archer}.")
                elif whatclass == "wizard":
                    print(f"Your attacks are {wizard}.")
                elif whatclass == "spearman":
                    print(f"Your attacks are {spearman}.")
                elif whatclass == "bandit":
                    print(f"Your attacks are {bandit}.")
                elif whatclass == "swordsman":
                    print(f"Your attacks are {swordsman}.")
                elif whatclass == "dev":
                    print(f"Your attacks are {dev}.")
                print(f"The enemy's health is {enemyhealth}")
                attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
                if whatclass == "hunter":
                    if attack == "rifle shot":
                        if energy >= hunterenergycosts.get("Rifle Shot"):
                            energy -= hunterenergycosts.get("Rifle Shot")
                            enemyhealth -= hunterdamage.get("Rifle Shot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "rifle smack":
                        if energy >= hunterenergycosts.get("Rifle Smack"):
                            energy -= hunterenergycosts.get("Rifle Smack")
                            enemyhealth -= hunterdamage.get("Rifle Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "rifle headshot":
                        if energy >= hunterenergycosts.get("Rifle Headshot"):
                            energy -= hunterenergycosts.get("Rifle Headshot")
                            enemyhealth -= hunterdamage.get("Rifle Headshot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "archer":
                    if attack == "bow and arrow":
                        if energy >= archerenergycosts.get("Bow and arrow"):
                            energy -= archerenergycosts.get("Bow and arrow")
                            enemyhealth -= archerdamage.get("Bow and arrow")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "bow and arrow headshot":
                        if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                            energy -= archerenergycosts.get("Bow and arrow Headshot")
                            enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "bow smack":
                        if energy >= archerenergycosts.get("Bow Smack"):
                            energy -= archerenergycosts.get("Bow Smack")
                            enemyhealth -= archerdamage.get("Bow Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "arrow smack":
                        if energy >= archerenergycosts.get("Arrow Smack"):
                            energy -= archerenergycosts.get("Arrow Smack")
                            enemyhealth -= archerdamage.get("Arrow Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "shotgun attack":
                        if energy >= archerenergycosts.get("Shotgun Attack"):
                            energy -= archerenergycosts.get("Shotgun Attack")
                            enemyhealth -= archerdamage.get("Shotgun Attack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "minigun attack":
                        if energy >= archerenergycosts.get("Minigun Attack"):
                            energy -= archerenergycosts.get("Minigun Attack")
                            enemyhealth -= archerdamage.get("Minigun Attack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "wizard":
                    if attack == "staff smack":
                        if energy >= wizardenergycosts.get("Staff Smack"):
                            energy -= wizardenergycosts.get("Staff Smack")
                            enemyhealth -= wizarddamage.get("Staff Smack")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "water spell":
                        if energy >= wizardenergycosts.get("Water Spell"):
                            energy -= wizardenergycosts.get("Water Spell")
                            enemyhealth -= wizarddamage.get("Water Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "fire spell":
                        if energy >= wizardenergycosts.get("Fire Spell"):
                            energy -= wizardenergycosts.get("Fire Spell")
                            enemyhealth -= wizarddamage.get("Fire Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "electric spell":
                        if energy >= wizardenergycosts.get("Electric Spell"):
                            energy -= wizardenergycosts.get("Electric Spell")
                            enemyhealth -= wizarddamage.get("Electric Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "slam against a wall spell":
                        if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                            energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                            enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "meteor shower":
                        if energy >= wizardenergycosts.get("Meteor Shower"):
                            energy -= wizardenergycosts.get("Meteor Shower")
                            enemyhealth -= wizarddamage.get("Meteor Shower")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "bandit":
                    if attack == "dagger slash":
                        if energy >= banditenergycosts.get("Dagger Slash"):
                            energy -= banditenergycosts.get("Dagger Slash")
                            enemyhealth -= banditdamage.get("Dagger Slash")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "boomerang throw":
                        if energy >= banditenergycosts.get("Boomerang Throw"):
                            energy -= banditenergycosts.get("Boomerang Throw")
                            enemyhealth -= banditdamage.get("Boomerang Throw")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "spearman":
                    if attack == "spear stab":
                        if energy >= spearmanenergycosts.get("Spear Stab"):
                            energy -= spearmanenergycosts.get("Spear Stab")
                            enemyhealth -= spearmandamage.get("Spear Stab")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "spear swing":
                        if energy >= spearmanenergycosts.get("Spear Swing"):
                            energy -= spearmanenergycosts.get("Spear Swing")
                            enemyhealth -= spearmandamage.get("Spear Swing")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "swordsman":
                    if attack == "sword stab":
                        if energy >= swordsmanenergycosts.get("Sword Stab"):
                            energy -= swordsmanenergycosts.get("Sword Stab")
                            enemyhealth -= swordsmandamage.get("Sword Stab")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "sword slash":
                        if energy >= swordsmanenergycosts.get("Sword Slash"):
                            energy -= swordsmanenergycosts.get("Sword Slash")
                            enemyhealth -= swordsmandamage.get("Sword Slash")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    elif attack == "sword poke":
                        if energy >= swordsmanenergycosts.get("Sword Poke"):
                            energy -= swordsmanenergycosts.get("Sword Poke")
                            enemyhealth -= swordsmandamage.get("Sword Poke")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if whatclass == "dev":
                    if attack == "ultimate laser":
                        if energy >= devenergycosts.get("Ultimate Laser"):
                            energy -= devenergycosts.get("Ultimate Laser")
                            enemyhealth -= devdamage.get("Ultimate Laser")
                            if enemyhealth <= 0:
                                enemyhealth = 0
                            print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                            print(divider)
                        else:
                            print("You don't have enough energy points to battle! The enemy kills you.")
                            break
                            sys.exit("You die")
                    else:
                        print("Your class can't do that attack, you don't attack, the enemy attacks.")
                        print(divider)
                if attack == "d":
                    print("You defended! You gained 20 health!")
                    your_health += 20
                    energy -= 3

                if your_health <= 0:
                    your_health = 0
                    print(divider)
                    print("You died.")
                    print(divider)
                    sys.exit("Game ended")
                elif enemyhealth <= 0:
                    print(divider)
                    print("You defeated the enemy! You gained some health and energy")
                    print(divider)
                    your_health += 110
                    energy += 15
                    print(f"You have {your_health} health and {energy} energy")
                    break

                sleep(2)
                enemy_attack = randint(10, 55)
                if whatclass == "hunter":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "archer":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "wizard":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "spearman":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "bandit":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "swordsman":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")
                elif whatclass == "dev":
                    print(
                        f"You have {your_health} health."
                    )
                    print(divider)
                    print(f"The enemy dealed {enemy_attack} damage to you!")
                    your_health -= enemy_attack
                    if your_health <= 0:
                        your_health = 0
                    print(f"You have {your_health} health now.")

                if your_health <= 0:
                    your_health = 0
                    print(divider)
                    print("You died.")
                    print(divider)
                    sys.exit("Game ended")
                
            sleep(2)
            print(divider)
            print("You survived the attack.")
            energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
            break
        
        elif take_crystals == "n":
            sleep(1.5)
            print(divider)
            print("You don't take the crystals.")
            break

        else:
            print("You gave an invalid answer")
            continue

    sleep(2)
    print(divider)
    print("Crystal Golem: WHO DARES TO TRESPASS INTO MY TERRITORY?")
    sleep(2)
    print(divider)
    energy, your_health = battle(energy, your_health)
    sleep(2)
    print(divider)
    print("You survived")
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    sleep(1)
    print(divider)
    typewriter_print("Zayden and Ember quickly run further into the cavern.", 0.08)
    aqua6(energy, astrocoins, your_health)

#the sixth event that might happen, MINIBOSS TIME!!!
#how to perform: aqua6(energy, astrocoins, your_health)
def aqua6(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember arrive at the end of the crystal cavern, the chamber is lit with bright shiney crystals.

""", 0.06)
    sleep(1.5)
    typewriter_print("FWOOSH", 0.05)
    sleep(1.5)
    print(divider)
    typewriter_print("All of a sudden, a HUGE wave with a face emerges.", 0.07)
    sleep(3)
    print(divider)
    print("Aqua Guardian: I am the Aqua Guardian! You shall not pass this final stage to defeat the evil being, unless you defeat me.")
    sleep(4)
    print(divider)
    print("Zayden: We will defeat you, and the evil being too!")
    sleep(3)
    print(divider)
    print("Aqua Guardian: I will let you pass if you defeat me, but if you don't, you will get locked up by the evil soldiers.")
    sleep(4)
    print("               Are you ready?")
    sleep(3)
    print("Ember: Sure, let's fight!")


    sleep(2)
    print(divider)
    print("Prepare to fight, MINIBOSS TIME...")
    sleep(2)
    enemyhealth = 390
    print(f"You have {your_health} health")
    sleep(1.5)
    print(divider)
    print(f"The Aqua Guardian has {enemyhealth} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        ember_attack = randint(10, 50)
        sleep(2)
        print(divider)
        print(f"Ember dealed {ember_attack} damage to the Aqua Guardian!")
        enemyhealth -= ember_attack

        if enemyhealth <= 0:
            print(divider)
            print("You and Ember defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
            

    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)

    sleep(3.5)
    print(divider)
    print("Aqua Guardian: You defeated me! Looks like you two are the chosen ones. I'll let you pass.")
    wizard_choose(energy, astrocoins, your_health)

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------


"""
--------------------------------
_________________________________

This is the Inferno Kingdom path
_________________________________
--------------------------------
"""

#the first event that might happen
#how to perform: fire1(energy, astrocoins, your_health)
def fire1(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember get to the borders of the Inferno Kingdom

""", 0.08)
    sleep(1)
    print("Ember: Look, there is a fire wall with 5 archer towers here, we have to break it to get past.")
    sleep(3)
    print(divider)
    print("Zayden: I'll do it.")
    sleep(1.7)
    print(divider)
    enemyhealth = 200
    print(f"You have {your_health} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use?").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack")
                print(divider)
    sleep(2)
    typewriter_print("""
    
CRASH!!!

""", 0.1)
    typewriter_print("The fire wall tumbles to the ground.", 0.08)
    sleep(1)
    print(divider)
    print("Ember: Let's go.")
    fire2(energy, astrocoins, your_health)

    
#the second event that might happen
#how to perform: fire2(energy, astrocoins, your_health)
def fire2(energy, astrocoins, your_health):
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    sleep(1)
    print(divider)
    typewriter_print("Once they get across the wall, they find a shiny thing stuck in a little rock crevice.", 0.08)
    typewriter_print("You and Ember go check it out.", 0.08)
    sleep(1)
    print(divider)
    typewriter_print("""It is a scroll  

Next to it is a note""", 0.07)
    print(divider)
    typewriter_print("Hi heros, I'm that Wizard on that stone, next to the 2 signs. Remember me?", 0.07)
    sleep(1)
    print(divider)
    typewriter_print("Every time you successfully get out of a disaster, I will send you a Reward Scroll to help you.", 0.07)
    sleep(1)
    print(divider)
    typewriter_print("What you guys are doing are very awesome and will benefit Celestiaterra a lot, I will help you as much as I can.", 0.07)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
    sleep(2)
    print(divider)
    while True:
        path = input("You and Ember get to a split path. Where do you want to go? Left (l) or Right (r) ").lower().rstrip()
        if path == "l":
            sleep(2)
            print(divider)
            print("You and Ember go left.")
            fire3(energy, astrocoins, your_health)
            break
        elif path == "r":
            sleep(2)
            print(divider)
            print("You and Ember go right.")
            fire4(energy, astrocoins, your_health)
            break
        else:
            print("You gave an invalid answer")
            continue
    fire5(energy, astrocoins, your_health)


#when you go left for fire2
#how to perform: fire3(energy, astrocoins, your_health)
def fire3(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember arrive at a little cliff, a river of lava runs beneath it.

""", 0.08)
    sleep(1)
    print(divider)
    print("Ember: Look, the path is on the other side of the cliff. We have to get over the cliff.")
    sleep(2.1)
    print(divider)
    print("Zayden: Yup, I don't want to fall in that lava- ")
    sleep(1.9)
    print(divider)
    typewriter_print("FOOM!!! Two Molten Soldiers come out of the little volcanoes beside the path.", 0.07)
    sleep(1)
    print(divider)
    print("Molten Soldiers: You guys will not go further into the Inferno Kingdom!")
    sleep(2)
    print(divider)
    print("Zayden: Ugh, we have to fight again.")
    sleep(1)
    energy, your_health = battle(energy, your_health)
    sleep(2)
    typewriter_print("""
    
Here comes the second one!

""", 0.08)
    sleep(1)
    energy, your_health = minion(energy, your_health)
    sleep(2)
    typewriter_print("""
    
You survived

""", 0.09)
    sleep(1)
    print(divider)
    print("Ember: Now we have to build a bridge.")
    sleep(1.9)
    print(divider)
    print("You have to find: Rock, 20 Fire Wood, and a long rope.")
    looked_there1 = "no"
    looked_there2 = "no"
    while looked_there1 == "no" or looked_there2 == "no":
        print(divider)
        while True:
            look = input(
                "Where do you want to look: In a mini volcano (1), under a big chunk of obsidian (2), or under molten rock (3) ").rstrip()
            if look == "1":
                print("You look in a mini volcano...")
                sleep(2)
                print("You find nothing but a bird nest.")
                break         
            elif look == "2":
                if looked_there2 == "no":
                    print("You look under obsidian...")
                    sleep(2)
                    print("You find 20 Fire Wood and a long rope.")
                    looked_there2 = "yes"
                    break
                elif looked_there2 == "yes":
                    print("You already looked here.")
                    break
            elif look == "3":
                if looked_there1 == "no":
                    print("You look under molten rock...")
                    sleep(2)
                    print("You find a rock! Of course...")
                    looked_there1 = "yes"
                    break
                elif looked_there1 == "yes":
                    print("You already looked here.")
                    break
            else:
                print("You gave an invalid answer.")
                continue
    sleep(2)
    print(divider)
    typewriter_print("You build a bridge to cross the cliff.", 0.08)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)


#when you go right for fire2
#how to perform: fire4(energy, astrocoins, your_health)
def fire4(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember come to a forest, well, a forest of dead trees.

""", 0.07)
    sleep(1)
    print("Zayden: Why does this look so creepy?")
    sleep(2)
    print(divider)
    typewriter_print("vmmmm", 0.1)
    sleep(2.5)
    print(divider)
    print("Ember: What was that?")
    sleep(2.5)
    print(divider)
    typewriter_print("VMMMM", 0.1)
    sleep(1)
    print(divider)
    print("Zayden: HORNETS!")
    sleep(1)
    print(divider)
    typewriter_print("Three Blaze Hornets come charging at Zayden and Ember.", 0.07)
    sleep(1)
    print(divider)
    energy, your_health = minion(energy, your_health)
    sleep(2)
    print("""
    
Here comes another one!

""")
    energy, your_health = minion(energy, your_health)
    sleep(2)
    print("""
    
Here comes another one!

""")
    energy, your_health = minion(energy, your_health)
    sleep(2)
    print(divider)
    print("You survived.")
    sleep(2)
    print(divider)
    print("Zayden: Quick! We have to destroy the hornet nest before they wake up!")
    sleep(2)
    print(divider)
    typewriter_print("Zayden and Ember run to the hornet nest.", 0.07)
    sleep(1)
    print(divider)
    done = "no"
    for _ in range(3):
        right_strength = choice(["1", "2", "3"])
        while True:
            strength = input("How hard do you hit? (1) (2) or (3) ").rstrip()
            if strength == "1" or strength == "2" or strength == "3":
                if strength == "1" and strength == right_strength:
                    sleep(2)
                    print(divider)
                    typewriter_print("You hit the nest!", 0.08)
                    sleep(1)
                    print(divider)
                    typewriter_print("The hornets died.", 0.08)
                    sleep(2)
                    done = "yes"
                    break
                elif strength == "2" and strength == right_strength:
                    sleep(2)
                    print(divider)
                    typewriter_print("You hit the nest!", 0.08)
                    sleep(1)
                    print(divider)
                    typewriter_print("The hornets died.", 0.08)
                    sleep(2)
                    done = "yes"
                    break
                elif strength == "3" and strength == right_strength:
                    sleep(2)
                    print(divider)
                    typewriter_print("You hit the nest!", 0.08)
                    sleep(1)
                    print(divider)
                    typewriter_print("The hornets died.", 0.08)
                    sleep(2)
                    done = "yes"
                    break
                else:
                    print("You gave an invalid answer")
                    continue

        if done == "yes":
            break
    
    if done == "no":
        sleep(2)
        print(divider)
        typewriter_print("The Hornets wake up and deal 20 damage.", 0.08)
        your_health -= 20
        print(divider)

    typewriter_print("Zayden and Ember continue on the path.", 0.08)
    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)


#the fifth event that might happen
#how to perform:fire5(energy, astrocoins, your_health)
def fire5(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
You arrive at a huge volcano.

""", 0.08)
    sleep(1)
    print("Ember: Woah, how are we supposed to get up? Ack! Lava!")
    sleep(1.9)
    print(divider)
    typewriter_print("Foosh! The Wizard appears in front of Zayden.", 0.07)
    sleep(1)
    print(divider)
    print("Zayden: AHHH! Oh, it's you Wizard. May you please help us out, get to the top of the volcano?")
    sleep(3)
    print(divider)
    print("Wizard: Yes, I will, you just need to answer a series of questions.")
    sleep(2)
    print(divider)
    print("Zayden: Okay, let's start.")
    question1 = input("How many archer towers are one the fire wall? ").lower().rstrip()
    if question1 == "5" or question1 == "five":
        sleep(2)
        print(divider)
        print("Wizard: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Wizard: You answered incorrectly, I will take away 10 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 10
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question2 = input("How many path options did you have when you went to the split path? ").lower().rstrip()
    if question2 == "2" or question2 == "two":
        sleep(2)
        print(divider)
        print("Wizard: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Wizard: You answered incorrectly, I will take away 10 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 10
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question3 = input("What weapon was the blacksmith making when you visited him? ").lower().rstrip()
    if question3 == "ninja star":
        sleep(2)
        print(divider)
        print("Wizard: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Wizard: You answered incorrectly, I will take away 10 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 10
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    sleep(1)
    if your_health <= 0:
        your_health = 0
        print("You died from the questions the wizard is asking.")
        sys.exit("Game Ended")

    print("Wizard: Congratulations, I will send you to the top!")
    sleep(2)
    print(divider)
    typewriter_print("In less than a second, Zayden and Ember gets teleported to the top of the volcano.", 0.07)
    fire6(energy, astrocoins, your_health)


#the sixth event that might happen MINIBOSS TIME!!!
#how to perform: fire6(energy, astrocoins, your_health)
def fire6(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Ember is at the top of the volcano

""",0.08)
    sleep(1)
    print("Zayden: Oh look! The volcano is frozen at the top. It's a large platform!")
    sleep(2.1)
    print(divider)
    typewriter_print("CRASH!!! A Molten lava monster appears in front of the two people.", 0.07)
    sleep(3)
    print(divider)
    print("Inferno Guardian: I am the Inferno Guardian! You shall not pass this final obstacle to defeat the evil being! Turn back now!")
    sleep(4)
    print(divider)
    print("Zayden: We will not turn back!")
    sleep(3)
    print(divider)
    print("Inferno Guardian: Hmph, arrogant human, if you don't defeat me, you will get locked up by the evil soldiers.")
    sleep(4)
    print("                  Are you ready?")
    sleep(3)
    print("Zayden: Of course!")


    sleep(2)
    print(divider)
    print("Prepare to fight, MINIBOSS TIME...")
    sleep(2)
    enemyhealth = 400
    print(f"You have {your_health} health")
    sleep(1.5)
    print(divider)
    print(f"The Inferno Guardian has {enemyhealth} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        ember_attack = randint(15, 60)
        sleep(2)
        print(divider)
        print(f"Ember dealed {ember_attack} damage to the Inferno Guardian!")
        enemyhealth -= ember_attack

        if enemyhealth <= 0:
            print(divider)
            print("You and Ember defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 200
            print(divider)
            print("You got defeated.")
            print(divider)
            sleep(2)
            print("You got captured by the evil soliders.")
            event1(astrocoins, energy, your_health)
            

    energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)

    sleep(3.5)
    print(divider)
    print("Inferno Guardian: The chosen ones, you are worthy to pass.")   
    wizard_choose(energy, astrocoins, your_health)

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------


"""
--------------------------------
_________________________________

This is the Final Two Paths
_________________________________
--------------------------------
"""

#two different endings to choose from
#how to perform: wizard_choose(energy, astrocoins, your_health)
def wizard_choose(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    print("Zayden: WOAH, where am I?")
    sleep(2)
    print(divider)
    print("Wizard: I have taken you to the transfer dimension, the dimesion where you teleport to places. This is also the last time you can trade.")
    sleep(3)
    print(divider)
    energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
    sleep(1.5)
    print(divider)
    print("Zayden: Wait, but where is my partner?")
    sleep(2)
    print(divider)
    print("Wizard: I sent him back home, I told him you need to do this by yourself.")
    sleep(2.1)
    print(divider)
    print("Zayden: Okay, what do I do now?")
    sleep(1.9)
    print(divider)
    done = "no"
    while done == "no":
        victory = input("Wizard: You have two choices, to go to reactivate the Cosmic Gem (1), or kill the evil being (I will help you) (2). ")
        if victory == "1":
            sleep(2)
            print(divider)
            print("Wizard: Okay, teleporting you now.")
            done = "yes"
            gem(energy, astrocoins, your_health)
        elif victory == "2":
            sleep(2)
            print(divider)
            print("Wizard: Okay, teleporting us now.")
            done = "yes"
            final_boss(energy, astrocoins, your_health)            
        else:
            print("You gave an invalid answer")


#activating the gem
#how to perform: gem(energy, astrocoins, your_health)
def gem(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("You arrive at a cave and go into it.", 0.07)
    sleep(1)
    print(divider)
    typewriter_print("You go deeper and see a big bat hanging from the roof of the cave.", 0.07)
    sleep(2)
    print(divider)
    print("Bat: I am the protector of the Cosmic Gem, answer my five questions and I'll let you pass.")
    sleep(2.5)
    question1 = input("How many layers are the prison walls of where you woke up? ").lower().rstrip()
    if question1 == "3" or question1 == "three":
        sleep(2)
        print(divider)
        print("Bat: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Bat: You answered incorrectly, I will take away 50 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 50
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question2 = input("What kind of forest is the forest the Wizard was next to two signs? ").lower().rstrip()
    if question2 == "pine":
        sleep(2)
        print(divider)
        print("Bat: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Bat: You answered incorrectly, I will take away 55 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 55
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question3 = input("What did the apple outside of the prison cell say? ").lower().rstrip()
    if question3 == "chess is fun":
        sleep(2)
        print(divider)
        print("Bat: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Bat: You answered incorrectly, I will take away 10 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 10
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question4 = input("What color was the stone the Wizard was sitting on? ").lower().rstrip()
    if question4 == "green":
        sleep(2)
        print(divider)
        print("Bat: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Bat: You answered incorrectly, I will take away 10 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 10
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)
    question5 = input("How many possible kingdoms could you go to? ").lower().rstrip()
    if question5 == "3" or question5 == "three":
        sleep(2)
        print(divider)
        print("Bat: You answered correctly!")
        print(divider)
        sleep(2)
    else:
        sleep(2)
        print(divider)
        print("Bat: You answered incorrectly, I will take away 40 of your health.")
        print(divider)
        sleep(2.5)
        your_health -= 40
        print(f"You have {your_health} health now.")
        print(divider)
        sleep(2)


    sleep(1)
    if your_health <= 0:
        your_health = 0
        print("You died from Cosmic Gem entrance questions.")
        sys.exit("Game Ended")

    sleep(2)
    print(divider)
    print("Bat: You are the chosen one, you are destined to defeat the evil being.")
    sleep(2)
    print("     I shall open the gates for you to reactvate the Cosmic Gem")
    sleep(2)
    print(divider)
    print("Zayden: Thank you!")
    sleep(1.2)
    print(divider)
    typewriter_print("Zayden comes to Cosmic Gem chamber.", 0.08)
    sleep(4)
    print(divider)
    typewriter_print("Zayden put's his hand on the gem.", 0.08)
    sleep(4)
    print(divider)
    typewriter_print("ACTIVATE", 0.5)
    sleep(2)
    print(divider)
    typewriter_print("SHOOM! A golden ray of light radiates from the gem and it starts glowing.", 0.07)
    sleep(4)
    print(divider)
    typewriter_print("Meanwhile...", 0.09)
    sleep(2)
    print(divider)
    typewriter_print("The evil being gets automaticly teleported into his chamber.", 0.07)
    sleep(2)
    print("Locked")
    sleep(2)
    print("Away")
    sleep(2.5)
    print("For eternity.")
    sleep(4)
    print(divider)
    victory()


#killing the evil being
#how to perform: final_boss(energy, astrocoins, your_health)
def final_boss(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    typewriter_print("""
    
Zayden and Wizard teleport on a large black platform.

""", 0.08)
    sleep(1)
    print("Zayden: Woah, this is the evil being's lair? Lame. ")
    sleep(1.9)
    print(divider)
    typewriter_print("BAM! The evil being made up of black smoke and has two bright red eyes appear in front of Zayden.", 0.06)
    sleep(1)
    print(divider)
    print("Zayden: AHHHHHHH! The evil being! You cruel and ugly monster!")
    sleep(3)
    print(divider)
    print("Evil Being: YOU, ZAYDEN. YOU TRY TO DEFEAT ME??? HA! COME AND I'LL DESTROY")
    sleep(2.5)
    print(divider)
    print("Zayden: I'm not scared of you dirty face.")
    sleep(2)
    print(divider)
    print("Evil Being: GRRRRRRR!!!")

    sleep(2)
    print(divider)
    print("Prepare to fight, FINAL BOSS TIME...")
    sleep(2)
    enemyhealth = 500
    print(f"You have {your_health} health")
    sleep(1.5)
    print(divider)
    print(f"The Evil Being has {enemyhealth} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You got defeated.")
            sleep(2)
            print("You died by the final boss.")
            sys.exit("Game Ended")
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        wizard_attack = randint(15, 60)
        sleep(2)
        print(divider)
        print(f"Wizard dealed {wizard_attack} damage to the Evil Being")
        enemyhealth -= wizard_attack

        if enemyhealth <= 0:
            print(divider)
            print("You and wizard defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You got defeated.")
            sleep(2)
            print("You died by the final boss.")
            sys.exit("Game Ended")
        

    sleep(4)
    print(divider)
    print("Evil Being: How- how did you defeat me?! NOOOOOOOOO!")  
    sleep(2)
    print(divider)
    typewriter_print("The evil being disintegrates into bits of black dust.", 0.08)
    sleep(2)
    print(divider)
    victory()


def victory():
    print("""
    
CONGRATULATIONS! You finished the game! There are more fun trials awaiting you on other paths.

""")
    sleep(2)
    sys.exit("You finished the game!")



# The shopping, or, trading funtion in the game, you will encounter these traders along your journey.
# How to perform: energy, astrocoins, your_health = trading(energy, astrocoins, your_health)
def trading(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    shop_item1 = choice(["Healing Herbs (3 AstroCoins) (Heals 20 health)", "Cookies (4 AstroCoins) (Gives 8 energy)",
                         "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)"])
    shop_item2 = choice(["Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)",
                         "Energy Drink (9 AstroCoins)(Gives energy but it's random)"])
    shop_item3 = choice(["Cooked Beef (5 AstroCoins) (Gives 10 energy)", "Cheese (2 AstroCoins) (Heals 10 health)"])
    shop_items_cost = {
        "Healing Herbs (3 AstroCoins) (Heals 20 health)": 3,
        "Cookies (4 AstroCoins) (Gives 8 energy)": 4,
        "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)": 6,
        "Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)": 12,
        "Energy Drink (9 AstroCoins)(Gives energy but it's random)": 9,
        "Cooked Beef (5 AstroCoins) (Gives 10 energy)": 5,
        "Cheese (2 AstroCoins) (Heals 10 health)": 2
    }
    typewriter_print("""

You see a trader! He has things in store for you! You can trade or not trade.

""", 0.08)
    sleep(1)
    while True:
        trade = input("Do you want to trade? Yes (y) or no (n): ").lower().rstrip()
        if trade == "n":
            print(divider)
            print("Okay, continuing your journey.")
            return energy, astrocoins, your_health
        elif trade == "y":
            done = "no"
            while done == "no":
                if astrocoins < shop_items_cost.get(shop_item1) and astrocoins < shop_items_cost.get(
                        shop_item2) and astrocoins < shop_items_cost.get(shop_item3):
                    print("You can't afford anything now, returning to your journey!")
                    return energy, astrocoins, your_health
                else:
                    print(divider)
                    print(f"You have {astrocoins} AstroCoins")
                    print(divider)
                    print(f"""
        The trader has these items: 
        {shop_item1}, 
        {shop_item2}, 
        and {shop_item3}
        """)
                    print(divider)
                    while True:
                        shopping = input("What do you want to buy? ").lower()
                        if shopping == "healing herbs":
                            if shop_item1 == "Healing Herbs (3 AstroCoins) (Heals 20 health)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Healing Herbs (3 AstroCoins) (Heals 20 health)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Healing Herbs (3 AstroCoins) (Heals 20 health)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Healing Herbs (3 AstroCoins) (Heals 20 health)") * how_much
                                        your_health += 20 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "cookies":
                            if shop_item1 == "Cookies (4 AstroCoins) (Gives 8 energy)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Cookies (4 AstroCoins) (Gives 8 energy)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Cookies (4 AstroCoins) (Gives 8 energy)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Cookies (4 AstroCoins) (Gives 8 energy)") * how_much
                                        energy += 8 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "sandwich":
                            if shop_item1 == "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                    elif shop_items_cost.get(
                                            "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Sandwich (6 AstroCoins) (Gives 6 energy and heals 12 health)") * how_much
                                        energy += 6 * how_much
                                        your_health += 12 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "super potion":
                            if shop_item2 == "Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Super Potion (12 AstroCoins) (Gives 10 energy and heals 25 health)") * how_much
                                        energy += 10 * how_much
                                        your_health += 25 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "energy drink":
                            if shop_item2 == "Energy Drink (9 AstroCoins)(Gives energy but it's random)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Energy Drink (9 AstroCoins)(Gives energy but it's random)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Energy Drink (9 AstroCoins)(Gives energy but it's random)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Energy Drink (9 AstroCoins)(Gives energy but it's random)") * how_much
                                        energy += randint(5, 20) * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "cooked beef":
                            if shop_item3 == "Cooked Beef (5 AstroCoins) (Gives 10 energy)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Cooked Beef (5 AstroCoins) (Gives 10 energy)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Cooked Beef (5 AstroCoins) (Gives 10 energy)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Cooked Beef (5 AstroCoins) (Gives 10 energy)") * how_much
                                        energy += 10 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        elif shopping == "cheese":
                            if shop_item3 == "Cheese (2 AstroCoins) (Heals 10 health)":
                                while True:
                                    how_much = int(input("How much do you want to buy? "))
                                    if shop_items_cost.get(
                                            "Cheese (2 AstroCoins) (Heals 10 health)") * how_much > astrocoins:
                                        print("You can't afford that.")
                                        continue
                                    elif shop_items_cost.get(
                                            "Cheese (2 AstroCoins) (Heals 10 health)") * how_much <= astrocoins:
                                        astrocoins -= shop_items_cost.get(
                                            "Cheese (2 AstroCoins) (Heals 10 health)") * how_much
                                        your_health += 10 * how_much
                                        print(
                                            f"You have {energy} energy, {your_health} health, and {astrocoins} AstroCoins now")
                                        while True:
                                            done = input("Are you done trading?(yes/no)").lower().rstrip()
                                            if done == "yes" or done == "no":
                                                break
                                            else:
                                                print("Please give a valid answer")
                                                continue
                                        break
                                    else:
                                        print("You gave an invalid answer (Please type a whole number)")
                                        continue
                            else:
                                print("That is not an item the trader has.")
                                continue
                            break
                        else:
                            print("That is not an item the trader has.")
                            done = "no"
            print("Returning to your journey!")
            return energy, astrocoins, your_health
        else:
            print("That is not an option.")
            continue

#The Wizard's Reward Scroll, gives you random rewards of health, astrocoins, or energy
#How to perform: energy, astrocoins, your_health = reward_scroll(energy, astrocoins, your_health)
def reward_scroll(energy, astrocoins, your_health):
    sleep(2)
    print(divider)
    print('''
    
You found a Reward Scroll!

''')
    print(divider)
    sleep(1.5)
    print("You will get a random amount of AstroCoins, Energy, or Health.")
    print(divider)
    sleep(1)
    what = choice(["AstroCoins", "Energy", "Health"])
    if what == "AstroCoins":
        print("You will get some AstroCoins...")
        sleep(2)
        how_much = randint(8,15)
        astrocoins += how_much
        print(divider)
        print(f"You got {how_much} AstroCoins!")
        print(divider)
        sleep(1)
        print(f"You have {astrocoins} AstroCoins, {energy} Energy, and {your_health} Health now.")
        return energy, astrocoins, your_health
    elif what == "Energy":
        print("You will get some Energy...")
        sleep(2)
        how_much = randint(8,15)
        energy += how_much
        print(divider)
        print(f"You got {how_much} Energy!")
        print(divider)
        sleep(1)
        print(f"You have {astrocoins} AstroCoins, {energy} Energy, and {your_health} Health now.")
        return energy, astrocoins, your_health
    else:
        print("You will get some Health...")
        sleep(2)
        how_much = randint(35,60)
        your_health += how_much
        print(divider)
        print(f"You got {how_much} Health!")
        print(divider)
        sleep(1)
        print(f"You have {astrocoins} AstroCoins, {energy} Energy, and {your_health} Health now.")
        return energy, astrocoins, your_health

#smaller battles
#hwo to perform: energy, your_health = minion(energy, your_health)
def minion(energy, your_health):
    print(divider)
    print("Prepare to fight...")
    enemyhealth = randint(150, 170)
    print(f"You have {your_health} health")
    while enemyhealth > 0:
        sleep(1)
        print(divider)
        print(f"You have {energy} energy")
        if whatclass == "hunter":
            print(f"Your attacks are {hunter}.")
        elif whatclass == "archer":
            print(f"Your attacks are {archer}.")
        elif whatclass == "wizard":
            print(f"Your attacks are {wizard}.")
        elif whatclass == "spearman":
            print(f"Your attacks are {spearman}.")
        elif whatclass == "bandit":
            print(f"Your attacks are {bandit}.")
        elif whatclass == "swordsman":
            print(f"Your attacks are {swordsman}.")
        elif whatclass == "dev":
            print(f"Your attacks are {dev}.")
        print(f"The enemy's health is {enemyhealth}")
        attack = input("What attack do you want to use? Or, do you want to defend for 3 energy (d)?: ").lower()
        if whatclass == "hunter":
            if attack == "rifle shot":
                if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle smack":
                if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "rifle headshot":
                if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "archer":
            if attack == "bow and arrow":
                if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow and arrow headshot":
                if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "bow smack":
                if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "arrow smack":
                if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "shotgun attack":
                if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "minigun attack":
                if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "wizard":
            if attack == "staff smack":
                if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "water spell":
                if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "fire spell":
                if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "electric spell":
                if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "slam against a wall spell":
                if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "meteor shower":
                if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "bandit":
            if attack == "dagger slash":
                if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "boomerang throw":
                if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "spearman":
            if attack == "spear stab":
                if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "spear swing":
                if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "swordsman":
            if attack == "sword stab":
                if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword slash":
                if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            elif attack == "sword poke":
                if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if whatclass == "dev":
            if attack == "ultimate laser":
                if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    if enemyhealth <= 0:
                        enemyhealth = 0
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                else:
                    print("You don't have enough energy points to battle! The enemy kills you.")
                    break
                    sys.exit("You die")
            else:
                print("Your class can't do that attack, you don't attack, the enemy attacks.")
                print(divider)
        if attack == "d":
            print("You defended! You gained 20 health!")
            your_health += 20
            energy -= 3

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You died.")
            print(divider)
            sys.exit("Game ended")
        elif enemyhealth <= 0:
            print(divider)
            print("You defeated the enemy! You gained some health and energy")
            print(divider)
            your_health += 110
            energy += 15
            print(f"You have {your_health} health and {energy} energy")
            break

        sleep(2)
        enemy_attack = randint(10, 70)
        if whatclass == "hunter":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "archer":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "wizard":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "spearman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "bandit":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "swordsman":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")
        elif whatclass == "dev":
            print(
                f"You have {your_health} health."
            )
            print(divider)
            print(f"The enemy dealed {enemy_attack} damage to you!")
            your_health -= enemy_attack
            if your_health <= 0:
                your_health = 0
            print(f"You have {your_health} health now.")

        if your_health <= 0:
            your_health = 0
            print(divider)
            print("You died.")
            print(divider)
            sys.exit("Game ended")

    return energy, your_health



event1(astrocoins, energy, your_health)
