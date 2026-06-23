list1 = ["_____", "_____", "_____"]
list2 = ["_____", "_____", "_____"]
list3 = ["_____", "_____", "_____"]
print("Welcome to tic tac toe")
divider = "---------------------"
print(divider)
print(list1)
print(list2)
print(list3)

def player1():
    while True:
        player1 = input("Where do you want to play player 1? 1 - 9 ").rstrip()
        if player1 == "1":
            if list1[0] == "__O__" or list1[0] == "__X__":
                print("That is taken")
                continue
            else:
                list1[0] = "__O__"
                break
        elif player1 == "2":
            if list1[1] == "__O__" or list1[1] == "__X__":
                print("That is taken")
                continue
            else:
                list1[1] = "__O__"
                break
        elif player1 == "3":
            if list1[2] == "__O__" or list1[2] == "__X__":
                print("That is taken")
                continue
            else:
                list1[2] = "__O__"
                break
        elif player1 == "4":
            if list2[0] == "__O__" or list2[0] == "__X__":
                print("That is taken")
                continue
            else:
                list2[0] = "__O__"
                break
        elif player1 == "5":
            if list2[1] == "__O__" or list2[1] == "__X__":
                print("That is taken")
                continue
            else:
                list2[1] = "__O__"
                break
        elif player1 == "6":
            if list2[2] == "__O__" or list2[2] == "__X__":
                print("That is taken")
                continue
            else:
                list2[2] = "__O__"
                break
        elif player1 == "7":
            if list3[0] == "__O__" or list3[0] == "__X__":
                print("That is taken")
                continue
            else:
                list3[0] = "__O__"
                break
        elif player1 == "8":
            if list3[1] == "__O__" or list3[1] == "__X__":
                print("That is taken")
                continue
            else:
                list3[1] = "__O__"
                break
        elif player1 == "9":
            if list3[2] == "__O__" or list3[2] == "__X__":
                print("That is taken")
                continue
            else:
                list3[2] = "__O__"
                break
        else:
            print("You gave an invalid answer")
            continue


    print(list1)
    print(list2)
    print(list3)

    checker()


def player2():
    while True:
        player1 = input("Where do you want to play player 2? 1 - 9 ").rstrip()
        if player1 == "1":
            if list1[0] == "__O__" or list1[0] == "__X__":
                print("That is taken")
                continue
            else:
                list1[0] = "__X__"
                break
        elif player1 == "2":
            if list1[1] == "__O__" or list1[1] == "__X__":
                print("That is taken")
                continue
            else:
                list1[1] = "__X__"
                break
        elif player1 == "3":
            if list1[2] == "__O__" or list1[2] == "__X__":
                print("That is taken")
                continue
            else:
                list1[2] = "__X__"
                break
        elif player1 == "4":
            if list2[0] == "__O__" or list2[0] == "__X__":
                print("That is taken")
                continue
            else:
                list2[0] = "__X__"
                break
        elif player1 == "5":
            if list2[1] == "__O__" or list2[1] == "__X__":
                print("That is taken")
                continue
            else:
                list2[1] = "__X__"
                break
        elif player1 == "6":
            if list2[2] == "__O__" or list2[2] == "__X__":
                print("That is taken")
                continue
            else:
                list2[2] = "__X__"
                break
        elif player1 == "7":
            if list3[0] == "__O__" or list3[0] == "__X__":
                print("That is taken")
                continue
            else:
                list3[0] = "__X__"
                break
        elif player1 == "8":
            if list3[1] == "__O__" or list3[1] == "__X__":
                print("That is taken")
                continue
            else:
                list3[1] = "__X__"
                break
        elif player1 == "9":
            if list3[2] == "__O__" or list3[2] == "__X__":
                print("That is taken")
                continue
            else:
                list3[2] = "__X__"
                break
        else:
            print("You gave an invalid answer")
            continue


    print(list1)
    print(list2)
    print(list3)

    checker()



def checker():
    if list1[0] == "__O__" and list2[0] == "__O__" and list3[0] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[0] == "__O__" and list1[1] == "__O__" and list1[2] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[1] == "__O__" and list2[1] == "__O__" and list3[1] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[2] == "__O__" and list2[2] == "__O__" and list3[2] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list2[0] == "__O__" and list2[1] == "__O__" and list2[2] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list3[0] == "__O__" and list3[1] == "__O__" and list3[2] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[0] == "__O__" and list2[1] == "__O__" and list3[2] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[2] == "__O__" and list2[1] == "__O__" and list3[0] == "__O__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[0] == "__X__" and list2[0] == "__X__" and list3[0] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[0] == "__X__" and list1[1] == "__X__" and list1[2] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[1] == "__X__" and list2[1] == "__X__" and list3[1] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[2] == "__X__" and list2[2] == "__X__" and list3[2] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list2[0] == "__X__" and list2[1] == "__X__" and list2[2] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list3[0] == "__X__" and list3[1] == "__X__" and list3[2] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[0] == "__X__" and list2[1] == "__X__" and list3[2] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")
    elif list1[2] == "__X__" and list2[1] == "__X__" and list3[0] == "__X__":
            print(divider)
            print("Player 1 wins!")
            exit("Game Ended")

    if (list1[0] == "__O__" or list1[0] == "__X__") and (list1[1] == "__O__" or list1[1] == "__X__") and (list1[2] == "__O__" or list1[2] == "__X__") and (list2[0] == "__O__" or list2[0] == "__X__") and (list2[1] == "__O__" or list2[1] == "__X__") and (list2[2] == "__O__" or list2[2] == "__X__") and (list3[0] == "__O__" or list3[0] == "__X__") and (list3[1] == "__O__" or list3[1] == "__X__") and (list3[2] == "__O__" or list3[2] == "__X__"):
        print("It's a tie.")
        exit("Game Ended")

while True:
    player1()
    player2()