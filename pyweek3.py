#!/usr/bin/python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for i in a:
   if i < 5:
      b.append(i)

print("{0} is a list of all items smaller than 5".format(b))

num = int(input("Please Enter a number\n"))
for i in a:
    if i < num:
       c.append(i)

print("{0} is a list of all items smaller than {1}".format(c, num))
