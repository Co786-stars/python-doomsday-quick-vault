"""" -------------------: Basic of Numpy :-------------"""
"""
-:-:-:--:-:-:- whole module is about -:-:-:-:-:-:- How to create ndarray  
1)) ndarray
2)) ndim attribute
3)) ndmin argument
"""


# Numpy is use to work with arrays and the array object of numpy is called ndarray
# ndarray object is created in numpy using numpy.array() function
# to create the ndarray we pass the datatpe from array() function
# then the datatype is convert into ndarray with the help of numpy.array() function.

import numpy as np
var1 = np.array([1, 2, 3, 4]) # list is convert into ndarray using numpy.array()
var2 = np.array((1, 2, 3, 4, 5)) # tuple converted in the form of list (array) using numpy.array()
var3 = np.array({1, 2,3, 4, 5, 6, 8, 9})
print(type(var1), var1)
print(var2)
print(var3)

# Simple : to create ndarray we pass the array datatype from array() function

a1 = np.array(10)  # element as a array or  0d array
print(a1)

a2 = np.array([1, 2, 3, 4, 5]) # 1d array with element
print(a2)

a3 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])  # 2d array with 1d array 
print(a3)

a4 = np.array([[[10, 20, 30], [10, 20, 30]], [[10, 20, 30], [10, 20, 30]], 
               [[10, 20, 30], [10, 20, 30]]]) # 3d array with 2d array
print(a4)

# ndim attribute  provided by numpy to check array dimension and return in the from of integer
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)


arrr = np.array((1, 2, 3, 4, 5, 6), ndmin = 1) # we should always use ndmin argument to  
print(arrr)  # specify the dimenson of list 



