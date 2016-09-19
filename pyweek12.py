#!/usr/bin/python
a = [5, 10, 15, 20, 25]


def make_list(list):
   new_list = []
   new_list.append(list[0])
   new_list.append(list[-1])
   print("The new list:{0}".format(new_list))

make_list(a)
