exitornot = "no"
ICE_CREAM = ["chocolate", "vanilla"]
while exitornot == "no":
  add = input(f"Right now you have these flavors: {ICE_CREAM}. Do you want to add or remove something? ").lower().rstrip()
  if add == "add":
    what = input("What do you want to add? ").rstrip()
    ICE_CREAM.append(what)
    print(f"Right now you have these flavors: {ICE_CREAM}.")
  elif add == "remove": 
    something = input("What do you want to remove? ").rstrip().lower()
    ICE_CREAM.remove(something)
    print(f"Right now you have these flavors: {ICE_CREAM}.")
  else: 
    print("You gave an invalid response.")
  exitornot = input("Do you want to exit or not?(exit/no) ").lower().rstrip()
print(", ".join(ICE_CREAM))

