#!/usr/bin/python

def generate_fib(num):
   fib_nums = []

   for i in range(0,num):
      if i == 0:
         fib_nums.append(1)
      elif i == 1:
         fib_nums.append(1)
      else:
        fib_nums.append(fib_nums[i-2] + fib_nums[i-1])

   return fib_nums

while quit != "quit":
   num = int(input("Input how many Fibonnaci numbers you want generated:"))
   seq = generate_fib(num)
   print("The fibonacci sequence generated is:{0}".format(seq))
   quit = input("Press enter to generate another fibonnaci sequence or type quit to end:\n")
