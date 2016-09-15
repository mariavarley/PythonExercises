#!/usr/bin/python
import datetime
import random

rand = random.randint(1,9)

noguess = 0
while True:
   num = int(input("Please pick a number between 1 and 9:\n"))
   noguess = noguess + 1;

   if rand == num:
      print("You guessed right!")
      print("You made {0} guesses".format(noguess))
      break
   elif num < rand:
      print("You guessed too low!")
   else:
      print("You guessed too high!")

   guess = input("Press enter to guess again? If not enter exit\n")
   if guess == "exit":
      print("You made {0} guesses".format(noguess))
      break

