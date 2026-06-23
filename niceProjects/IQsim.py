from time import sleep


divider = "--------------------------------\n"
iq = 0

def car():
    global iq


    def punch():
        global iq
        sleep(2)
        print("You punch the car!")
        print(divider)
        sleep(2)
        print("Bam bam bam!")
        print(divider)
        sleep(1.5)
        print("Car starts beeping alarm")
        print(divider)
        sleep(2)
        iq += 1
        print("You gained 1 IQ!")
        print(divider)

    def kick():
        global iq
        sleep(2)
        print("You kicked the car!")
        print(divider)
        sleep(2)
        print("Boom boom boom!")
        print(divider)
        sleep(1.5)
        print("Neighbor yells: CAR VANDALIZER!")
        print(divider)
        sleep(2)
        iq += 1.5
        print("You gained 1.5 IQ!")
        print(divider)
        
    def jump():
        global iq
        sleep(2)
        print("You try to jump over the car!")
        print(divider)
        sleep(2)
        print("Boing!")
        print(divider)
        sleep(1.5)
        print("You accidentally trip at the top at bang your face.")
        print(divider)
        sleep(2)
        iq += 2
        print("You gained 2 IQ!")
        print(divider)

    def ask():
        global iq
        sleep(2)
        print("You try to ask the car to move.")
        print(divider)
        sleep(2)
        print("Hello car? Can yo uplease move out of the way so I can get past?")
        print(divider)
        sleep(2)
        print("You stand there for 1 hour and finally realize cars can't talk")
        print(divider)
        sleep(2)
        iq += 2.5
        print("You gained 2.5 IQ!")
        print(divider)
    
    def disguise():
        global iq
        sleep(2)
        print("You disguise as a theif and try to sneak into the car")
        print(divider)
        sleep(2)
        print("Person: AHHHH CAR THEIF! I'm calling 911!")
        print(divider)
        sleep(2)
        print("The police come and arrest you.")
        print(divider)
        sleep(2)
        iq += 3
        print("You gained 3 IQ!")
        print(divider)        

    def stare():
        global iq
        sleep(2)
        print("You stare at a tree")
        print(divider)
        sleep(2)
        print("The tree doesn't do anything")
        print(divider)
        sleep(2)
        print("You fall asleep")
        print(divider)
        sleep(2)
        iq += 3.5
        print("You gained 3.5 IQ!")
        print(divider)          

    def explode():
        global iq
        sleep(2)
        print("You get a bomb in thin air")
        print(divider)
        sleep(2)
        print("You place the bomb on the car")
        print(divider)
        sleep(2)
        print("You forgot the lighter...")
        print(divider)
        sleep(2)
        iq += 4
        print("You gained 4 IQ!")
        print(divider)

    def oreo():
        global iq
        sleep(2)
        print("You somehow turn into a oreo")
        print(divider)
        sleep(2)
        print("You roll to the car")
        print(divider)
        sleep(2)
        print("Someone: OH WOW FREE OREO!!! *Eats you*")
        print(divider)
        sleep(2)
        iq += 4.5
        print("You gained 4.5 IQ! even though you aren't alive anymore...")
        print(divider)

    def final():
        global iq
        sleep(2)
        print("You finally realized you can walk around the car")
        print(divider)
        sleep(2)
        print("You accidentally fall down a drain")
        print(divider)
        sleep(2)
        print("You: Well, I got past the car!")
        print(divider)
        sleep(2)
        print("You passed the car stage!!!")
        print(divider)

    def insta_win():
        global iq
        sleep(2)
        print("You won...um...how?")
        iq += 10000000000000000000
    sleep(2)
    print("You have to get past a car in the road! Note: Newest things to do give the most IQ!")
    print(divider)
    while iq < 5:
        while True:
            print(f"You have {iq} IQ")
            option = input("""
            
Pick a thing to do:
1. Punch the car

""").lower().strip()
            if option == "1":
                punch()
                break
            else:
                continue
    while iq < 14:
        while True:
            print(f"You have {iq} IQ")
            option = input("""
            
Pick a thing to do:
1. Punch the car
2. Kick the car

""").lower().strip()
            if option == "1":
                punch()
                break
            elif option == "2":
                kick()
                break
            else:
                continue
    while iq < 22:
        while True:
            print(f"You have {iq} IQ")
            option = input("""
            
Pick a thing to do:
1. Punch the car
2. Kick the car
3. Jump over

""").lower().strip()
            if option == "1":
                punch()
                break
            elif option == "2":
                kick()
                break
            elif option == "3":
                jump()
                break
            else:
                continue
    while iq < 35:
        while True:
            print(f"You have {iq} IQ")
            option = input("""
            
Pick a thing to do:
1. Punch the car
2. Kick the car
3. Jump over
4. Ask

""").lower().strip()
            if option == "1":
                punch()
                break
            elif option == "2":
                kick()
                break
            elif option == "3":
                jump()
                break
            elif option == "4":
                ask()
                break
            else:
                continue









print("Welcome to the IQ Simulator!")
print(divider)
sleep(2)
print("Please select a stage: ")
print(divider)
while True:
    stage = input(print("""

(a) Car

""")).lower().strip()
    if stage == "a":
        car()
    else:
        print("Please select a valid stage.")
        sleep(1)
