from random import randint, choice
from time import sleep

def typewriter_print(text, interval):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(interval)
    print("\n")

divider = "-----------------------------------\n"

health = 100
hunger = 100
players = 20
day = 0
events_health = ["snake", "fire", "bees", "water", "player", "healing herb", "rest", "magic", "tofu"]
events_hunger = ["robber", "burnt", "rotten", "sick", "apples", "kind player", "potatoes", "roast animal", "fish"]

# All health decreasing or adding functions

def snake():
    global health
    global hunger
    print(divider)
    typewriter_print("Ssssss! A snake jumps out from a bush and bites your leg.", 0.08)
    sleep(1.5)
    typewriter_print("You lie half-conscious on the floor of the forest.", 0.08)
    sleep(1.5)
    print("-20 health")
    health -= 20

def fire():
    global health
    global hunger
    print(divider)
    typewriter_print("You were trying to light a fire to cook your dinner.", 0.08)
    sleep(1.5)
    typewriter_print("You accidentally catch a dry stick next to you on fire and light yourself up.", 0.08)
    sleep(1.5)
    print("-10 health")
    health -= 10

def bees():
    global health
    global hunger
    print(divider)
    typewriter_print("You want to get honey from a beehive on a tree (why)", 0.08)
    sleep(1.5)
    typewriter_print("You accidentally shake the branch too hard and the bees become hostile.", 0.08)
    sleep(1.5)
    print("-15 health")
    health -= 15

def water():
    global health
    global hunger
    print(divider)
    typewriter_print("You want to fish in the river on a raft", 0.08)
    sleep(1.5)
    typewriter_print("The raft breaks and you fall in the river", 0.08)
    sleep(1.5)
    print("-10 health, but +5 hunger (yay?)")
    health -= 10
    hunger += 5

def player():
    global health
    global hunger
    print(divider)
    typewriter_print("You meet a player in the woods.", 0.08)
    sleep(1.5)
    typewriter_print("You get beaten up and tied to a rock", 0.08)
    sleep(1.5)
    print("-10 health")
    health -= 10





def healing_herbs():
    global health
    global hunger
    print(divider)
    typewriter_print("You find some grass on the floor", 0.08)
    sleep(1.5)
    typewriter_print("You find out they are healing herbs!", 0.08)
    sleep(1.5)
    print("+15 health")
    health += 15

def rest():
    global health
    global hunger
    print(divider)
    typewriter_print("You get an anouncement that everyone gets a break for a day.", 0.08)
    sleep(1.5)
    typewriter_print("You sleep and rest", 0.08)
    sleep(1.5)
    print("+10 health")
    health += 10

def magic():
    global health
    global hunger
    print(divider)
    typewriter_print("You are walking in the mountains.", 0.08)
    sleep(1.5)
    typewriter_print("You find a magic scroll and you open it and suddenly get healed with magic!", 0.08)
    sleep(1.5)
    print("+20 health")
    health += 20

def tofu():
    global health
    global hunger
    print(divider)
    typewriter_print("You find tofu in the desert", 0.08)
    sleep(1.5)
    typewriter_print("You eat it.", 0.08)
    sleep(1.5)
    print("+10 health, -10 hunger")
    health += 10
    hunger -= 10


# All hunger decreasing or adding functions


def robber():
    global health
    global hunger
    print(divider)
    typewriter_print("Another player comes and takes some of your food while you were sleeping!", 0.08)
    sleep(1.5)
    typewriter_print("You starve for that day.", 0.08)
    sleep(1.5)
    print("-10 hunger")
    hunger -= 10

def burnt():
    global health
    global hunger
    print(divider)
    typewriter_print("You find a black burnt thingy on the ground.", 0.08)
    sleep(3)
    typewriter_print("You eat it", 0.08)
    sleep(1.5)
    print("-20 hunger")
    hunger -= 20

def rotten():
    global health
    global hunger
    print(divider)
    typewriter_print("You find a dead rabbit on the floor.", 0.08)
    sleep(3)
    typewriter_print("You eat it", 0.08)
    sleep(1.5)
    print("-15 hunger")
    hunger -= 15

def sick():
    global health
    global hunger
    print(divider)
    typewriter_print("You accidentally ate an ant.", 0.08)
    sleep(1.5)
    typewriter_print("You suddenly feel sick.", 0.08)
    sleep(1.5)
    print("-10 hunger")
    hunger -= 10





def apples():
    global health
    global hunger
    print(divider)
    typewriter_print("You find a apple tree!", 0.08)
    sleep(1.5)
    typewriter_print("You climb up and pick some apples to eat", 0.08)
    sleep(1.5)
    print("+10 hunger")
    hunger += 10

def kind_player():
    global health
    global hunger
    print(divider)
    typewriter_print("You meet a player in the woods.", 0.08)
    sleep(1.5)
    typewriter_print("They see you and is sad for you so they give you a cookie", 0.08)
    sleep(1.5)
    print("+15 hunger")
    hunger += 15

def potatoes():
    global health
    global hunger
    print(divider)
    typewriter_print("You see a brown thing in the dirt.", 0.08)
    sleep(1.5)
    typewriter_print("You dig it up and find a lot of potatoes!", 0.08)
    sleep(1.5)
    print("+5 hunger")
    hunger += 5


def roast_animal():
    global health
    global hunger
    print(divider)
    typewriter_print("You see a dead animal not far away.", 0.08)
    sleep(1.5)
    typewriter_print("You see that it is somehow already roasted and ready to eat!", 0.08)
    sleep(1.5)
    print("+20 hunger")
    hunger += 20


def fish():
    global health
    global hunger
    print(divider)
    typewriter_print("You want to make a raft and get fish in the river (why)", 0.08)
    sleep(1.5)
    typewriter_print("You successfully get an entire bucket of fish!", 0.08)
    sleep(1.5)
    print("+10 hunger")
    hunger += 10


typewriter_print("Speaker: Hello, welcome to the Surival Games! Survive the longest in harsh inviornments to win. Only one shall remain.", 0.08)
while True:
    print(divider)
    sleep(2)
    day += 1
    hunger -= randint(1, 20)
    health -= randint(1, 15)
    players -= randint(1,4)
    print(f"It is day {day}")
    print(divider)
    sleep(1)
    if health <= 0:
        print("You have 0 health, you die.")
        exit("Game over")
    if hunger <= 0:
        print("You starved to death.")
        exit("Game over")
    
    if players <= 0:
        print("You have won the games! You are the only one left.")
        exit("You win!")
    else:
        print(f"There are {players} left")
        print(divider)
        sleep(1.5)

    print(f"You have {health} health and {hunger} hunger.")
    print(divider)
    sleep(2)
    while True:
        decision = input("Would you like to: find food (1) | explore (2) | or pass (3) ").strip()
        if decision == "1":
            sleep(1)
            to_do = choice(events_hunger)
            break
        elif decision == "2":
            sleep(1)
            to_do = choice(events_health)
            break
        elif decision == "3":
            sleep(1)
            break

try:
    test = int(input("What is 1 + 1: "))

except ValueError:
    print("Give a valid integer")

else:
    print("done")

finally:
    print("execution complete")
    
