#!/usr/bin/python

while True:
   print("Please type rock, paper or sissors to play or quit to quit the game:\n")
   player1 = input("Player1:")
   player2 = input("Player2:")

   if player1 == player2:
      print("It's a draw!!")
   elif player1 == "rock" and player2 == "scissors":
      print("Player1 is the winner!!")
   elif player1 == "sissors" and player2 == "paper":
      print("Player1 is the winner!!")
   elif player1 == "paper" and player2 == "rock":
      print("Player1 is the winner!!")
   else:
      print("Player2 is the winner!!")

   play = input("Do you want to play again?\n")
   if play == "no":
      break
