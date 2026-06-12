"""
In this session we are discuss about Numpy datatype for python
>> There are two common datatype use in python primitive and non primitive
>> The given data type is the part of premitive datatype
>> string >> float >> int >> complex
>> The given data type is the part of non premetive datatype
>> arrray >> tuple >> list >> complex  >> dict >> set

>> Now we study about numpy datatype : -
In numpy there are single-chracter codes that represent different datatypes.
these type code make it eaiser to work with arrays and perform efficent operations.
'i' = integer
'f' = float
'c' = complex
'b' = Boolean
'S' = String
'U' = Unicode string
'u' = unsigned integer
'O' = object
'M' = datetime
'm' = timedelta
"""
import numpy as np
arr1 = np.array((np.arange(1, 6)), ndmin = 1)
arr2 = np.array(['str1', 'str2', 'str3', 'str4'], ndmin = 1 )
print(arr1.dtype) # numpy.dtype is a property that define datatype of array int64 = 64 is size
print(arr2.dtype) # ......... output : U4 means : usignned string and 4 is size

ary = np.array([1, 2, 3, 4], dtype = 'S') # we use array() to create ndarray and with the array() 
print(ary)  # use it or define the dtype property as well. output :- [b'1', b'2', b'3', b'4']   b(boolean)
print(ary.dtype) # the datatype i, u, f, s, and U define size as well output: S1 = means string and 1 is size

ary2 = np.array([1, 2, 3, 4], dtype='i4')  # create an array with 4 bytes datatype integer
print(ary2)
print(ary2.dtype)

# ary = np.array(['a', '2', '3'], dtype = 'i')
# print(ary) # value error is generated 
# print(ary.dtype) # value error are generated

# converting the datatype on existing arrray
# to converting the datatype in existing array is to make a 
# copy of the array with the astype() method

# Now

#convert the float in int using numpy datatype 'i'
aray = np.array([1.1, 2.1, 3.1, 4.1])
print(aray) # [1.1 2.1 3.1 4.1]
new = aray.astype('i') # astype() function is convert the whole value of ndarray in int format means 
print(new) # it copy the value or display it

#convert ndarray in int using int keyword 
aray2 = np.array([1.1, 1.1, 1.1, 1.1])
var1 = aray2.astype(int)
print(var1) # [1 1 1 1]
print(var1.dtype) # int64


#convert the ndarray elsements into bool (True either False)
aray3 = np.array([1.2, 0, 1.4])
var2 = aray3.astype(bool)
print(var2)  # [True False, True]
print(var2.dtype)  # bool


