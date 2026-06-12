"""
In this module we again discuss the iteration of array but in this module we discuss how we 
iterate the each scaler element 
"""
# __________________________different parameter use whith nditer function__________________#
import numpy as np 
arr = np.array(np.arange(1, 9), ndmin=1)
arr = arr.reshape(2, 2, 2) # [[[1 2][3 4]]  [[5 6][7 8]]]
for i in np.nditer(arr):
    print(i)


arr = np.array(np.arange(20), ndmin=1)
# arr = arr.reshape(2, 2, 5) # in 3d : [[[ 0  1  2  3  4]
#                                      [ 5  6  7  8  9]]
#                                      
#                                     [[10 11 12 13 14]
#                                      [15 16 17 18 19]]]
print(arr)
for i in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
    print(i)


x = np.array([1, 2, 3, 4, 5])
for i in np.nditer(x, flags=['buffered'], op_dtypes=['S']): # copy or buffered value is important when we use ndiiter 
    print(i)

# ______________________________different step and size________________________________________#

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80 , 90], ndmin = 1)
for i in np.nditer(arr[::2]): # for 1d array skip 1 step
    print(i)


arr = arr.reshape(3, 3) # [[10 20 30] [40 50 60] [70 80 90]]
print(arr)
for i in np.nditer(arr[::2]): # take the step 1 step means array # [10 20 30] [40 50 60]
    print(i, end=" ") # 10 30 50 70 80 90 # arr[:, ::2] or arr[::2] value are same

# __________________________enumerated iteration using ndenumerate()___________________________#
# __________________________enumerated iteration using ndenumerate()___________________________#
# __________________________enumerated iteration using ndenumerate()___________________________#
# __________________________enumerated iteration using ndenumerate()___________________________#

"""
The word Enumeration means mentioning sequence number of somethings one by one .
when we use ndenumerate() method whith array ?
when we required corosponding index of the element while iterating
"""

arr = np.array([1, 2, 3])
for px, x in np.ndenumerate(arr):
    print(px, x)



arr = np.array(np.arange(16), ndmin= 1)
arr = arr.reshape(4, 4)  # [[[0 1][2 3]] [[4 5][6 7]] [[8 9][10 11]] [[12 13] [14 15]]]
for idx, x in np.ndenumerate(arr):  # idx store index value of element that stored in x one by one 
    print(idx, x)                   # x store element of array one by one and idx show it position



# Create a 2D NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Use np.ndenumerate() to get indices and values
for index, value in np.ndenumerate(array):
    print(f"Index: {index}, Value: {value}")
# np.ndenumerate() function helps you access both the index and the value of each 
# element in a multi-dimensional NumPy array


