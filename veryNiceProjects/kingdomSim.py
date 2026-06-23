from random import choice, randint
from time import sleep
from os import system

print("You have traveled to the world of Celestiaterra!\n")
print("You seek to become king!\n")
sleep(2)
print("You want create a kingodom of your own.\n")
sleep(1)


class Kingdom:
    def __init__(self, area, population, power, culture, food, age, disaster, threats, tax, money, happy):
        self.area = area
        self.population = population
        self.power = power
        self.culture = culture
        self.food = food
        self.age = age
        self.disaster = disaster
        self.threats = threats
        self.tax = tax
        self.money = money
        self.happy = happy

while True:
    area = input("""
What kingdom do you want to conquer?
The Plains (p)
The Mountains (m)
The Coast (c)

""").lower().strip()
    if area == "p":
        print(
            "You have chosen The Plains. The Plains give you an extra food boost but increases threats.\n"
        )
        sleep(2)
        land = Kingdom("Plains", 2, 0, 0, 10, 0, "None", 0, 0, 0, 100)
        break
    elif area == "m":
        print(
            "You have chosen The Mountains. The Mountains decreases threat but also decreases culture.\n"
        )
        sleep(2)
        land = Kingdom("Mountains", 2, 0, 0, 10, 0, "None", 0, 0, 0, 100)
        break
    elif area == "c":
        print(
            "You have chosen The Coast. The Coast gives you extra power but increases disasters.\n"
        )
        sleep(2)
        land = Kingdom("Coast", 2, 0, 0, 10, 0, "None", 0, 0, 0, 100)
        break
    else:
        print("That is not a valid area\n")

deaths = 0

event_yn = ["n", "n", "n", "n", "n", "n", "n", "n", "y", "n", "n", "n", "n", "n", "n"]
disaster = ["Earthquake", "Volcano", "Wildfire", "Wildfire", "Flash Flood", "Drought", "Drought", "Disease", "Earthquake", "Volcano", "Wildfire", "Wildfire", "Flash Flood", "Drought", "Drought", "Disease", "Earthquake", "Volcano", "Wildfire", "Wildfire", "Flash Flood", "Drought", "Drought", "Disease", "Earthquake", "Volcano", "Wildfire", "Wildfire", "Flash Flood", "Drought", "Drought", "Disease", "Earthquake", "Volcano", "Wildfire", "Wildfire", "Flash Flood", "Drought", "Drought", "Disease", "End of World"]
event_happening = "no"
disaster_time = 0

#Purchases:



#Disasters:
def earthquake():
    global deaths
    print("An earthquake has struck your kingdom!")
    if land.area == "Coast":
        deaths += 100
    else:
        deaths += randint(20,80)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def volcano():
    global deaths
    print("A volcano erupted in your kingdom!")
    if land.area == "Coast":
        deaths += 100
    else:
        deaths += randint(20,80)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def wildfire():
    global deaths
    print("Someone forgot to put out a fire! A wildfire has started in your kingdom!")
    if land.area == "Coast":
        deaths += 100
    else:
        deaths += randint(20,80)
    sleep(1)
    print("The wildfire has burnt down many crops.")
    land.food -= randint(10,30)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def flashflood():
    global deaths
    print("A flash flood occured in your kingdom!")
    if land.area == "Coast":
        print("Your kingdom was on the coast . . . it was greatly effected.")
        deaths += 120
    else:
        deaths += randint(20,80)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def drought():
    global deaths
    print("The priests did not pray to the rain god enough and a drought has started in your kingdom!")
    if land.area == "Coast":
        deaths += 100
    else:
        deaths += randint(20,80)
    sleep(1)
    print("The crops started to dry.")
    land.food -= randint(10,30)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def disease():
    global deaths
    print("A plague doctor has BROUGHT a plague to our kingdom! Never trusting them again...")
    if land.area == "Coast":
        deaths += 120
    else:
        deaths += randint(50,100)
    sleep(1)
    print(f"There has been {deaths} deaths :(\n")

def end_of_world():
    global deaths
    print("It's the end of the world! This should be pretty self explanatory >:)\n")
    sleep(1)
    print("bye byee, truly unfortunate\n")
    sleep(1)
    end()

# Invasions:

# def invasion():
#     global deaths
#     if land.area == "Coast":
#         deaths += 100
#     else:
#         deaths += randint(20,80)
#     sleep(1)
#     print(f"There has been {deaths} deaths :(\n")

def end():
    land.population = 0

