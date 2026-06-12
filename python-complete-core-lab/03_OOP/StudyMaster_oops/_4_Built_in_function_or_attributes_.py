'''
> In this module we are going to Discuss__________self label(pointer)_____________How to access class member
                                         _____Built_in class function___________Built_in attribute

________________________________________________________________________________________________________________________
🍎
Self(label, pointer) in python ?
self is the standard name for the first parameter in instance methods of a class. It refers to the current object (instance)
and provides access to its attributes and methods.

Although self is not a reserved keyword, and you can technically use any valid name, using self is the recommended convention
in Python for clarity, readability, and consistency

self is not a variable that stored in memory, it is  just a reference (pointer or label) to the current object in memory (in RAM) that use to
initialize attributes(variable) during runtime of program.

Syntax:
class Person:
    """Demonstrates how 'self' works in Python classes."""
    def __init__(self):
        self.name = "Xyz"  # 'self' refers to the current object
obj = Person()
print(obj.name)

# step 1 = Python reads and loads the class definition into memory.
#          No code inside the class is executed yet.
# step 2 = An object of the class is created.
#          Python calls __init__ and passes the object as 'self'.
# step 3 = Access the 'name' attribute of the object.


Syntax:
class SyntaxSelf:
    def __init__(memo_reference): # we use another name at the place of self parameter
        memo_reference.name = "Wizard"
obj = SyntaxSelf() #instantiation
print(obj.name)


________________________________________________________________________________________________________________________
🍎
How to access class member in python ?
In Python, class members (attributes and methods) can be accessed using two main approaches:
instance methods and class methods.

Instance Methods use the keyword self to refer to the current object (instance) of the class.
This allows access to instance-specific attributes and methods using the syntax self.attribute_name.

Class Methods use the keyword cls to refer to the class itself, rather than any particular instance.
This is useful for accessing or modifying class-level attributes using the syntax cls.attribute_name.

Question1
Create a class called Car with attributes brand, model, and year. Add a method called display_info() that prints out the
car's details. Then, create an object of the class, access and print its attributes, call the method, and finally update
the year attribute and print the updated info.

Question2
Create a class called Spaceship with attributes name, mission_type, and fuel_level. Add a method called status_report()
that prints the spaceship's current status. Then, create an object of the class, access and print its attributes, call
the method, and finally update the fuel_level and print the updated status.

# Syntax to access the class member : -
#accessing_attribute : - object_name.variable_name
#accessing_method    : - object_name.method_name()
class Spaceship:
    def __init__(self, *args):
        self.name = args[0]
        self.mission_type = args[1]
        self.fuel_level = args[2]

    def status_report(self):
        print(f"spaceship's current fuel status : {self.fuel_level}") # access the attributes inside the class

#Instantation(object creation)
obj = Spaceship("Vikram s21", "naval attack", 90)

# access the attributes in outside of class
print("ship : ",obj.name, "\nType : ",obj.mission_type,
      "\nfuel :",obj.fuel_level)

# Updating the attribute data value
obj.fuel_level = 70
#method calling
obj.status_report()


________________________________________________________________________________________________________________________

🍎
Built-in Class method in python ?
In python built-in class method is a predefined function that enhances our class behavior or object interaction.
It includes special methods like __init__() for object construction and built-in functions like getattr() for
dynamic attribute access.

Built-in Class method usually belongs to two category first is start and end with double underscores (__).
follow via parentheses which is known as dunder method but on other hands second is end with parentheses
which is known as functional method.

The methods that contain double underscores or are followed by parentheses ( __xyz__() ) are typically defined
inside a class or known as dunder methods or special method and these methods are part of the object’s behavior usually
require self (a reference to the instance) as the first argument for instance methods.
examples : - __init__(self), __str__(self), __repr__(self),
             __len__(self), __call__(self), __getitem__(self, key) .... etc.

Note : -
For class methods, we use cls as the first argument, and they are defined using the @classmethod decorator.
For static methods, we use the @staticmethod decorator, and they do not require any implicit first argument (self or cls).
examples : - __init__(cls), __str__(cls), __repr__(cls),
             __len__(cls), __call__(cls), __getitem__(cls, key) .... etc.


# How to use dunder method
# Syntax:(1)
class DunderMethod:
    """This class demonstrates the use of dunder (double underscore) methods in Python."""

    def __init__(self, y):
        """
        __init__ is a constructor dunder method.
        It is automatically called when an object is created.
        It initializes the object's attributes.
        'self' refers to the current instance of the class.
        it returns None by default, and that return value is not displayed on the screen.
        if forcefully we will try to return other datatype except None it raised an error
        'y' is the value passed during object creation and assigned to self.x.
        """
        self.x = y
        # return 5  # TypeError: __init__() should return None, not 'int' or other datatype

    def __str__(self):
        """
        __str__ is a dunder method used to define the string representation of the object.
        It is called when we use print(obj) or str(obj).
        It must return a string, not print it.
        If it returns None, Python raises a TypeError.
        """
        return f" __str__() String representation : {self.x}"

    def __repr__(self):
        """
        __repr__ is another dunder method used for the official string representation of the object.
        It is mainly used for debugging and logging.
        If __str__ is not defined, print(obj) will fall back to __repr__().
        if in case we want to execute __repr__() directly in the presence of __str__() we use repr(obj)
        """
        return f" __rpr__() DunderMethod(x = {self.x})"

    def __len__(self):
        """
        len__() is a dunder method that is triggered when len(obj) is invoked.
        It is used to return the length of the object.
        It must return an integer value.
        Internally, it uses len(self.data) to get the length of the list.
        If it returns a non-integer, Python will raise a TypeError
        """
        self.lst = 'string'
        # return f"{len(self.lst)}" error are generate but in functional len() error are not generate
        return len(self.lst) # output : 5

# Creating an object using string
obj = DunderMethod('xyz')

# Using the object, that calls __str__() internally
print(obj)

# Using __str__() by accessing 'xyz'
print(str(obj))

# Using __repr__() by accessing 'xyz'
print(repr(obj))

# Using __len__() by indexing item arbitrary argument
print(len(obj))



#Syntax:(2)
class DunderExample:
    """class body try to demonstrate class built-in dunder methods"""

    def __init__(self):
        """
        __init__ is a constructor dunder method.
        It is automatically called when an object is created.
        It initializes the object but does nothing in this case.
        """
        pass

    def __call__(self, *args, **kwargs):
        """
        __call__() is a dunder method that is triggered when obj() is invoked.
        It is used to make the object behave like a function.

        It accepts:
        - *args: Any number of positional arguments.
        - **kwargs: Any number of keyword arguments.

        It returns:
        - A formatted string showing the arguments passed to the object.

        Purpose:
        - Demonstrates how objects can be made callable.
        - Useful in scenarios like decorators, function-like behavior, or dynamic execution.
        - If __call__() is not defined, calling obj() will raise a TypeError.
        """
        return f"__call__() called with args={args}, kwargs={kwargs}"


    def __getitem__(self, key):
        """
        __getitem__() is a dunder method that enables indexing and slicing.
        It is triggered when obj[key] is used.

        Parameters:
        - key (int or str): The index or key to access.

        Behavior:
        - Returns a formatted string showing the key accessed.
        - Demonstrates how objects can behave like containers.
        """
        sample_data = ['laptop', 'mobile', 'chair', 'pen']
        return f"__getitem__() accessed key {key}: {sample_data[key]}"

obj_ = DunderExample()

# Call the object like a function
print(obj_(10, 20, key='value'))
# Output: __call__() called with args=(10, 20), kwargs={'key': 'value'}

# Access the object like a list
print(obj_[1])
# Output: __getitem__() accessed key 1: banana


Syntax:(3)
class AccessAttribute:
    """class body try to access attributes using cls and self parameter"""
    def __init__(self):
        self.name = "wizard"

    @classmethod
    def new_function(cls):
        cls.age = 20

    @classmethod
    def __repr__(cls):
        obj = AccessAttribute()
        cls.new_function()
        return f"my name is {obj.name} and age is {cls.age}"

# y = AccessAttribute.__init__() # out : TypeError
x = AccessAttribute.__repr__()
print(x)

# Interpreter Execution Flow (Step-by-Step)
# Class Definition Phase:
#
# Python reads the entire class body (AccessAttribute) and stores its methods and attributes in memory.
# No code inside the methods is executed yet—only definitions are registered.
# Calling AccessAttribute.__repr__():
#
# This is a direct call to a class method. No object is created yet.
# Since __repr__ is decorated with @classmethod, Python passes the class itself (AccessAttribute) as the cls parameter.
# Inside __repr__:
#
# obj = AccessAttribute() creates an instance of the class.
# This triggers the __init__ method.
# Inside __init__, self.name = "wizard" sets an instance attribute.
# cls.new_function() is called.
# This sets a class-level attribute cls.age = 20.
# The method returns a string using:
# obj.name → instance attribute
# cls.age → class attribute
# Return and Print:
#
# The returned string is stored in variable x.
# print(x) outputs:

# Clarification on cls and Memory Reference
# Even though no object is passed to __repr__, the class itself is passed as cls.
# This is how class methods work: they operate on the class, not on an instance.
# The memory reference of the class (AccessAttribute) is passed to cls, allowing access to class-level attributes and methods.




The methods that are followed by parentheses (like xyz()) may be defined by us or provided by Python as built-in functions.
These are typically used to interact with objects, such as accessing or modifying attributes. Most importantly, they are
usually used outside the class.
example : - getattr(), setattr(), hasattr(), delattr(), isinstance(), issubclass(), type(), id(), dir(), vars()
            callable(), help(), repr(), str(), format(), len(), abs(), sum(), max(), min() etc...

Syntax : -
class Student:
    def __init__(self, name, age, grade):
        # constructor is initialized the attribute
        self.my_name, self.my_age = name, age
        self.my_grade = grade

    def func(self):
        pass

    def func2(self):
        # method is show how format work
        self.name, self.roll, self.color = "xyz", 231.0000001, 'gray'
        return "{} {:.2f} {Eye_color}".format(self.name, self.roll, Eye_color = self.color)

# calling the method
obj = Student("wizard", 21, "A++")

print(getattr(obj, 'my_name'))
# is used to get the value of an attribute by name
# syntax : getattr(object_name, attribute_name)

print(hasattr(obj, 'my_grade'))
# is used to check if the object has a specific attribute
# syntax : hasattr(object_name, attribute_name)
# commonly known as attribute checker → returns True or False

print(isinstance(2, Student))
# is used to check if an object is an instance of a class
# syntax : isinstance(object_name, class_name)
# commonly known as type checker → returns True or False


print(vars(obj))
# is used to inspect the object details in dictionary form
# syntax : vars(object_name)
# commonly known as object inspector → shows all attributes and their values

print(help(obj))
# is used to show the documentation of the object/class
# syntax : help(object_name)
# commonly known as doc viewer → shows class docstring and method info


print(callable(obj.__init__))
# is used to check if an object or method is callable (like a function)
# syntax : callable(object_name or method_name)
# commonly known as function checker → returns True or False


delattr(obj, 'my_name')
print(obj.__dict__)
# is used to delete an attribute from an object
# syntax : delattr(object_name, attribute_name)
# commonly known as attribute remover → check using __dict__


setattr(obj, 'my_degree', 'technical')
print(obj.__dict__)
# is used to set or update an attribute value
# syntax : setattr(object_name, attribute_name, new_value)
# commonly known as attribute setter → adds or updates attribute


print(obj.func2())
# is used to format strings with placeholders
# syntax : "text {}".format(value)
# commonly known as string formatter → used for clean output

print(str(obj.my_grade), repr(obj.my_grade))
# str is used to convert any datatype into string (without quotes)
# repr is used for debugging, returns string with quotes
# syntax : str(object_name), repr(object_name)
# str → string converter | repr → representation (debug-friendly)

print(dir(obj))
# is used to list all attributes and methods of an object
# syntax : dir(object_name)
# commonly known as object explorer → includes built-in and user-defined

print(id(obj))
# is used to get the unique ID (memory address) of the object
# syntax : id(object_name)
# commonly known as memory locator → valid during object lifetime


Is the both are class method ?
Yes both are the class method but :
__init__() is a method/function (inside class, part of object behavior).
getattr() is a built-in function (outside class, part of Python tools).

Questions : -
Create a class Student with attributes name, age, and grade. ? Then use given method :
getattr(), delattr(), hasattr(), setattr()


Create a class ShoppingCart that stores a list of item prices. ?
Write a Python class GitHubUser that takes a GitHub username and fetches public profile data using the GitHub API.
Create a class Product that represents an item from Amazon. Use web scraping (e.g., with BeautifulSoup) to fetch product details like name, price, and rating.



________________________________________________________________________________________________________________________
🍎
Built-in class attribute in python ?
Built-in class attribute in Python is a predefined, non-callable property automatically associated with a class or its
objects, used to store metadata or structural information (e.g., __dict__, __doc__, __class__).

Built-in class attributes stated with double underscore or they don't follow parentheses like built-in class methods
they just hold data or metadata or non-callable.
example :-  __name__, __dict__, __doc__, __class__, __module__, __bases__
            obj.__dict__, MyClass.__doc__

How to know method and attributes ?
parentheses = function
Double underscores + parentheses = function
Double underscores without parentheses = attribute


#Syntax:(1)
class Book:
    """class body is trying to define attributes"""

    # __annotations__ can be used to store type hints. is it is necessary ?
    # No, using __annotations__ is not necessary in Python — it's completely optional.
    comp: list
    dict: dict
    lit: tuple

    def __init__(self):
        """constructor initializes attributes"""
        self.comp = ['python', 'c++', 'java']
        self.dict = {'Nda': 'pathfinder', 'cds': 'ncrtc'}
        self.lit = ('Hindi', 'sanskrit', 'veda')

# Create an instance of the Book class
obj = Book()

# __dict__ shows all attributes of the object in dictionary format
print("dict        : ", obj.__dict__)  # defines this attribute: syntax → obj_name.__dict__
# dot (.) helps access the attribute and shows instance variables as a dictionary
# __doc__ returns the docstring of the class
print("doc         : ", obj.__doc__)  # defines this attribute: syntax → class_name.__doc__
# used to access documentation string written inside triple quotes

# __name__ returns the name of the current module
print("name        : ", __name__)  # defines this attribute: syntax → __name__
# when running directly, it returns "__main__"

# __class__ returns the class to which the object belongs
print("class       : ", obj.__class__)  # defines this attribute: syntax → obj_name.__class__
# shows the class type of the object

# __module__ returns the name of the module in which the class is defined
print("module      : ", obj.__module__)  # defines this attribute: syntax → obj_name.__module__
# usually "__main__" if defined in the same script

# __annotations__ shows type hints defined in the class
print("annotations : ", Book.__annotations__)  # defines this attribute: syntax → class_name.__annotations__
# shows type hints for attributes (if any are declared)

# __init__ is the constructor method used to initialize object attributes
print("init        : ", Book.__init__)  # defines this attribute: syntax → class_name.__init__
# shows the reference to the constructor method

# __class__.__name__ gives the name of the class as a string
print("name        : ", obj.__class__.__name__)  # syntax → obj_name.__class__.__name__
# useful for logging or debugging class names


# Syntax:(2)
class X:
    pass

class Y(X):
    pass

z, y = X(), Y()

# __bases__ returns a tuple of base classes from which the class inherits
print("base        : ", Y.__bases__)  # defines this attribute: syntax → class_name.__bases__
# shows the parent classes of Y (in this case, X)

# __mro__ shows Method Resolution Order (important in multiple inheritance)
print("mro         : ", Y.__mro__)  # defines this attribute: syntax → class_name.__mro__
# shows the order in which classes are searched for methods

# __subclasses__() returns a list of immediate subclasses of a class
print("subclass    : ", X.__subclasses__())  # defines this attribute: syntax → class_name.__subclasses__()
# shows all classes that directly inherit from X
# Type: this Class method (not an attribute) because it is callable

# __sizeof__ returns the size of the object in bytes
print("size        : ", obj.__sizeof__())  # defines this attribute: syntax → obj_name.__sizeof__()
# useful for memory profiling


________________________________________________________________________________________________________________________
Note : -

✅ 💫💫💫 Examples 💫💫💫

Attributes:(non-callable)
__dict__, __doc__, __class__, __module__
Accessed like: obj.__dict__, MyClass.__doc__

Methods:(callable, dunder method)
__init__(), __str__(), __len__()   # category 1st
Called like: obj.__str__(), len(obj)

Methods:(callable, functional method)
getattr(), delattr(), hasattr(), setattr() #category 2nd


🍎 Object Initialization and Representation
   __init__(self, ...) – Constructor, called when an object is created.
   __new__(cls, ...) – Used to create a new instance; rarely overridden.
   __del__(self) – Destructor, called when an object is about to be destroyed.
   __str__(self) – Defines the “informal” or nicely printable string representation of an object.
   __repr__(self) – Defines the “official” string representation of an object.


🍎 Attribute Access and Management
   __getattr__(self, name) – Called when an attribute is not found.
   __getattribute__(self, name) – Called for every attribute access.
   __setattr__(self, name, value) – Called when an attribute is set.
   __delattr__(self, name) – Called when an attribute is deleted.


🍎 Operator Overloading
   __add__(self, other) – +
   __sub__(self, other) – -
   __mul__(self, other) – *
   __truediv__(self, other) – /
   __floordiv__(self, other) – //
   __mod__(self, other) – %
   __pow__(self, other) – **
   __eq__(self, other) – ==
   __ne__(self, other) – !=
   __lt__(self, other) – <
   __le__(self, other) – <=
   __gt__(self, other) – >
   __ge__(self, other) – >=


🍎 Type Conversion
   __int__(self) – Converts to int
   __float__(self) – Converts to float
   __complex__(self) – Converts to complex
   __bool__(self) – Converts to bool
   __bytes__(self) – Converts to bytes
   __str__(self) – Converts to str


🍎  Container Emulation
    __len__(self) – Returns length
    __getitem__(self, key) – Access item
    __setitem__(self, key, value) – Set item
    __delitem__(self, key) – Delete item
    __contains__(self, item) – in operator


🍎  Iteration and Callable
    __iter__(self) – Returns iterator
    __next__(self) – Returns next item
    __call__(self, ...) – Makes an object callable like a function


🍎  Context Management
    __enter__(self) – Called when entering a with block
    __exit__(self, exc_type, exc_val, exc_tb) – Called when exiting a with block

"""

# Basic :VVI
# How to clear the confusion b/w both methods :
# Built-in class Dunder method | Built-in class functional method read below : -

# 🍎 Dunder Methods (Special Methods)
#         Format:    __method__()
#         Examples:  __init__(), __str__(), __repr__(), __len__(), __call__(), __getitem__(), etc.
#                    Called dunder methods (double underscore)
#                    Used inside classes
#                    Control object behavior with built-in functions

# 🍎 class Built-in Functional method
#         Format:   function_name()
#         Examples: getattr(), setattr(), hasattr(), delattr(), isinstance(), type(), id(), dir(),
#                   vars(), callable(), help(), str(), repr(), format(), len(), sum(), max(), min(), etc.
#                   Called built-in functions
#                   Used outside or inside classes
#                   Work with attributes, objects, types, and data

# Both use () but:
# __xyz__() → dunder method (special method)
# xyz() → built-in function
'''


