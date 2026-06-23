from random import randint, choice
from string import ascii_letters
print("Welcome to the Username and Password Generator! You can always rerun this program until you get a username and password you like.")
adjectives = ["Blazing", "Frozen", "Cool", "Brave", "Awesome", "Dark"]
animals =  ["Dragon", "Monkey", "Tiger", "Frog", "Bat", "Eagle", "Shark", "Scorpion","Phoenix", "Character"]
nouns = ["Ninja", "Prince", "Hero", "Robot", "Jedi", "Wizard", "Doctor", "King", "Dude"]
likeornot = "no"
for k in range(999999999999999999999999999999999999999999999999999999999999999999999999):
  if likeornot == "no":
    username = choice(adjectives) + choice(animals) + choice(nouns) + str(randint(100,999))
    password = ""
    length = randint(10, 19)
    for n in range(length):
      character = choice(["number", "special character", "letter"])
      if character == "number":
        password += str(randint(0,9))
      elif character == "special character":
        password += choice(["@", "#", "!", "$", "%", "&", "*"])
      elif character == "letter":
        password += choice(ascii_letters)
    print(f"Your username is {username}")
    print(f"Your username is {password}")
    likeornot = input("Do you like your username and password?(yes/no): ").lower().rstrip()
  elif likeornot == "yes":
    print("Great!")
    break
  else:
    print("You gave an invalid answer, please restart.")
    break
