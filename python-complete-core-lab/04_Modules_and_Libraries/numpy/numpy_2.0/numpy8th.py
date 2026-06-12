"""It about use of shape atttribute in numpy"""
# Array shape of numpy attribute
# shape atttribute is  define number of element in each diminsion
# Numpy shape attribute returns tuple with each index
 
import numpy as np 
arr = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
print(arr)   #output : (2, 5) # 2 denote number of first dimensional element 
print(arr.shape) # and 5 denote number of second dimensional element

arr2 = np.array(np.arange(5), ndmin =3)
print(arr2.shape) # output (1, 1, 5) 

# the value 1 1 5 it means array cis 3 dimensional and first dimension contain 1 element 
# second dimensional also contain 1 element and third dimensional contain 5 element
print(arr2) # [[[0 1 2 3 4 5]]]
