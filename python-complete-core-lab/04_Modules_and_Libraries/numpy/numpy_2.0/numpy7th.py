"""
use of copy and view in numpy module
"""

import numpy 
arr = numpy.array((numpy.arange(10)), ndmin = 1) # ndmin is specifi the ndarray must be 3d
cop = arr.copy() # copy is use to create a new array  
arr[0] = 5  # change the element on 0 index 
print(arr)  # array is disply after change the value
print(cop) # the original state of the array is display


aray = numpy.array([10, 20, 30, 40, 50], ndmin = 1)
viw = aray.view() # view is just a views of original array (means if there is any change
aray[2:4] = [25, 30] # in original state of array then view of behavious is auto change
print(aray) # thats why we say view is just a views of array
print(viw)


# Now concept : - 
"""
> views : if we change the original state of array then this affect on views
> copy :  if we change the original state of array the there is no affect on copy array 
>         because copy array is a new array it not a views of orignal array 
> let     if we change in view then the changes also affect on original array 
"""
ary = numpy.array([4, 3, 2, 1], ndmin = 1)
v = ary.view()
v[0:4] = [1, 2, 3, 4]
print(ary)
print(v)

# Now : when we change the views orginal array should be affected
#       when we change the orginal array views should be affected
#       when we change the orginal array then copy array should not be affected
#       when we change the copy array then original array should not be affected
