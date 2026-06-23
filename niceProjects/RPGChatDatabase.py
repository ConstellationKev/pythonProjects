from random import randint, choice

print("Greetings, I'm Constellation. Welcome to the Role Playing Game Chat Database!")
divider = "----------------------------------------"
print(divider)
def what_to_do():
    whattodo = input(
        "What do you want to do?(Classes/Adventure game(STILL BEING CODED)): ").lower(
        ).rstrip()
    return whattodo
whattodo = what_to_do()
if whattodo == "classes":
    doneornot = "no"
    while doneornot == "no":
        print(divider)
        character = input(
            "What character or class do you want to explore?(Press enter to continue): "
        ).lower()
        print(divider)
        if character == "random":
            character = choice(["hunter", "bandit", "archer", "wizard", "spearman", "shieldman", "swordsman", "healer", "pizza man", "dual wielder", "stalker" "chef", "astronaut", "assassin", "bloodmage", "ninja", "special"])
        if character == "hunter":
            print("""Hunter: Uses a rifle

      Season 1 class

    Stats: Good aim and attack power, through charged attacks. If lands headshot, extra damage is done.

    Skins: Military, Bush Camo Outfit (craftable from twigs, leaves, sticks, mud, etc), and Spy.

    Weapon: Rifle, deals 40 health damage on body shots, 100 to 90 health on headshots. Bullet (craftable made from rock, obsidian, stone, pebble, etc anything rock.)
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "archer":
            print("""Archer: Uses bow and arrows

    Season 1 class

    Stats: Ranged attacker. Can attack air enemies. Can do “shotgun” attacks (Multiple arrows) Or “minigun attacks” depending on firerate. Needs arrows in order to attack. Run out of arrows and its melee.

    Skins: Camo, Armor, Spy

    Special Ability: Arrow Rain. Requires loads of arrows. Can wear double quivers and use double bows.

    Arrows: Maximum amount of arrows in quiver: 100 to 150 arrows as you expand storage.

    Damage: 25 damage for bodyshots. and 85 to 100 damage for headshots. Using arrows as melee deals 8 damage per strike. 75 to 100 for headstrike.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "bandit":
            print("""Bandit: Dagger or boomerang
    
    Season 1 class

    Stats/Abilities: Steals loot to use and sell. Melee attacker can attack multiple enemies when throws a dagger like a boomerang.

    Passive Ability: 20% more chance of getting rare rarity loot.

    Skin: Thief, Adventurer, ??? (Special skin), Wild West Cowboy.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "wizard":
            print("""Wizard: Staff or book
    
    Season 1 class

    Stats/Abilities: Uses powerful spells can vary from ranged to close to charged attacks. Uses mana.

    Passive Ability: Can make teammate weapons magical like fire, electricity, ice, etc. Uses more mana, the stronger it is.

    Skins: Galaxy, evil witch, angel.

    Special ability: Meteor rain. Uses All the mana they have to summon a powerful meteor shower, that all have special effects. REQUIRES TO BE LEVEL 50 BECAUSE VERY POWERFUL.

    Meteor effects: Dazed/confused. Extra damage. Raises ally stats. Lowers enemy stats. Burn damage, electric damage, freeze damage, etc.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "spearman":
            print("""Spearman: Spear
    
    Season 1 class

    Stats: Ranged melee, pierces through shields, can do extra damage with the tip.

    Passive: Can deal more damage, the more critical items you have equipped.

    Special ability: Spear Cyclone At 50% health, gains rage mode and starts spinning with the spear, increasing all ally attacks by 10%, gains a 25% damage boost for itself, and can harm multiple enemies with a high rate.

    Skins: Jungleman, juggernaut. (For juggernaut, it's actually an advanced class. Reason why skin is here is because you need to use juggernaut spearman skin for juggernaut. In order to get the actual class, deal 500000 damage and tank 100000 damage.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "shieldman":
            print("""Shieldman: Shield
    
    Season 1 class

    Stats: Uses a moderate shield. Can raise defense for all allies, and tanks damage through the shield.

    Passive: Gains a 15% defense buff when at 30% health, for 2 turns per battle.

    Skins: Royal defender

    Special ability: Makes a huge forcefield that can cover a lot of people and is there for 30 seconds and requires level 20.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "swordsman":
            print("""Swordsman: Sword or lance
      
    Season 1 class

    Stats: Uses a powerful sword, can use multiple abilities, like spin slash and double slash (totally didn't use miitopia for that idea hahahahaha).

    Passive: If a teammate is at low health, guard them with their sword at all costs.

    Skins: Demon, Royal guard

    Special ability: 3 golden swords appear and fly toward where the sword is pointed. Each sword does 75 damage. Requires level 25.

    Swordsman evolution: Dual Wielder.
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "healer":
            print("""Healer: Medkit or staff
      
    Season 1 class

    Stats: Can heal people using medkit and staff, 230 health. Also what is a healing shield that sounds too weird is for magical healing. Also healer can buff peeps.

    Special ability: Can use healing force field
    """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "pizza man":
            print("""Pizza Man: Rides a motercycle and has a huge rolling pin and pizza slicer
            
Season 2 INTERMEDIATE CLASSES

Stats: High attack, can attack at a high rate. Can also thorw rolling pin for a lot of damage but loses it forever, good for endgames when it is a 1v1 fight.

Special ability: Rolling pin turns large and rolls over enemy, dealing a lot of damage then using a pizza slicer, he slices the enemy.""")
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "dual wielder":
            print(
                """Dual wielder: Duel wields any common weapons, like: Swords, Axes, Staffs, Bows, Shields, or Daggers.

  Season 2 INTERMEDIATE CLASSES

  Stats: High attack or defense, depending on weapon. Ranged weapons are not very helpful for a dual wielder, and same with staffs.

  Passive ability: Can dual wield any weapon from the above without having it to be the same. For example, Axe and Dagger.

  Special ability: Throws out an all out attack with all the weapons they have.

  Skins: Mystery, ??? Idk, please list some.
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "stalker":
            print("""Stalker: Uses somewhat magical knives that can duplicate.

  Season 2 INTERMEDIATE CLASSES

  Stats: Can go invisible for a turn, and cannot be able to go invisible after 3 turns, you can attack while invisible. Can throw knives, and make enemies bleed, and dizzy. (THIS IS A TECH CLASS, MEANING IT IS A DISTURBING CLASS, NOT SUPPORT OR DPS.)

  Passive: At 25% health or below, you heal 25% more health back. (Only happens once a battle.) Also increases speed and damage.

  Special/Ultimate: Freezes time for a second and attacks enemies 10 times before they can blink.

  Skins: 1880s, Mystery,

  Stalker evolution: Can turn into Ninja class, or Assassin.
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "chef":
            print("""Chef: Pots and Pans

  Season 2 INTERMEDIATE CLASSES

  Stats: Uses Pots and pans as a weapon. Can heal allies with food. Can use knives as well, to cut enemies up into soup. Cooks soup to feed allies, buffing them or healing them. Bakes allies food to buff them. When attacking enemies, use a pan and whack them in the head, dealing a decent amount of damage, may cause them to be stunned for a turn.

  Passive: Gives allies 10% crit chance, and gives self a 20% boost.

  Ultimate: Puts literally everything in a pot, and depending on how much inside of it, the more damage it does, healing allies as well. Conflicts burn damage to enemies.

  Skins: Murderer, Gorden Ramsey, Robot chef
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "astronaut":
            print(
                """Astronaut: No weapons: Only a bag that has random infinite items.

  Season 2 INTERMEDIATE CLASSES

  Stats: In the bag, there are many random things for fight, not a DPS class, but a support. Can add items onto weapons to make them stronger.

  Passive: Troll: Commits lol on enemies and makes them have less defense at the start of battle for 2 turns.
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "assassin":
            print(
                """Assassin: Literally the maxed version of Stalker and Bandit. Not much to explain here, except the new stuff added.

  Season 3: ADVANCED CLASSES 

  Stats: More damage, a DPS class, lots of speed, can attack TWICE! Can stack damage by sharpening knives/daggers.

  Passive: Pretty much every passive before this from Stalker and Bandit, but can lock targets with one enemy and gets more loot.

  Ultimate: Pickpockets every enemy, then strikes them with a whirlwind, knocking them against a random wall PERFECTLY, then slices all of them in one swing.

  THIS IS THE FINAL STAGE OF BANDIT AND STALKER, OTHER THAN NINJA, WHICH IS ANOTHER CLASS YOU CAN CHOOSE FROM STALKER.
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "ninja":
            print("""Ninja: Grenades, knives, and katanas

  Season 3: ADVANCED CLASSES

  Stats: Pretty much stalker as well, but a bit different. Unlock grenades in shops, gain loads of agility/speed, and do more damage the more agility/speed you have. This is a tech class. Can attack twice as well.

  Passive: Every turn, you can counter an attack you spot that's very strong, but take damage yourself as well.

  Ultimate: Bounty for a monster comes up, you then target the monster bounty, and instantly kill that enemy. (Does not apply to bosses and big mini bosses, or that would be too op. Only does a decent amount of damage to those.)

  Skins: Sensei, Serial killer
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "bloodmage":
            print("""Bloodmage: Dual wields Staff and Book.

  Season 3: ADVANCED CLASSES

  Stats: Like a vampire, can drain enemy health like lifesteal, and gains health and blood. (This is related to the bloodmage from raid boss destiny.) Use blood in order to use massive buffs on allies or healing, or damage. Can drain your own health to create blood attacks even stronger, same with the buffs. Ultimate: Boils blood in order to splat onto enemies, and burns them, also makes you take 5 damage every turn, but you do more damage, and can do AOE healing.

  Effects: Nausea, Dizziness
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        elif character == "special":
            print("""


  Event/Special Classes


  Reaper: Fight the grim reaper and beat him 20 times, and die 100 times total by any enemy from the dark realm.

  Snowman: Build a snowman for _____ in winter.

  Santa: Receive a present in winter.

  Civilian: Beat the Giant, boss.

  Alchemist: Help the alchemist from another world in a story quest.

  Juggernaut: Read the spearman skin, juggernaut description and do what it tells you.

  Mayor: Help 15 towns out.

  Attorney: Beat a certain boss in the courtyard.

  Summoner: Be a builder, defend the city, and obtain the special book from somebody on the 10th floor.

  Scientist: Beat the mad scientist as the alchemist class.

  Adventurer: Beat the game.

  Farmer: Heal as the civilian 1000 health.

  Surgeon: Heal 100,000 health with any class.

  Imp: Unlock the demon skin as swordsman or dual wielder.

  Freezer: Win the arctic event.

  Glator: Unlock achievement: How did you get here…? In the Roblox YouTuber realm in Tower Defense Simulator.

  Developer: (Locked unless developer gives you it)

  Hacker: Get sent to another realm and hack that world, during an event.

  Singer: Participate in a singing battle against others during an event.

  Imposter: Be able to slaughter during an event.

  Rick Astley: Beat the April Fools event, Never gonna give you up-

  Steve: Get into Minecraft and beat the game.

  Admin: Only unlocked if you are one of the creators.

  Moderator: Same thing as admin, but not that good.

  Beta tester: ONLY UNLOCKED BY PLAYING BETA VERSION

  Alpha tester: ONLY UNLOCKED BY PLAYING IN ALPHA VERSION
  """)
            doneornot = input("Are you done at looking at classes?(yes/no): "
                              ).lower().rstrip()
            if doneornot == "yes":
                break
            else:
                if doneornot != "no":
                    print("You gave an invalid answer.")
        else:
            print(
                "You may have made a typo, RPG database doesn't see that character or class."
            )
            print(divider)
            doneornot = "no"

elif whattodo == "adventure game":
    print("Welcome to RPG Chat Adventure game!")
    print(divider)
    energy = randint(40, 45)
    classesingame = [
        "hunter", "archer", "bandit", "wizard", "spearman", "swordsman"
    ]
    hunter = [
        "Rifle Shot(3 energy)", "Rifle Smack(0 energy)",
        "Rifle Headshot(15 energy)"
    ]
    hunterdamage = {"Rifle Shot": 40, "Rifle Smack": 10, "Rifle Headshot": 95}
    hunterenergycosts = {
        "Rifle Shot": 3,
        "Rifle Smack": 0,
        "Rifle Headshot": 15
    }
    hunterhealth = 210
    archer = [
        "Bow and arrow(3 energy)", "Bow and arrow Headshot(12 energy)",
        "Bow Smack(0 energy)", "Arrow Smack(2 energy)",
        "Shotgun Attack(8 energy)", "Minigun Attack(9 energy)"
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
    bandit = ["Dagger Slash(6 energy)", "Boomerang Throw(9 energy)"]
    banditdamage = {"Dagger Slash": 40, "Boomerang Throw": 60}
    banditenergycosts = {"Dagger Slash": 6, "Boomerang Throw": 9}
    bandithealth = 210
    wizard = [
        "Staff Smack(0 energy)", "Water Spell(8 energy)",
        "Fire Spell(9 energy)", "Electric Spell(10 energy)",
        "Slam Against A Wall Spell(9 energy)", "Meteor Shower(15 energy)"
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
    spearman = ["Spear Stab(7 energy)", "Spear Swing(6 energy)"]
    spearmandamage = {"Spear Stab": 55, "Spear Swing": 40}
    spearmanenergycosts = {"Spear Stab": 7, "Spear Swing": 6}
    spearmanhealth = 210
    swordsman = [
        "Sword Stab(7 energy)", "Sword Slash(6 energy)", "Sword Poke(3 energy)"
    ]
    swordsmandamage = {"Sword Stab": 50, "Sword Slash": 45, "Sword Poke": 20}
    swordsmanenergycosts = {"Sword Stab": 7, "Sword Slash": 6, "Sword Poke": 3}
    swordsmanhealth = 205
    dev = ["Ultimate Laser(1 energy)"]
    devdamage = {"Ultimate Laser": 10000000000000}
    devenergycosts = {"Ultimate Laser": 1}
    devhealth = 1000000000000000000000000000000000000000
    whatclass = input(
        "What class do you want to be? (Season 1 classes only, also, no healer and shieldman): "
    ).lower().rstrip()
    if whatclass == "hunter":
        print(
            f"You are a {whatclass} and have {hunterhealth} health. Your attacks are {hunter}."
        )
    elif whatclass == "archer":
        print(
            f"You are a {whatclass} and have {archerhealth} health. Your attacks are {archer}."
        )
        print(f"You have {energy} energy.")
    elif whatclass == "wizard":
        print(
            f"You are a {whatclass} and have {wizardhealth} health. Your attacks are {wizard}."
        )
        print(f"You have {energy} energy.")
    elif whatclass == "spearman":
        print(
            f"You are a {whatclass} and have {spearmanhealth} health. Your attacks are {spearman}."
        )
        print(f"You have {energy} energy.")
    elif whatclass == "bandit":
        print(
            f"You are a {whatclass} and have {bandithealth} health. Your attacks are {bandit}."
        )
        print(f"You have {energy} energy.")
    elif whatclass == "swordsman":
        print(
            f"You are a {whatclass} and have {swordsmanhealth} health. Your attacks are {swordsman}."
        )
        print(f"You have {energy} energy.")
    elif whatclass == "dev":
        print(
            f"You are a {whatclass} and have {devhealth} health. Your attacks are {dev}."
        )
        print(f"You have {energy} energy.")
    else:
      print("That is not a class avaliable in this game.")
      exit("Game Ended")
    leftorright = input(
        "You are walking on a path, do you want to go left or right? ").lower(
        ).rstrip()
    if leftorright == "right":
        print(f"You meet a {choice(classesingame)}!")
        choicemade = input(
            "Do you want to fight or try to make friends(make friends)? "
        ).lower()
        if choicemade == "make friends":
            friendsornotchoices = ["yes", "no", "maybe"]
            friendsornot = choice(friendsornotchoices)
            if friendsornot == "yes":
                print("You made friends with the person! He let you pass")
            elif friendsornot == "no":
                print(
                    "The person does not want to be friends, be prepared for battle!!!"
                )
            elif friendsornot == "maybe":
              print("The person says he will maybe be your friend, so he takes 5 energy and let you pass.")
              energy -= 5
              print(f"You have {energy} energy.")
        elif choicemade == "fight":
            print(divider)
            print("Prepare to fight...")
            enemyhealth = randint(190, 210)
            if whatclass == "hunter":
                  your_health = hunterhealth
                  print(f"You have {your_health} health")
            elif whatclass == "archer":
                  your_health = archerhealth
                  print(f"You have {your_health} health")
            elif whatclass == "wizard":
                  your_health = wizardhealth
                  print(f"You have {your_health} health")
            elif whatclass == "spearman":
                  your_health = spearmanhealth
                  print(f"You have {your_health} health")
            elif whatclass == "bandit":
                  your_health = bandithealth
                  print(f"You have {your_health} health")
            elif whatclass == "swordsman":
                  your_health = swordsmanhealth
                  print(f"You have {your_health} health")
            elif whatclass == "dev":
                  your_health = devhealth
                  print(f"You have {your_health} health")
            while enemyhealth > 0:
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
              attack = input("What attack do you want to use?: ").lower()
              if whatclass == "hunter":
                if attack == "rifle shot":
                  if energy >= hunterenergycosts.get("Rifle Shot"):
                    energy -= hunterenergycosts.get("Rifle Shot")
                    enemyhealth -= hunterdamage.get("Rifle Shot")
                    print(f"You used rifle shot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "rifle smack":
                  if energy >= hunterenergycosts.get("Rifle Smack"):
                    energy -= hunterenergycosts.get("Rifle Smack")
                    enemyhealth -= hunterdamage.get("Rifle Smack")
                    print(f"You used rifle smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "rifle headshot":
                  if energy >= hunterenergycosts.get("Rifle Headshot"):
                    energy -= hunterenergycosts.get("Rifle Headshot")
                    enemyhealth -= hunterdamage.get("Rifle Headshot")
                    print(f"You used rifle headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "archer":
                if attack == "bow and arrow":
                  if energy >= archerenergycosts.get("Bow and arrow"):
                    energy -= archerenergycosts.get("Bow and arrow")
                    enemyhealth -= archerdamage.get("Bow and arrow")
                    print(f"You used bow and arrow! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "bow and arrow headshot":
                  if energy >= archerenergycosts.get("Bow and arrow Headshot"):
                    energy -= archerenergycosts.get("Bow and arrow Headshot")
                    enemyhealth -= archerdamage.get("Bow and arrow Headshot")
                    print(f"You used bow and arrow headshot! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "bow smack":
                  if energy >= archerenergycosts.get("Bow Smack"):
                    energy -= archerenergycosts.get("Bow Smack")
                    enemyhealth -= archerdamage.get("Bow Smack")
                    print(f"You used bow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "arrow smack":
                  if energy >= archerenergycosts.get("Arrow Smack"):
                    energy -= archerenergycosts.get("Arrow Smack")
                    enemyhealth -= archerdamage.get("Arrow Smack")
                    print(f"You used arrow smack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "shotgun attack":
                  if energy >= archerenergycosts.get("Shotgun Attack"):
                    energy -= archerenergycosts.get("Shotgun Attack")
                    enemyhealth -= archerdamage.get("Shotgun Attack")
                    print(f"You used shotgun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "minigun attack":
                  if energy >= archerenergycosts.get("Minigun Attack"):
                    energy -= archerenergycosts.get("Minigun Attack")
                    enemyhealth -= archerdamage.get("Minigun Attack")
                    print(f"You used minigun attack! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "wizard":
                if attack == "staff smack":
                  if energy >= wizardenergycosts.get("Staff Smack"):
                    energy -= wizardenergycosts.get("Staff Smack")
                    enemyhealth -= wizarddamage.get("Staff Smack")
                    print(f"You used staff smack The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "water spell":
                  if energy >= wizardenergycosts.get("Water Spell"):
                    energy -= wizardenergycosts.get("Water Spell")
                    enemyhealth -= wizarddamage.get("Water Spell")
                    print(f"You used water spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "fire spell":
                  if energy >= wizardenergycosts.get("Fire Spell"):
                    energy -= wizardenergycosts.get("Fire Spell")
                    enemyhealth -= wizarddamage.get("Fire Spell")
                    print(f"You used fire spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "electric spell":
                  if energy >= wizardenergycosts.get("Electric Spell"):
                    energy -= wizardenergycosts.get("Electric Spell")
                    enemyhealth -= wizarddamage.get("Electric Spell")
                    print(f"You used electric spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "slam against a wall spell":
                  if energy >= wizardenergycosts.get("Slam Against A Wall Spell"):
                    energy -= wizardenergycosts.get("Slam Against A Wall Spell")
                    enemyhealth -= wizarddamage.get("Slam Against A Wall Spell")
                    print(f"You used slam against a wall spell! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "meteor shower":
                  if energy >= wizardenergycosts.get("Meteor Shower"):
                    energy -= wizardenergycosts.get("Meteor Shower")
                    enemyhealth -= wizarddamage.get("Meteor Shower")
                    print(f"You used meteor shower! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "bandit":
                if attack == "dagger slash":
                  if energy >= banditenergycosts.get("Dagger Slash"):
                    energy -= banditenergycosts.get("Dagger Slash")
                    enemyhealth -= banditdamage.get("Dagger Slash")
                    print(f"You used dagger slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "boomerang throw":
                  if energy >= banditenergycosts.get("Boomerang Throw"):
                    energy -= banditenergycosts.get("Boomerang Throw")
                    enemyhealth -= banditdamage.get("Boomerang Throw")
                    print(f"You used boomerang throw! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "spearman":
                if attack == "spear stab":
                  if energy >= spearmanenergycosts.get("Spear Stab"):
                    energy -= spearmanenergycosts.get("Spear Stab")
                    enemyhealth -= spearmandamage.get("Spear Stab")
                    print(f"You used spear stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "spear swing":
                  if energy >= spearmanenergycosts.get("Spear Swing"):
                    energy -= spearmanenergycosts.get("Spear Swing")
                    enemyhealth -= spearmandamage.get("Spear Swing")
                    print(f"You used spear swing! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "swordsman":
                if attack == "sword stab":
                  if energy >= swordsmanenergycosts.get("Sword Stab"):
                    energy -= swordsmanenergycosts.get("Sword Stab")
                    enemyhealth -= swordsmandamage.get("Sword Stab")
                    print(f"You used sword stab! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "sword slash":
                  if energy >= swordsmanenergycosts.get("Sword Slash"):
                    energy -= swordsmanenergycosts.get("Sword Slash")
                    enemyhealth -= swordsmandamage.get("Sword Slash")
                    print(f"You used sword slash! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                elif attack == "sword poke":
                  if energy >= swordsmanenergycosts.get("Sword Poke"):
                    energy -= swordsmanenergycosts.get("Sword Poke")
                    enemyhealth -= swordsmandamage.get("Sword Poke")
                    print(f"You used sword poke! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)
              if whatclass == "dev":
                if attack == "ultimate laser":
                  if energy >= devenergycosts.get("Ultimate Laser"):
                    energy -= devenergycosts.get("Ultimate Laser")
                    enemyhealth -= devdamage.get("Ultimate Laser")
                    print(f"You used ULTIMATE LASER! The enemy is now on {enemyhealth} health!")
                    print(divider)
                  else:
                    print("You don't have enough energy points! You die.")
                    break
                else:
                  print("Your class can't do that attack.")
                  print(divider)

              enemy_attack = randint(10,70)
              if whatclass == "hunter":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "archer":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "wizard":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "spearman":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "bandit":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "swordsman":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              elif whatclass == "dev":
                  print(
                      f"You have {your_health} health."
                  )
                  print(divider)
                  print(f"The enemy dealed {enemy_attack} damage to you!")
                  your_health -= enemy_attack
                  print(f"You have {your_health} health now.")
              
              if your_health <= 0:
                print(divider)
                print("You died.")
                print(divider)
                break
                exit("Game ended")
              elif enemyhealth <= 0:
                print(divider)
                print("You defeated the enemy! You gained some health.")
                print(divider)
                your_health += 180
                print(f"You have {your_health} health")




else:
    print("You gave an invalid answer")
    what_to_do()
