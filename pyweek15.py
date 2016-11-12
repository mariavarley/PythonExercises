#!/usr/bin/python
#Exercise 15
#Write a program (using functions!)
#that asks the user for a long string containing multiple words.
#Print back to the user the same string,
#except with the words in backwards order.

def reverse_string_1(input_string):
   result = sentence.split()
   result.reverse()
   result = " ".join(result)
   return result

sentence = raw_input("Please Enter a long string containing multiple words\n")
reverse_string = reverse_string_1(sentence)
print("The reversed list:{0}".format(reverse_string))
