"""
Numpy joining array function using concatenate() function
np.stack() and np.concatenate() are used to combine NumPy arrays, but they work a bit 
differently.
"""

# np.concatenate()
# This function joins a sequence of arrays along an existing axis.

import numpy as np 
arry1st = np.array(np.arange(1, 5), ndmin = 1)
arry2nd = np.array(np.arange(5, 10), ndmin = 1)
arry3rd = np.concatenate((arry1st, arry2nd))  # numpy.concatenate() use to join the two nd arrays
print(arry3rd)

arr1st = np.array([[10, 20], [20, 40]], ndmin = 2)
arr2nd = np.array([[60, 70], [80, 90]], ndmin = 2)
arr4th = np.concatenate((arr1st, arr2nd), axis=1)
print(arr4th)

"""Numpy joining array function using stack() function"""
# np.stack()
# This function joins a sequence of arrays along a new axis. The arrays must have the same shape.
arr = np.stack((arr1st, arr2nd), axis=1)
print(arr)


# np.stack() adds a new axis, and all input arrays must have the same shape.
# np.concatenate() joins arrays along an existing axis, and the input arrays must 
# have compatible shapes except in the axis of concatenation.