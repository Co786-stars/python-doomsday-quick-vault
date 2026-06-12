# _________________________________________________________________________________________
# Array reshape
# By reshaping we can add or remove dimensions or change number of element in each diminsion
import numpy as np 
x = np.array([1, 2, 3, 4, 5, 6])   # 1d array to 2d array
y = x.reshape(2, 3) # first dimensonal element is 2 and second dimensional element  is 3
print(y) # [[1 2 3] [4 5 6]]

x = np.array((np.arange(10, 90, 5)), ndmin = 1) # 
# y = x.reshape() #
print(x.shape) # first we find the total element of array that is 16 element in 0 dimension (16,)
print(x.reshape(2, 2, 4)) # 1d array to 3d array >> [[] []] >> [ [[] []] [[] []] ]
# >> [[[10 15 20 25] 
#      [30 35 40 45]] 
#      [[50 55 60 65]
#      [70 75 80 85]]]

"""
Note : - We can not reshape into any shape of ndarray first we analyze then we procede it.
"""

# Return copy or view
arry = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arry.reshape(2, 4)) # >> [[] []] >> [[1 2 3 4] [5 6 7 8]]
# print(arry.reshape(3, )) # >> [[] [] []] >> [[] [] []] # not possible that why we can't reshape 
#                                                        the array into any shape using reshape attribute
print(arry.reshape(4, 2)) # [[] [] [] []] >> [[1 2] [3 4] [5 6] [7 8]]

# Now return or view
print(arry.reshape(2, 4).base) # check and return the array is copy or view output [1 2 3 4 5 6 7 8 9]

x = np.array(np.arange(10), ndmin = 1)
y = x.reshape(2, 5) # [[][]] >> [[0 1 2 3 4] [5 6 7 8 9]]
z = x.view()  # z store the views of x as it is 
print(y)
print(z)
print(z.reshape(5, -1)) # Note :- when we pass the -1 from reshape method then python auto reshape
#                                 the ndarrays but we can not pass -1 in more then 1d.
#                                 if we try to pass from more then 1d array then it return 0d ndarray

x = np.array(np.arange(1, 11), ndmin = 3)
x = x.reshape(5, 2)
print(x.shape) # (5, 2) 
print(x.reshape(-1))  # if use -1 in more the 1d array then return single ndarray

x = np.array(np.arange(5), ndmin = 1)
print(x.shape)



"""_________________________________________________________________________________

NOTE : - THERE ARE MORE FUNCTION TO CHANGE THE SHAPE OF ARRAY IN NUMPY GIVEN BELOW : -
         flatten, ravel
         FOR REARRANGING ELEMENT WE HAVE A FUNCTION : -
         rot90, flip, fliplr, flippud
"""
