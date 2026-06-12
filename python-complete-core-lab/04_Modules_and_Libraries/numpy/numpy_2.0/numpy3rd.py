
#  Now the numpy Lession : ---------
import numpy as np
arr1 = np.arange(10)         # [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = np.arange(1, 10, 2)   # [1, 3, 5, 7, 9]
arr3 = np.arange(0.3, 1, 0.3)  # [0.3, 0.6. 0.10, .. ]
arr4 = np.array([10, 20, 30, 40])
print(arr1, arr2, arr3)
print(arr4)

"""
explanation : -

> Import function is use to import numpy as(alias) np

> numpy.arange() is a function in the NumPy library that used to create arrays with 
  regular incrementing values

> numpy.arange([start, ]stop, [step, ], dtype=None, *, like=None)
  start: The starting value of the range (inclusive). The default value is 0.

  stop: The end value of the range (exclusive).

  step: The spacing between consecutive values. The default value is 1.

  dtype: The type of the output array. If not given, it is inferred from the input.

  like: Reference object to allow the creation of arrays which are not NumPy arrays.  
  If an array-like passed in as like, it ensures that the result is compatible with it.
"""

