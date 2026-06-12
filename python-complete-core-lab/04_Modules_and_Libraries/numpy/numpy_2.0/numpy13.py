"""
In Numpy this module is all about split function in numpy that is : -
numpy.array_split(), numpy.hsplit(), numpy.vsplit(), numpy.dsplit
all are work same there are more functions to concatenate etc like 
vstack(), dstack() 
"""

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90], ndmin = 1)
newarr = np.array_split(arr, 3)
print(newarr)  # access the array that split with the help of array_split function
print(newarr[1]) # access the splited array

arry = np.array(np.arange(100, 1000, 99), ndmin = 1)
# print(arry.shape)
arry = arry.reshape(2, 5)
print(arry)
new = np.array_split(arry, 2)
new2 = np.array_split(arry, 2, axis = 1)
print(new)
print(new2)
print(arry.base) 

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]], ndmin = 2)
print(np.hsplit(x, 3))