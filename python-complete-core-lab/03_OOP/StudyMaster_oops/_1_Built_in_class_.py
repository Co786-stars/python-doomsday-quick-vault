"""
> In the module we are going to Discuss the topic ________Built-in-class_________.
> In python every thing is an object we use class to manage or create the objects.
> type() is a predefined function in Python that returns the class type of object.

"""

print("type() is a predefined function in Python that returns the class type of an object")

num = 10         # output: <class 'int'>
print(type(num))

var = "string"   # output: <class 'str'>
print(type(var))

com = complex(2) # output: <class 'complex'>
print(type(com))

flt = 20.01
print(type(flt))

bo1, bo2 = True, False   #output <class 'bool'>
print(type(bo1), type(bo2))

lst = [10, 20, 40, "string"] # output: <class 'list'
print(type(lst))

dic = {'key1':10, 'key2':'string', "key3":2j+0, 'key4':0.001} # output: <class 'Dict'>
print(type(dic))

tup = (10, 20, 30, 40, 50) # output: <class 'tuple'>
print(type(tup))


# simple class using function
def func():
    """this is an object"""
    var = "string_value"
x, y = func, func()  # No value is assign in y so None is automatically assign (means Nothing value exist)
print(type(x), type(y)) # <class 'function'>, <class 'NoneType'>


