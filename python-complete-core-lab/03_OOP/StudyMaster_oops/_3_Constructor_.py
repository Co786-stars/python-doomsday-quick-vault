"""
________________________________________________________________________________________________________________________
> In this module we are going to Discuss _________Constructor & it's type in python___________
________________________________________________________________________________________________________________________

A constructor is a special type of method in object-oriented programming that is automatically invoked(called) when an
object of a class is instantiated(created).

when we create an object, constructor(__init__) is automatically invoked(called) this method is used to initialize the object's attributes.
It is  one of the special methods in Python, often referred to as a “magic method” or "dunder methods" because it has double underscores before
and after its name (__init__) followed by parentheses.

We use self as the first parameter in the __init__() constructor to pass the reference to the current instance of the class.
When an object is created, self allows access to the object's attributes and methods, effectively linking the constructor
to the specific memory location of that object.


Types of constructor that we use in python?
✔️ Default Constructor (non-parameterized)
✔️ Parameterized Constructor
⚠️ Copy Constructor
⚠️ Private constructor
⚠️ Simulated Overloaded Constructor
❌ No static constructor in Python

Default constructor : -
A default (non-parameterized) constructor in Python is a constructor that only takes self and requires no arguments
from the user when creating an object. it is commonly use in all OOPs based language python, java, c#, c++.
syntax :

class Default:
    '''try to display default constructor'''
    def __init__(self):   # Default/non parameterize constructor
        self.attr = "values" # self is a label or pointer that help to access the objects attributes(variable)
obj = Default() # pass memory reference to self
print(obj.attr) # out : values


Parameterized Constructor:
A parameterized constructor is a constructor method in Python that accepts self and requires additional arguments from the user when
an object is instantiated(created). This allows us to initialize the object with specific values at the time of its instantiation.
It is commonly used in all object-oriented programming languages such as Python, Java, C#, and C++.

syntax :-
class Parameterized:
    '''try to display Parameterized constructor '''
    def __init__(self, arg1, arg2): # parameterized Constructor(takes additional argument from user)
        self.fst = arg1
        self.snd = arg2
obj = Parameterized("hello", "everyone") # passed the positional argument During instantiation
print(obj.fst, obj.snd) # out : hello everyone

How it works : -
when an object is instantiated, the constructor (__init__) assigns values to instance variables like fst and snd using the self reference
These variables are stored in the object’s memory space in RAM, which is volatile. This means they are only accessible during runtime.
Once the object is destroyed or the program ends, the memory is released and the data is no longer accessible.

self is not a variable that stored in memory, it is  just a reference (pointer or label) to the current object in memory (in RAM) that use to
initialize attributes(variable) during runtime of program.


fst and snd(attributes) are instance variables (attributes) of the object that stored inside the object’s memory, which is allocated in RAM (not ROM).
which is volatile memory, means it is cleared when the program ends.



Copy Constructor:
A copy constructor is a special constructor used to create a new object as a copy of an existing object.
Python does not have a built-in copy constructor, but we can simulate this behavior using
the copy module (copy.copy() and copy.deepcopy())
Custom methods like __copy__() and __deepcopy__()

Note :
In Python, the concept of a copy constructor isn't built into the language like in C++,
but we can implement similar functionality

There are two main ways to implement a copy constructor in Python: using built-in methods like deepcopy or shallow copy.
Additionally, Python's object-oriented programming (OOP) allows for a custom approach using the special methods __copy__ and __deepcopy__.

The basic difference between them is that deepcopy creates a completely independent copy and does not affect the original data,
whereas shallow copy creates a new object but shares references to nested objects, so changes in the copy may affect the original.

What is memo in __deepcopy__(memory_reference, memo) ?
When Python calls copy.deepcopy(obj), it internally uses a dictionary called memo
In simple way memo is a dictionary passed by the deepcopy() function.
Track already copied objects (by their id).
Avoid infinite recursion in case of circular references.
Preserve shared references in the copied object.

syntax basic:(1)
import copy
class Copy:
    def __init__(self, arg="Hello everyone"):
        self.var1st = arg
obj = Copy() # Original object
obj2 = copy.copy(obj) # Copy object
print(obj.var1st, obj2.var1st) # Attributes is accessible from both object


Syntax ShallowDeep method:(2)
import copy
from copy import deepcopy
class ShallowDeep:
    # class try to display difference between shallow and deep copy
    def __init__(self):
        self.lst = [[10, 20, 30],
                    [40, 50, 60]]

    def display(self):
        #display the shallow and deep copy method
        shallow_copy = copy.copy(self.lst) # shallow copy implementation method
        deep_copy = deepcopy(self.lst)
        self.lst[1][2] = 70  # when original lst is change then we see the changes effect on copy lst. [[10,20,30], [40, 50, 70]]
        print(f"Shallow copy : {shallow_copy}") # we see the original data value is changed in shallow copy method
        print(f"Deepcopy : {deep_copy}") # we see the original data value is not changed in Deep copy method [[10,20,30], [40, 50, 60]]
obj = ShallowDeep()  #instanstation
obj.display() # function call

#Syntax Custom ShallowDeep constructor:(3)
import copy
class CustomImplementation:
    def __init__(self, name, data):
        self.name = name # name of person
        self.data = data  # mutable object

    def __copy__(self): # custom shallow copy implementation
        return CustomImplementation(self.name, self.data)

    def __deepcopy__(self, memo): # custom deepcopy implementation
        self.x = memo
        return self.x, CustomImplementation(copy.deepcopy(self.name, memo),
                                    copy.deepcopy(self.data, memo))

    def __str__(self):
        return f"data = {self.data}"

obj = CustomImplementation("wizard", [1, 2, 3])
shallow = copy.copy(obj) # triggers a shallow copy operation
deep = copy.deepcopy(obj) # triggers a deep copy operation

# Modify original data
obj.data.append(4)

print("Original :", obj) # original data [1, 2, 3, 4]
print("Shallow  :", shallow) # changed original state of data value [1, 2, 3, 4]
print("Deepcopy :", deep) # not change the original state of data value [1, 2, 3]



Private constructor : -
A private constructor is a special type of constructor that prevents external code from creating new instances of a class directly.
the class itself controls how and when instances are created. we don't have truly private constructors like in some other languages,
but we can simulate the behavior
In simple way : -
private constructor is a concept mostly found in languages like Java or C++, where we can restrict the creation of objects from outside the class.
Purpose of private constructor:-
To control how objects are created.
To prevent direct instantiation of a class.
Often used in design patterns like Singleton, Factory, or Utility classes.

Syntax:(1)
class PrivateConstructor:
    '''Class is trying to demonstrate private constructor like in other languages'''
    _allow = False  # Internal flag to control access

    def __init__(self):
        if not PrivateConstructor._allow:  # (not false):True
            raise Exception("We cannot access constructor directly by creating object")
        self.message = "This is a simulation of private constructor like other languages"

    @classmethod
    def instance_create(cls):
        cls._allow = True
        obj = cls()  # cls() means calling the constructor
        cls._allow = False
        return obj

# obj = PrivateConstructor()  # This will raise an exception
var = PrivateConstructor.instance_create()  #  This works
print(var.message)

# Private constructor simulation work in python (Explain)
# step1 =  Class is loaded
#           Python reads the class PrivateConstructor.
#           It stores the methods (__init__, instance_create) in memory.
#           But it does not run anything yet — no object is created.

# step2 = Internal flag is set
#          _allow = False by default.
#          This flag is used to block direct object creation.

# step3 =  we try to create object directly -> [obj = PrivateConstructor()]
#          Python calls __init__().
#          Inside __init__, it checks -> [if not PrivateConstructor._allow:]
#          This is True because _allow = False.
#          So Exception is raised(execute) that block the direct object creation
#          So we need simulating a private constructor.

# step4 =  we try to use class method [var = PrivateConstructor.instance_create()]
#          after that python invoke class method instance_create() and in inside .
#          _allow = True → unlocks the constructor.
#          cls() → creates the object (calls __init__()).
#          _allow = False → locks the constructor again.
#          Object is created successfully and stored in var.

# step5 = Now we are able to access the object and its data outside the class indirectly
#         via using class method var.message



Syntax:(2)
class NoDirectCreation:
    def __init__(self):
        raise Exception("Direct creation not allowed. Use get_instance().")

    @classmethod
    def get_instance(cls):
        obj = object.__new__(cls)
        obj.message = "Created via class method"
        return obj

# obj = NoDirectCreation()  #  Raises Exception
obj = NoDirectCreation.get_instance()  #  Works
print(obj.message)

# step1 = Python read the entire class and load whole methods in memory
#         But not Executed before instantiation(object creation) yet

# step2 = We try to create the object from NoDirectCreation()
#         __init__ constructor is auto initialize and raise
#         Exception that block direct object creation

# step3 = So we Invoke get_instance() using class method
#         obj NoDirectCreation.get_instance()

# step4 = Inside the get_instance() new object is created indirectly
#         using __new__(cls) constructor from NoDirectCreation class
#         Now create message attribute from obj(instance/object) and assign value in it
#         after that we return obj to calling the class method

# Step5 = we are access the attribute indirectly from class method
#         that whole is process define how we create simulation of private constructor indirectly in python


Simulated constructor overloading:-

Static constructor not use in python: -
There is no concept are use in python for static constructor But, we use @staticmethod or class-level initialization
logic as an alternative option but this method is not enough or doesn't look like static behaviour like c#.

"""


