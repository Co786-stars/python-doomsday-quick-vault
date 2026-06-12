"""
This topic is all about How to access 1d 2d 3d array element through loop using while or for 
as well. and how to iterate the more diminsions of array using numpy.nditter() attribute
"""
# ________________________________1d array______________________________________#

import numpy as np
arr = np.array([10, 20, 30], ndmin= 1)

# by using for loop we iterate the array : 1d arrray
for i in arr:
    print(i)   # all element of 1d array are display on output


arr = arr.reshape(3, 1) # this is the only one option for reshaping 
# now we iterate the 2d array [[10][10][30]]
for i in arr:
    print(i)


# by using for loop iterate through n-D array
arr = np.array(np.arange(100, 1000, 50), ndmin = 1)
for i in arr:
    print(i) 

# ________________________________2d array______________________________________#

arr = np.array(np.arange(10, 100, 10), ndmin=2) # [[10 20 30 40 50 60 70 80 90]]
arr = arr.reshape(3, 3)
for i in arr:  # for id array access row of array 
    print(i)   # which mean : 1st element of 2d array [10 20 30]
#                             2nd element of 2d array [40 50 60]
#                             4th element of 2d array [70 80 90]
# >> To access the element we use row loop as well as column loop


for i in arr:      # 1st iter : [10 20 30]   2nd iter : [40 50 60]    3rd itr : [70 80 90]
    for j in i:    # j stored :  10 20 30    j stored :  40 50 60    j stored :  70 80 90
        print(j)  # now the each element access one by one from single row out through print()

# _________________________________3d array________________________________________#

arr = np.array(np.arange(10, 100), ndmin=1)
# print(len(arr))  we use one of these any one to see the total 
# print(arr.shape)  number of element in dimension of list
arr = arr.reshape(3, 2, 15) # [[[][]] [[][]] [[][]]] # print(arr) 
for i in arr:  # access the 1d element which in in the from of array (access the row of 3d array)
    for j in i: # access the 2d element which is in the from of array (access the row of 2d array)
        for k in j: # acces the 3d dimension element value that we want 
            print(k)  # value of k is out in horizintal format

for i in arr:
    for j in i:
        print(j)  # simpley array is out one by one

# _____________________________numpy.nditer() attribute_________________________#

arr = np.array(np.arange(10), ndmin=1)
for i in np.nditer(arr):  # if arr is 1d 
    print(i)

arr = arr.reshape(5, 2)
# now the output is : [[0 1][2 3][4 5][6 7][8 9]]
for i in np.nditer(arr): # iterate item : [0 1] [2 3] [4 5] [6 7] [8 9]
    for j in np.nditer(i): #
        print(i)  # use np.adarray when we not known how we visulize the data 

for i in np.nditer(arr):
    print(i, end=" ")
    
