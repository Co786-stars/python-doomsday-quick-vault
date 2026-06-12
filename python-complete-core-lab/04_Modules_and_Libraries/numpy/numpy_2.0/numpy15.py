""" 
After where method Now in Searching we discuss searchsorted() function or method
searchsorted() function is part of the NumPy library in Python. 
It is used to find the indices where elements should be inserted to maintain order.
"""
# searchsorted() function returns the index at which the value 
# should be inserted to maintain the order.
import numpy as num
arr = num.array([10, 20, 30, 40, 50])
x = num.searchsorted(arr, 30)
print(x)  # only index

# Now what will happen when the value is not occure in arrray
y = num.searchsorted(arr, 95)
print(y)

"""
The method start search from left side or a write side to find the element from any side 
we must pass side parameter in searchsorted() method
"""
#example 
arr = num.array([10, 30, 20, 40, 50], ndmin = 1)
y = num.searchsorted(arr, 20, side='left')  # 1 (before the existing 20 index value return if start searching from right).
z = num.searchsorted(arr, 20, side='right')  # 3 (after the existing 20 index value return if start searching from right).
print(y, z)

# Note : - 
# side='left': The function returns the index of the first suitable location, which is 1 
#              (before the existing 20).

# side='right': The function returns the index of the last suitable location, which is 2 
#               (after the existing 20).