# Basic :VVI -
# ✔️ Default Constructor (non-parameterized) : Defined as __init__(self) with no parameters (except self)
# ✔️ Parameterized Constructor :               Define as __init__(self, .....) with parameters
# ⚠️ Copy Constructor :                        Python uses copy module or custom methods (__copy__, __deepcopy__)
# ⚠️ Private constructor :                     Simulated using name mangling (__init__ with classmethod or metaclass)
# ⚠️ Simulated Overloaded Constructor          Simulated using default arguments or @classmethod patterns
# ❌ No static constructor in Python :         No native static constructor; use @staticmethod or class-level setup


# Python does not support constructor overloading natively.
# We simulate it using default arguments or factory methods.

# Copy constructors are not built-in.
# We use copy.copy() or copy.deepcopy() for similar behavior (simulation).

# private constructor in Python is a constructor that restricts direct object creation
# Private constructors can be mimicked using class methods or metaclasses
# to restrict instantiation and control object creation.


# Static constructors are not available in Python.
# We can use @staticmethod or class-level initialization logic as an alternative.

# C#     : Except(Copy constructor)
# C++    : Except(Static constructor)
# Java   : Except(Static or copy constructor)
# Python : Except(Static constructor)
#          Mostly used(default, Parameterized constructor)
#          Simulate  behaviour(Overloaded, Copy, Private, constructor)
#          Note : In python we display similar behaviour of constructors that use in other language


