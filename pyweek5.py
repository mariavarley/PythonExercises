#!/usr/bin/python
from random import randint
a = []
b = []

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def generate_list(l_name):

   random_size = randint(5, 20)
   for x in range(random_size):
      l_name.append(randint(0, 40))
   print("Random list: {0}".format(l_name))
   return l_name

generate_list(a)
generate_list(b)
c = []

for i in a:
    if i in b and i not in c: 
       c.append(i)

print("{0} is a list of all numbers that are in both lists".format(c))
