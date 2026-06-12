"""
# Built-in class attribute --------------Built-in class attribute ------------Built-in class attribute -------------------------#
__dict__     : attribute is a dictionary object that contains attributes information defined for that object
__doc__      : attribute in Python is used to access the documentation string (docstring) of a module, class, method, or function. 
__name__     : attribute used to identify the module's name and exists in every Python module  When a module is run directly.
___module__  : attribute is used to indicate the name of the module in which a class or method is define
__bases__    : attribute in Python is used to access a tuple containing the base classes of a class. 
__class__    : attribute in Python is used to reference the class to which an object belongs
"""

class Book:
    "collecion of book"
    pass
obj1 = Book()


class Boys:
    """ Class body for  group of boys"""
    def method(self):
        """ Body is use to store the name of boys"""
        print("hello")
    pass

print(Book.__dict__)
print(Boys.__doc__)  
print(Boys.method.__doc__)
print(__name__)    # output :: __main__  # that identified you are in current module means main module 
print(obj1.__class__)   # output :: <Class ' __main__Book'>  # __main__ is indicate class Book is avilable in current module (file)
print(Book.__module__)

# ----------------------------------------------------------
# >> This shows that the Dog class inherits from the Animal class Is there a specific scenario you’re working
#    on where you need to use the __bases__ attribute
# >> This attribute provides information about the direct parent classes from which the class inherits.
class Animal:
    pass

class Dog(Animal):
    pass

print(Dog.__bases__)  # output :: (<Class '__main__'.Animal)





