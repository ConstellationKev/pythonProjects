win_or_not = {
  "RS" : "Player 1 wins!",
  "RR" : "Tie",
  "RP" : "Player 2 wins!",
  "SP" : "Player 1 wins!",
  "SS" : "Tie",
  "SR" : "Player 2 wins!",
  "PR" : "Player 1 wins!",
  "PP" : "Tie",
  "PS" : "Player 2 wins!"
}
def start_game():
  start_question = input("Do you want to play Rock Paper Scissors?(Y/N) ").upper().rstrip()
  if start_question == "Y":
    while True:
      input1 = input("\nPlayer 1, what do you choose?(R/P/S) ").upper().rstrip()
      input2 = input("Player 2, what do you choose?(R/S/P) ").upper().rstrip()
      winornot = input1 + input2
      print("\n" + win_or_not[str(winornot)])
      decision = input("\nWould you like to keep playing?(Y/N) ").upper().rstrip()
      if decision == "N":
        print("Thanks for playing!")
        break
      else:
        continue
  else:
    print("Okay, we can play again next time.")
start_game()
