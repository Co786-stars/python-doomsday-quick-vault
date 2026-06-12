"""
1)) list slicing in python
2)) step use in list preformance
    [start:end] and [start:end:step]
"""
# for 1d array

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(arr[2:5]) # output of ndarray is : [30 40 50]
# print(tuple(arr[2:5])) # output : (np.int64(30), np.int64(30)), np.int64(30)))
print(arr[4:])
print(arr[:4]) # last index item is not included
print(arr[-3:-1]) # first item is not included

"""Now step value is important"""
arr2 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
print(arr2) 
print(arr2[4:9:2]) # stntax : [start:end] or [start:end:step]
print(arr[::2])  # we can also use this to take the step in list


# for 2d array 

arr3 = np.array((np.arange(20, 25), np.arange(10, 15), np.arange(25, 30)))
print(arr3[::2], end="\n\n")  # [[20 21 22 23 24] [25 26 27 28, 29]]
print(arr3[1:3, 2], end="\n\n")   # [[10 11 12 13 14] [25 26 27 28 29]] >> [12, 27] >> first(renge) second(index value)
print(arr3[1, 1:4], end="\n\n")  # [11 12 13 ] >> [start step]
print(arr3[1:3, 3:5], end="\n\n") # [[13 14] [28 29]]  [start:end, step]

