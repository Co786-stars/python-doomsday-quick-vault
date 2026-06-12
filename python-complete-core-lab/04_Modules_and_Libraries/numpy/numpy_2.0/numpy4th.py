"""
Whole module is about indexing of Numpyarray
1)) indexing of nndarray
2)) negative indexing of ndarray

"""
import numpy as num


var = num.array([10, 20, 30, 40, 50], ndmin = 1) # 1d array
print(var[0]) # access the 1st position index elemnent from ndarray that is 10


var = num.array([[1, 2, 3], [3, 2, 1], [4, 5, 6]], ndmin = 2)  # 2d array
# there are the two way to acess the 2d element or 3d element
print(var[1][2]) # access the 2nd postion of 3rd index value from ndarray which is 1
print(var[1, 2]) # access the 2nd position of 3rd element value from ndarray



var = num.array([[[2, 3, 4], [5, 7, 7]], [[9, 8, 7], [5, 3, 4]]], ndmin = 3) # 3d array
print(var[0][1][1]) # access the 2nd element of 2nd array from 1st position of array   
print(var[0, 1, 1]) # access the 2nd element of 2nd array from 1st position of array

# print(var[0][0][1]) # output 2 
# explation : - How 7 is an answer
# array contian total number of 2 array that is denoted with index 0 or 1
# index 0 contain total two array that is also denoted with 0 and 1
# now at the position 1 array 1 index element is 7
# and we acess at the 0 position on 1 index place display value of 1st index element
# that is 7 . Hence thats why 7 is display 
#  
lst = [[10, 20, 30, 40], [10, 20, 30, 40]]
# print(lst[1, 2])  # error occure because only by this method ndarray is accessable .

# Now negative indexing 
var = num.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(var)
print(var[1, -1]) # in negative indexing list item always start with -1 , -1 ...((-1-tn)-1)


 