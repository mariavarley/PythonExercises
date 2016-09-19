#!/usr/bin/python
import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(10), 5)
b = random.sample(range(10), 10)

list2 = [i for i in a for x in b if i == x]
print("{0} is a list of all elements common to both lists".format(list2))
