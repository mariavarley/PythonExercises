#!/usr/bin/python
def get_num_from_user():
   num = int(input("Please enter a number:\n"))
   return num

def is_num_prime(num):
   a = range(1, num+1)
   b = []
   for i in a:
      if num%i == 0:
         b.append(i)

   if len(b) == 2:
      print("{0} is a prime number".format(num))
   else:
      print("{0} is not a prime number and here are its divisors:{1}".format(num, b)) 

num = get_num_from_user()

is_num_prime(num)
