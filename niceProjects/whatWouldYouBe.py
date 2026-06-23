from random import choice

powers_yes_or_no = choice(["yes", "no", "no", "no", "no"])
if powers_yes_or_no == "yes":
    powers = choice(["fire", "shadow", "ice", "water", "mythic arts", "flying", "super strength"])
    print(f"YOU HAVE POWERS: {powers}")
name = choice(["Kevin", "Tony"])
home = choice(["mansion", "dog house", "house", "apartment", "igloo", "hotel", "basement", "rv van", "boat house", "underground base"])
transport = choice(["car", "helicopter", "feet", "bicycle", "private jet", "hovercraft", "portals", "motercycle", "scooter", "boat", "yacht", "horse", "donkey"])
job = choice(["president", "dentist", "pro athlete", "docter", "surgeon", "soldier", "pilot", "software engineer", "clown", "CEO", "waiter", "teacher", "vet", "truck driver"])
salary = choice(["$10 per year", "$100 per year", "$1,000 per year", "$100,000 per year", "$1,000,000 per year", "$10,000,000 per year", "$1,000,000,000 per year", "$1,000,000 per minute", "$0.01 per year"])
pet = choice(["fish", "dog", "cat", "bird", "shark", "octopus", "turtle", "dragon", "robot"])
place = choice(["mountains", "beach", "city", "farm", "iceberg", "desert", "volcano", "island", "park"])

print(f"{name} would live in a {home} at the {place}. You have a awesome {transport}. Your job is a {job} and earn {salary}. You also have a {pet} as a pet.")
