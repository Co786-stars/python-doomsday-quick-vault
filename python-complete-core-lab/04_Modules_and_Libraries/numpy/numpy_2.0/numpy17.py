"""
Numpy filtering : -
Filtering in NumPy involves selecting elements from an array that meet certain conditions. 

It's a powerful way to extract and work with subsets of data based on specific criteria.

The filter condition is created using comparison operations (>, <, ==, etc.).

we can filter based on multiple conditions, combine conditions using logical operators (&, |)
and apply filtering to multi-dimensional arrays.
"""

# ______________________________________________________________________________________________#

import numpy as np
x = np.array(np.arange(100, 0, -10), ndmin = 1) # filtring for 1d array

z = x < 50  # x < [100 90 80 70 60 50 40 30 20 10] : [ 6 7 8 9] # filtering element always use condition
print(z, np.where(z))  # if we use where then display index number where condition is true
print(x[z]) # x[6 7 8 9]  # filtring the array element

f = []
for element in x:
    
    if element < 40:
        f.append(True)
    else:
        f.append(False)
new = x[f]
print(f)
print(new)


# ______________________________________________________________________________________________#


arry = np.array(np.arange(1, 10), ndmin = 1)  # [1 2 3 4 5 6 7  8 9]
filter = []  # empty list in filter 
for fil in arry:  # fil = 1 2 3 4  5 6 7 8 9 
    if fil%2 == 0:  # false true false true false true false true false
        filter.append(True) 
    else:
        filter.append(False)
# filter = [False True False True False True False True False]
# In this empty arry is display because each place of item si false and at the false value no item is original 
# dispaly according to sadsified condition  >> filter = [False, False, False, False, False, False, False, False, False] 
print(arry[filter]) # [2 4 6 8]  >> all the number or item of array is display where true value is occure in filter array



# small example of filter
p = np.array([1, 2, 3, 4], ndmin = 1)
x = [False, True, True, False] # 
print(p[x]) # it means in p array the value where True is exist only on that place original value of ndarray is display it 
# Now on most important think this is when we filter the it is nacessary the total bool number of item and total original item of nd array
# is same {{{ otherwise Error are occure (INDEX error) }}}} called the filternig of ndarray elements .
#         {{{ if we use python method like x[p] means array contain numpy array then type error occure}}}
