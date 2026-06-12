"""
Basic : - definition 

The isinstance() function in Python is used to check if an object is an instance of a specified 
class or a tuple of classes. It returns True if the object is an instance of the specified class 
or any class in the tuple, and False otherwise.

"""

# -------------------------------------------------------------------------------------------------------------
class Device:
    """class body contain info of device"""
    pass

class Animal:
    """class body contain info of animal"""
    pass
# -------------------------------------------------------------------------------------------------------------

zebra = Animal()
Phone = Device()
x = isinstance(zebra, Device)  # output :: isinstance(object, classinfo)
print(x)

# Normally use to check the class 
x = 5
print(isinstance(x, int))  # Output: True  a simple fucnction that use to check the class of object

y = [1, 2, 3]
print(isinstance(y, (list, tuple)))  # Output: True


