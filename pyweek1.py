#!/usr/bin/python
import datetime
name = input("Please enter your name\n")
age = int(input("Please enter your age\n"))
howmany = int(input("Please enter another number\n"))
now = datetime.datetime.now()
year = now.year

ans = year + (100 - age)

i = 0
while i < howmany:
	print("{0}, you will be 100 in the year {1}".format(name, ans))
	i = i + 1;
