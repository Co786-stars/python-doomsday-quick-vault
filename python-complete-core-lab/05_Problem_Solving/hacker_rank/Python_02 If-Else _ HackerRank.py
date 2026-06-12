class Number:
    def __init__(self, user_value):
        """initialize the attributes"""
        self.n = user_value

    def actions(self):
        """method is tried performed an actions"""
        if self.n%2 != 0:
            self.val = "Weird"

        elif self.n%2 == 0 and 2 >= self.n <= 5:
            self.val = "Not Weird"

        elif self.n%2 == 0 and 6 >= self.n <= 20:
            self.val = "Weird"

        else:
            self.val = "Not Weird"

        return self.val  # return the exact values


class WirdNotWird(Number):
    """class body is try to display the output"""
    def __int__(self, user_input):
        super().__int__(1)  # placed user_input to remove the override issue


    def display(self):
        self.stored_value = super().actions() # invoke the actions method in parents class
        return self.stored_value

try:
    user = int(input("Enter the number : ")) # 5
    obj = WirdNotWird(user)  # parents constructor is initiliaze
    final_output = obj.display()
    print(final_output)
except ValueError:
    print("pls enter the valid number")

'''
#!/bin/python3
import math
import os
import random
import re
import sys

n = int(input().strip())
if n % 2 != 0:
    var = "Weird"

elif n % 2 == 0 and n >= 2 and n <= 5:
    var = "Not Weird"

elif n % 2 == 0 and n >= 6 and n <= 20:
    var = "Weird"
else:
    var = "Not Weird"
print(var)
'''

# Task/Question:
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of  2 to 5 , print Not Weird
# If n is even and in the inclusive range of  6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
#
# A single line containing a positive integer, n.
# Constraints
# 1 <= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.



# Extra : - Other method
# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2 != 0:
#         value = "Weird"
#     elif n%2 == 0  and n <= 5:
#         value = "Not Weird"
#     elif n%2 == 0 and n <= 20:
#         value = "Weird"
#     else:
#         value = "Not Weird"
#     print(value)
