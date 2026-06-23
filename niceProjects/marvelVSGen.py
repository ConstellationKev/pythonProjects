from random import randint, choice
from time import sleep
characters = ["Captain Amercia", "Hulk", "Hawkeye", "Iron Man", "Wong", "Ancient One", "Spider Man", "Doctor Strange", "Ant Man", "Vision", "Nick Fury (eye patch man)", "purple raisin chin", "Thor", "Dormammu", "Shang-Chi", "Happy", "Black Panther", "Scarlet Witch", "Captian Marvel", "Sleep person", "Tree man", "Raccoon", "Odin", "Loki", "Falcon"]
divider = "-----------------------------------"
print("This is the Random Marvel Battle Generator!")
sleep(2)
print(divider)
while True:
    choice_made = input("Do you want to do 2 teams (1) or 3 teams (2) or 4 teams (3) or EVERYONE (4) ").rstrip()
    if choice_made == "1":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_one_number = str(randint(1,50))
        person_two_number = str(randint(1,50))
        sleep(2)
        print(divider)
        print(f"{person_one_number} {person_one}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two_number} {person_two}!!!")
        break
    elif choice_made == "2":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_three = choice(characters) 
        person_one_number = str(randint(1,50))
        person_two_number = str(randint(1,50))
        person_three_number = str(randint(1,50))
        sleep(2)
        print(divider)
        print(f"{person_one_number} {person_one}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two_number} {person_two}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_three_number} {person_three}!!!")
        break
    elif choice_made == "3":
        print("WHO WOULD WIN...")
        person_one = choice(characters)
        person_two = choice(characters)
        person_three = choice(characters) 
        person_four = choice(characters)
        person_one_number = str(randint(1,50))
        person_two_number = str(randint(1,50))
        person_three_number = str(randint(1,50))
        person_four_number = str(randint(1,50))
        sleep(2)
        print(divider)
        print(f"{person_one_number} {person_one}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_two_number} {person_two}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_three_number} {person_three}...")
        sleep(1)
        print("VS")
        sleep(3)
        print(f"{person_four_number} {person_four}!!!")
        break
    elif choice_made == "4":
        print("WHO WOULD WIN...")
        sleep(2)
        print(divider)
        for character in characters:
            number = randint(1,50)
            print(f"{number} {character}")
            sleep(0.5)
            print("VS")
            sleep(1.5)
        break
    else:
        print("You gave an invalid answer.")
        continue