"""
# Other topic related
class A:
    @classmethod
    def show(cls):  # class method
        print("abc")

class B:
    def show():  # Regular method
        print("xyz")

class C:
    @staticmethod # static method
    def show():
        print("pqr")

class D:
    def show(self): # instance method
        print("lmn")

# Call as class method
A.show() # class_name.attribute

# Call as regular class method
B.show() #class_name.attribute

# Call as static method
C.show() #class_name.attribute

# Call as instance method
# D.show() #class_name.attribute not work
D().show()

# Method Type	     Decorator	    First Parameter	   Called As	      Needs Object?	   Memory Reference Passed
# Instance Method	 None	        self	           obj.method()	      ✅ Yes	       Instance reference
# Class Method	     @classmethod	cls	               Class.method()	  ❌ No	           Class reference
# Static Method	     @staticmethod	None	           Class.method()	  ❌ No	           Nothing passed
# Regular Function	 None	        None	           Class.method()	  ❌ No            Nothing passed

# Define this obj = Xyz() core concept ?

# Is obj = Xyz() the instance or is Xyz() the instance?
# Xyz() is the actual instance — the object created in memory.
# obj is just a variable that holds the reference to that instance.
# So when we write obj = Xyz(), we are saying:
# "Create an instance of Xyz and store its reference in obj."
# Think of Xyz() as the factory that creates the object, and obj as the box where you store it.
"""

class X:
    def __init__(self):
        print("hello")

    def __call__(self):
        print("wizard")

obj = X()
obj()
#         __call__() is a dunder method that is triggered when obj() is invoked.
#         It is used to make the object behave like a function.

