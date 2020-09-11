# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:21:37 2020

@author: sreya
"""

# Print the first Armstrong number in the range of 1042000 to 702648265 and exit the loop as soon as you encounter the first armstrong number.
#use While loop


lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):

    # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print("The first armstrong number is ",num)
       break