#!/usr/bin/python
num = int(input("Please Enter a number\n"))
a = range(1, num+1)
b = []

for i in a:
    if num%i == 0:
       b.append(i)

print("{0} is a list of all numbers divisors of {1}".format(b, num))
