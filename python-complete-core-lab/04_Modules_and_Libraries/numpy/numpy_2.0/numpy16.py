"""
Note: -

numpy.sort() function
attribute.sort() function 
sorted() function
"""

# In this module we are discuss about sort function that is also read in previous session of list 
# we all are known sorting means putting the element in orderd sequences
import numpy as np
x = np.array([10, 30 ,50, 20, 70, 40, 90], ndmin=1)
# x.sort()  # this method is use for list array when we want to parmamently sort the item of array
# print(sorted(x))    # we use x.sorted method for temporary sort the array element
print(np.sort(x)) #  But carefull in numpy sort() function sort the ndarray for tempoary 
print(x)          #  but in python it arrange the array parmently


arr = np.array(['hello', 'python', 'awake', 'wizard'], ndmin = 1)
# arr.sort()  # this method is also sort array parmanently in list aaray but in nd array the method  
# print(arr)  # nd.sort(parameter) is not arrange item parmanently
# print(np.sort(arr))  # nd.sort() is use to sort the ndarray element for temporary time 
# print(sorted(arr))   # this method is also use to sort the array for temporary time

arr = np.array(np.arange(100, 10, -10), ndmin = 1)
new = arr.reshape(3, 3)
print(new)
print(np.sort(new))


"""

Explanation : --

import numpy as np

# Create an array
ndarr = np.array(np.arange(100, 0, -10), ndmin=1)

# Use ndarray.sort() for permanent in-place sorting
ndarr.sort()
print(ndarr)

# Output: [ 10  20  30  40  50  60  70  80  90 100]

# Use numpy.sort() for temporary sorting
print(np.sort(ndarr))

# Output: [ 10  20  30  40  50  60  70  80  90 100]

"""



