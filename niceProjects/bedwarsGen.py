from random import choice
from time import sleep
characters = ["None", "Aery", "Archer", "Ares", "Axolotl Amy", "Baker", "Alchemist", "Barbarian", "Beekeeper", "Bounty Hunter", "Builder", "Eldertree", "Farmer Cletus", "Fisherman", "Freiya", "Frosty", "Gingerbread Man", "Gomphy", "Grim Reaper", "Infernal Sheilder", "Jack", "Jade", "Lassy", "Melody", "Miner", "Pirate Davey", "Pyro", "Raven", "Santa", "Spirit Catcher", "Smoke", "Trapper", "Trinity", "Vanessa", "Void Regent", "Vulcan", "Wizard", "Warrior", "Yeti", "Yuzi"]
armor = ["Leather Armor", "Leather Armor", "Leather Armor", "Leather Armor", "Iron Armor", "Iron Armor", "Iron Armor", "Iron Armor", "Diamond Armor", "Diamond Armor", "Diamond Armor", "Diamond Armor", "Emerald Armor",  "Emerald Armor", "Warrior Armor", "Warrior Armor", "Void Armor"]
swords = ["Wooden Sword", "Wooden Sword", "Wooden Sword", "Wooden Sword", "Iron Sword", "Iron Sword", "Iron Sword", "Iron Sword", "Diamond Sword", "Diamond Sword", "Diamond Sword", "Diamond Sword", "Emerald Sword", "Emerald Sword", "Emerald Sword", "Freiya Sword", "Scythe", "Rageblade", "Twirlblade"]
divider = "-----------------------------------"
print("This is the Random BedWars Battle Generator!")
sleep(2)
print(divider)
while True:
    choice_made = input("Do you want to do 2 teams (1) or 3 teams (2) or 4 teams (3) or EVERYONE (4) ").rstrip()
    if choice_made == "1":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_one_armor = choice(armor)
        person_two_armor = choice(armor)
        person_one_sword = choice(swords)
        person_two_sword = choice(swords)

        sleep(2)
        print(divider)
        print(f"{person_one} with {person_one_armor} and {person_one_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two} with {person_two_armor} and {person_two_sword}!!!")
        break
    elif choice_made == "2":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_three = choice(characters)
        person_one_armor = choice(armor)
        person_two_armor = choice(armor)
        person_three_armor = choice(armor)
        person_one_sword = choice(swords)
        person_two_sword = choice(swords)
        person_three_sword = choice(swords)

        sleep(2)
        print(divider)
        print(f"{person_one} with {person_one_armor} and {person_one_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two} with {person_two_armor} and {person_two_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_three} with {person_three_armor} and {person_three_sword}!!!")
        break
    elif choice_made == "3":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_three = choice(characters) 
        person_four = choice(characters)
        person_one_armor = choice(armor)
        person_two_armor = choice(armor)
        person_three_armor = choice(armor)
        person_four_armor = choice(armor)
        person_one_sword = choice(swords)
        person_two_sword = choice(swords)
        person_three_sword = choice(swords)
        person_four_sword = choice(swords)

        sleep(2)
        print(divider)
        print(f"{person_one} with {person_one_armor} and {person_one_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two} with {person_two_armor} and {person_two_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_three} with {person_three_armor} and {person_three_sword}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_four} with {person_four_armor} and {person_four_sword}!!!")
        break
    elif choice_made == "4":
        print("WHO WOULD WIN...")
        sleep(2)
        print(divider)
        for character in characters:
            person_armor = choice(armor)
            person_sword = choice(swords)
            print(f"{character} with {person_armor} and {person_sword}")
            sleep(0.2)
            print("VS")
            sleep(1)
        break
    else:
        print("You gave an invalid answer.")
        continue