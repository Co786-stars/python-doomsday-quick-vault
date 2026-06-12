"""
Where function is not available in python .
Python numpy library offer a where() function and it often use for filtering elements in 
array based on condition 

To search the array element accordunf to satsified condition 
"""
# example 1

import numpy as np

# Create an array with values from 0 to 9
arry = np.array(np.arange(10))

# Use where() to get indices where elements are greater than 5
num1 = np.where(arry > 5)
print(num1)  # Output: (array([6, 7, 8, 9]),)



# Create an array with values from 10 to 19
arry = np.array(np.arange(10, 20))

# Use where() to get indices where elements are less than 13
num2 = np.where(arry < 13)
print(num2)  # Output: (array([0, 1, 2]),)


# Create an array with values from 10 to 19
arry = np.array(np.arange(10, 20))

# Use where() to get indices where elements are greater than 13 and less than 18
num2 = np.where((arry > 13) & (arry < 18))
print(num2)  # Output: (array([4, 5, 6, 7]),)


"""Now How it is work internally """

import numpy as np

# Create an array with values from 100 to 900, step 100
arr = np.array(np.arange(100, 1000, 100), ndmin=1)
# Apply the condition: elements greater than 500
con = arr > 500  # con = [False False False False False  True  True  True  True]
#                       100   200   300   400   500  < 600   700   800   900]
# Use np.where() to get indices where the condition is True
print(np.where(con))  # Output: (array([5, 6, 7, 8]),)
#                               [ 5    6    7    8 ]  # index value  where the element is True

# explain : -
# the array element compare with 500 itself one by one if it si greater the True store on that place else false store 
# now then after we use where from numpy module that show the index value of that place where True is store 
# then we conform from the index value of that item is satsified with condition .


x = np.array([1, 2, 4, 2, 4, 2], ndmin = 1)
y = np.where(x==2) # exactly output : 1st step => where([False True False True False True]) 2nd step =>> [0 1 3 5]  
print(y) # [0 1 3 5] >> then we acess the item from given index


# Now one more example
x = np.array(np.arange(1, 5), ndmin = 1)
y = np.where(x%2 == 0)
print(y)
#output : -
# step 1st : where([1%2==0, 2%2==0, 3%2==0, 4%2==0, 5%2==0])
# step 2nd : where([ False   True    False   True    False])
# step 3rd : where([          1                3          ]) # display index value
# output   : [1 2]
# Now on the index 1 and 2 the item is 2 and 4
# so due the the were function get only index value according to satsified condition 
