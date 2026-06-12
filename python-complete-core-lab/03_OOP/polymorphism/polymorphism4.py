# In python programming  iterators are created using iter() function and accessed with the next() function
# In most case iteratorare  use for data handling and created from an iterable object
# The datatype that contain more then one value simultaneously like list, tuple, set, dictonary are iterable with iter().

x = [10, 20, 30, 40]
var1 = iter(x) # iter() is use to count all iterable function 

for i in x:
    print(next(var1)) # we use next() to access the value of iterable datatype



y = iter("Hellowizard")
print(next(y))
print(next(y))




