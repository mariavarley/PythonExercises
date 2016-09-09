#!/usr/bin/python
str = input("Please Enter a string\n")
b = str[::-1]

if str == b:
   print("{0} is a palindrome".format(str))
else:
   print("{0} is not a palindrome".format(str))
