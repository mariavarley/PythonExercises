#!/usr/bin/python
num = int(input("Please Enter a number\n"))
check = int(input("Please Enter a number to divide with\n"))

if num%4 == 0:
   print("The number is divisible by 4")
elif num%2 == 0:
   print("The number is an even number")
else:
   print("The number is an odd number")

if num%check == 0:
   print("The number, {0} divides into {1} evenly".format(check, num))
else:
   print("These numbers do not divide evenly")