'''
________________________________________________________________________________________________________________________
extra :- ------
________________________________________________________________________________________________________________________

Program to Understand the concept of custom copy constructor implementation in python 
it's necessary to known how __str__ works. that given below  

class Func:
    """check how str work"""
    def __init__(self, name, age):
        """constructor initialize the attributes"""
        self.name = name
        self.age = age

    def __str__(self):
        # print(f"my name is {self.name}") Typeerror are appear
        return f"my name is {self.name}"
obj = Func("Wizard", 20) # method calling
print(obj)
# How interpreter read the program Explain : -
# step1 = Python(interpreter) reads the entire class block, not just the class name.
#         It loads all methods (__init__, __str__, etc.) into memory.
#         But it does not execute any method yet.

# step2 = After Instantiation (when we create/write object/obj=Func("wizard", 20)).
#         Python calls the __init__ constructor.
#         It creates the object and sets self.name = "Wizard" and self.age = 20.

# step3 = When we write print(obj)
#         Python looks for the __str__ method.
#         It calls __str__ and expects it to return a string.
#         But in the line that given below we print string but doesn't return any string.
#           def __str__(self): #So Python get automatically None and print(obj) is fail with. [Display:(TypeError __str__ return non-string (type NoneType)]
#                  print(f"my name is {self.name}") # correct way : - return f"string value is necessary"
# step4 = When we return string then there is no error is  display in output screen.

'''

# Extra  confusion concept : -
# step3 = When we write print(obj)
#         Python looks for the __str__ method.  #|-------->   but How does Python know to use __str__()?
#                                                             When Python sees print(obj), it does not just print the object directly. Instead, it follows a protocol:
                                                #|--------->  because it reads the class definition before instantiation or load in memory . Python knows about __str__()
                                                #|--------->  print(obj) internally calls obj.__str__() and expects a string. if __str__() is not defined, it falls back to __repr__() method.
#         It calls __str__ and expects it to return a string.
#         But in the line that given below we print string but doesn't return any string.
#           def __str__(self): #So Python get automatically None and print(obj) is fail with. [Display:(TypeError __str__ return non-string (type NoneType)]
#                  print(f"my name is {self.name}") # correct way : - return f"string value is necessary"

#extra
class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.name = "wizard"
            Singleton.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
        return cls.__instance
# __init__ is not directly accessible for creating multiple instances, and get_instance() controls access sso it is private constructor.