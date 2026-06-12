import numpy  # after imported any module we access attribute() of the module using modulename.attribute()
import time # this is time module to calculate month day and date etc.


# first we create using the list 
lst = list(range(1, 10))
initial = time.time()
lst = [x*2 for x in lst]
last = time.time()
print("print python list time ", last - initial)
# output : - 
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = [2, 4, 6, 10, 12, 14, 16, 18 ]

# now we create using the numpy array
arr = numpy.arange(1, 10)
initial = time.time()
arr = arr*2
last = time.time()
print("print python numpy time ", arr-last)


#  explanation : -
# numpy.arange() function is similar as a range() but more faster 
# 