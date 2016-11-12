#!/usr/bin/python
#Exercise 14
#Write a program (function!) that takes a list and
#returns a new list that contains all the elements
#of the first list minus all the duplicates.

def remove_duplicates_1(list1):
   return list(set(list1))

def remove_duplicates_2(list1):
   list2 = []
   for i in list1:
      if i not in list2:
         list2.append(i)

   return list2

list1=[1,2,3,4,"five",5,"five",4,3,2,1]
print("The list with duplicates is:{0}".format(list1))
new_list1 = remove_duplicates_2(list1)
print("The list without duplicates using the list function is:{0}".format(new_list1))
new_list2 = remove_duplicates_1(list1)
print("The list without duplicates using the set function is:{0}".format(new_list2))
