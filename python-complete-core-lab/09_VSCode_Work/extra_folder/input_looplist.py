"""x  = bytearray()  # empty byte array
print(x)

x = 5
y = bytearray(x)   # bytearray with integer
print(y)


x = [1, 2, 3, 4, 5] # list integer bytearray
y = bytearray(x)
print(y)



x  = "wizard"
y  = bytearray(x, 'utf-8')
z  = bytearray(x, 'utf-16')
# p  = bytearray(x)  error generate string argument without encoding 
print(y)
print(z)
# print(p)  error genreate p is not define name error

"""


# unicode of  about utf-8 and utf-16

# print('\U00000061') 
# import math 
# x = "Enter your number : "
# squareroot = int(input(x))
# squareroot = math.sqrt(squareroot)

# print(format(squareroot))

import os
os.system('notepad.exe lang_cod')