while land.population > 0:
    system("clear")

    #age increases
    land.age += 1

    #population increases
    if land.culture <= 5:
        land.population += 1
    elif land.culture > 5 and land.culture <= 10:
        land.population += 2
    elif land.culture > 10 and land.culture <= 25:
        land.population += randint(1, 5)
    elif land.culture > 25 and land.culture <= 50:
        land.population += randint(2, 8)
    elif land.culture > 50 and land.culture <= 90:
        land.population += randint(3, 12)
    elif land.culture > 90 and land.culture <= 150:
        land.population += randint(7, 20)
    elif land.culture > 150 and land.culture <= 220:
        land.population += randint(10, 30)
    elif land.culture > 220:
        land.population += randint(12, 50)

    #death rate
    if land.population <= 5:
        deaths = 0
    elif land.population > 5 and land.population <= 10:
        deaths = 1
    elif land.population > 10 and land.population <= 25:
        deaths = randint(1, 2)
    elif land.population > 25 and land.population <= 50:
        deaths = randint(1, 3)
    elif land.population > 50 and land.population <= 90:
        deaths = 3
    elif land.population > 90 and land.population <= 150:
        deaths = 4
    elif land.population > 150 and land.population <= 220:
        deaths = randint(3, 8)
    elif land.population > 220:
        deaths = randint(6, 12)

    #if food depleats
    if land.food < land.population:
        land.population -= land.population // 10
    land.population -= deaths

    #culture increases
    if land.population <= 5:
        land.culture += 1
    elif land.population > 5 and land.population <= 10:
        land.culture += 2
    elif land.population > 10 and land.population <= 25:
        land.culture += randint(1, 5)
    elif land.population > 25 and land.population <= 50:
        land.culture += randint(2, 7)
    elif land.population > 50 and land.population <= 90:
        land.culture += randint(3, 8)
    elif land.population > 90 and land.population <= 150:
        land.culture += randint(4, 9)
    elif land.population > 150 and land.population <= 220:
        land.culture += randint(5, 10)
    elif land.population > 220:
        land.culture += randint(6, 12)

    #no happiness
    if land.happy <= 0:
        end()

    #power increases
    if land.population <= 5:
        land.power = 5
    elif land.population > 5 and land.population <= 10:
        land.power = randint(5, 10)
    elif land.population > 10 and land.population <= 25:
        land.power = randint(10, 15)
    elif land.population > 25 and land.population <= 50:
        land.power = randint(15, 20)
    elif land.population > 50 and land.population <= 90:
        land.power = randint(20, 30)
    elif land.population > 90 and land.population <= 150:
        land.power = randint(35, 60)
    elif land.population > 150 and land.population <= 220:
        land.power = randint(70, 90)
    elif land.population > 220:
        land.power = randint(90, 100)

    #food production and food eating
    if land.population <= 5:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 5 and land.population <= 10:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 10 and land.population <= 25:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 25 and land.population <= 50:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 50 and land.population <= 90:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 90 and land.population <= 150:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 150 and land.population <= 220:
        land.food += land.population // 3
        land.food -= land.population // 4
    elif land.population > 220:
        land.food += land.population // 3
        land.food -= land.population // 4

    #threats
    if land.power <= 12:
        if land.age <= 30:
            land.threats = randint(1, 15)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(12, 35)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(60, 100)
    elif land.power > 12 and land.power <= 24:
        if land.age <= 30:
            land.threats = randint(1, 8)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(7, 28)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(35, 90)
    elif land.power > 24 and land.power <= 36:
        if land.age <= 30:
            land.threats = randint(1, 7)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(5, 20)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(20, 78)
    elif land.power > 36 and land.power <= 48:
        if land.age <= 30:
            land.threats = randint(1, 6)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(4, 17)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(17, 67)
    elif land.power > 48 and land.power <= 60:
        if land.age <= 30:
            land.threats = randint(1, 5)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(4, 15)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(16, 50)
    elif land.power > 60 and land.power <= 75:
        if land.age <= 30:
            land.threats = randint(1, 4)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(3, 12)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(8, 25)
    elif land.power > 75 and land.power <= 89:
        if land.age <= 30:
            land.threats = randint(1, 3)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(2, 8)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(3, 10)
    elif land.power > 89 and land.power <= 100:
        if land.age <= 30:
            land.threats = randint(1, 2)
        elif land.age > 30 and land.age <= 80:
            land.threats = randint(1, 3)
        elif land.age > 80 and land.age <= 150:
            land.threats = randint(1, 7)

    #inc in money
    land.money += land.tax * land.population

    
    #EVENTS HERE:
    #------------------------------
    if disaster_time == 10:
        land.disaster = "None"
        event_happening = "no"
        disaster_time = 0
        
    if event_happening == "no":
        event_yn_c = choice(event_yn)
        if event_yn_c == "n":
            pass
        elif event_yn_c == "y":
            event_happening = "yes"
            sleep(2)
            print("An event is occuring!\n")
            sleep(1)
            occuring_event = choice(disaster)
            land.disaster = occuring_event
            if occuring_event == "Earthquake":
                earthquake()
            elif occuring_event == "Volcano":
                volcano()
            elif occuring_event == "Wildfire":
                wildfire()
            elif occuring_event == "Flash Flood":
                flashflood()
            elif occuring_event == "Drought":
                drought()
            elif occuring_event == "Disease":
                disease()
            elif occuring_event == "End of World":
                end_of_world()
        else:
            print("How did this even happen")
    elif event_happening == "yes":
        disaster_time += 1
        #event details start here

    print(f"""

Kingdom Stats:
---------------------------

Area = [ {land.area} ]
----------
Population = [ {land.population} ]
The higher the population: 
The more power, better culture, and more food produced
----------
Power = [ {land.power} ]
You need power to conquer lands and prevent invasions
----------
Culture = [ {land.culture} ]
The better the culture, the more people will come to your Kingdom
----------
Happiness = [ {land.happy}% ]
Make sure this is above 0%
----------
Food = [ {land.food} ]
You need enough food to sustain your growing population
If the kingdom runs out of food, the population will decrease really fast
----------
Age = [ {land.age} Years ]
Increases every year
----------
Current Disasters = [ {land.disaster} ]
Disasters will slowly or quickly decrease the population
----------
Threat Level = [ {land.threats}% ]
The threat level shows the chances you will be invaded
The max is 100%
The lower the threat level, the better
----------
The tax right now is = [ {land.tax} ]
The more tax, the more money.
But, it will decrease happiness since people would be unhappy.
----------
Your current money = [ {land.money} ]
Use money to upgrade stats
----------
There were {deaths} deaths this year

You can also change the tax by pressing (t)
Or you can use your money (m)

""")
    next = input("Press Enter To Continue or do something\n").lower().strip()
    if next == "stop":
        land.population = 0
    elif next == "t":
        print("You are changing your tax level")
        change_t  = int(input("What do you want to change the tax level to? "))
        land.tax = change_t
        land.happy = 100 - change_t*10
    elif next == "m":
        print("You are using your money")
        use = input("Would you want to buy power (p) or food (f)").lower().strip()
        if use == "p":
            amnt = int(input("How much would you want to invest? "))
            if land.money - amnt >= 0:
                land.money -= amnt
                land.power += amnt // 3
                print("Transaction sucessful!")
                sleep(2)
            else:
                print("You don't have enough money.")
                sleep(2)
        elif use == "f":
            amnt = int(input("How much would you want to invest? "))
            if land.money - amnt >= 0:
                land.money -= amnt
                land.food += amnt // 2
                print("Transaction sucessful!")
                sleep(2)
            else:
                print("You don't have enough money.")
                sleep(2)
    
        
print("-----------------") 
print("\nSomething happened...")
sleep(3)
print("\nYour kingdom has perished. :(")
print(f"""

Your kingdom has survived for {land.age} years.

""")


#---------------------------
sleep(2)
if land.age > 1 and land.age <= 70:
    print("Your kingdom didn't do such a great job... Try using a different strategy next time.")
elif land.age > 70 and land.age <= 170:
    print("Your kingdom did an okay job! There may be better strategies to make your kingdom survive longer but yours is already pretty decent!")
elif land.age > 170 and land.age <= 270:
    print("Your kingdom was awesome! This kingdom would be written down in history.")
    file = open("top_scores.txt", "a+")
    file.write(str(land.age) + "\n")
    file.close()
elif land.age > 270 and land.age <= 300:
    print("This is one of the few kingdoms to survive for this long! What a magnificently long rule this kingdom had.")
    file = open("top_scores.txt", "a+")
    file.write(str(land.age) + "\n")
    file.close()
elif land.age > 300:
    print("I don't even know what to say! Your kingdom has done a superb job. The kingdom had a long a prosperous rule.")
    file = open("top_scores.txt", "a+")
    file.write(str(land.age) + "\n")
    file.close()