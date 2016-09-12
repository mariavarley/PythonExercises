#!/usr/bin/python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


list2 = [i for i in a if i %2 == 0 ]
print("{0} is a list of all even elements".format(list2))
