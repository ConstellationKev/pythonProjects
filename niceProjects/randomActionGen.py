from random import choice
people = ["Tony", "Kevin", "Dad", "Mom", "A Cow", "A Pig"]
verb = ["Eats", "Runs", "Cooks", "Writes", "Sings", "Punches", "Steals"]
noun = ["Tree", "Pig", "Book", "Dirt", "Sun", "Piano", "Airplane"]
place = ["Grocery Store", "Costco", "School", "Hospital", "Resturant", "Underground"]

for _ in range(2):
    print(f"{choice(people)} {choice(verb)} a {choice(noun)} at {choice(place)}")