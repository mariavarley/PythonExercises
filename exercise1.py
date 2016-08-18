#!/usr/bin/python
#Define a function max() that takes two numbers as arguments
#and returns the largest of them.
#Use the if-then-else construct available in Python.
#(It is true that Python has the max() function built in,
# but writing it yourself is nevertheless a good exercise.)
def max(num1, num2):
        if num1 == num2:
           return ERROR
	elif num1 > num2:
           return num1
        else: return num2

num1 = input("What's the first number? ")
num2 = input("What's the second number? ")

largest = max(num1, num2)
print("The larger number is {0}".format(largest))
