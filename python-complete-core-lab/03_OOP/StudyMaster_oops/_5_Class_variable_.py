"""
> In this module we are going to Discuss ____________________________Class variable

________________________________________________________________________________________________________________________
🍎
As we know, a variable is a type of container used to store data values in task-oriented or functional programming and
in functional or task oriented programming, we refer to them as variables, whereas in OOPs they are often called attributes.
Ex --> var       : call var is variable in functional programming
   --> self.var  : call var is variable in OOps based programming

In functional programming, variables are typically categorized as:
local variable Global variables.

Local Variables:
Defined inside a function.
Accessible only within that function.
Created when the function is invoked and destroyed when the function ends.
Can behave like global variables by using the global keyword

Global Variables
Defined outside all functions.
Accessible from any function within the same program.
hared across the entire codebase and easily accessible throughout the code.



🍎
In OOP, variables are often referred to as attributes, which are typically categorized into :
instance variables and class variable

Instance Variable:
A variable created for a specific instance of a class.
A separate copy is maintained for each object.
Modification in one object does not affect others.
The value of the variable can differ from object to object.
Instance variables are usually defined inside the constructor (__init__ method in Python).
They are accessed using the object reference.
Useful when each object needs to store unique data

Syntax:(1)
class Xyz:
    '''class body define the class variable'''
    var = 'class variable' # class variable
    def __init__(self):
        pass


Class Variable:
Class variables are defined for the entire class, not for individual instances.
They are typically declared at the top of the class, outside any methods.
Unlike instance variables, which create a separate copy for each object, class variables have only one shared copy across all objects.
Every object of the class can access and share the same class variable.
The value of a class variable remains the same for all objects unless explicitly changed at the class level.
Class variables can be accessed in two ways: using the class reference or using the object reference.

Syntax:(2)
class Pqr:
    '''class body try to display the instance variable'''
    def __init__(self):
        self.var = 'instance variable' #instance variable

Syntax:(3)
class LocalClassVariable:
    '''class body is try to display instance and class variable'''
    var1 = "wizard" # class variable (shared across all instances)

    def __init__(self):
        self.var2 = 30  # instance variable (unique to each object)

    def define_func1(self):
        self.var3 = [20, 40] # instance variable (created via object reference)

    @classmethod
    def define_func2(cls):
        cls.var4 = {2+0j, 3j} # class variable (created via class reference)


    def define_func3():
        var5 = {'key1':'value1', 'key2':'value2','key3':'value3'}  # Local variable (not a class or instance variable)
        # print(var5) # inside we easily access var5 but outside the class we can't without using reference
        return var5 # but we use return to calling method to access var5 attribute value

    @staticmethod
    def define_func4():
        var6 = (10, 20, 30) # Local variable (not a class or instance variable)
        # print(var6) # @staticmethod works like any other regular function inside a class — it does not require self or cls.
        return var6 # In simple way this method works as it is like define_func3(regular method inside the class)

#method calling/invoked
obj1 = LocalClassVariable() #
obj2 = LocalClassVariable #

#display attributes
print(obj1.var1)
print(obj1.var2)

obj1.define_func1() # when we invoked define_function1 then var1 store list value
print(obj1.var3) # when we use directly obj1.var3 attribute error are generate

obj1.define_func2()
print(obj1.var4) # access attribute using memory reference
print(LocalClassVariable.var4) # access attribute using class reference

print(obj2.define_func3()) # returned value is display via pridefine function print
# print(obj2.var5) # Attribute error are generate only accessible inside the function

Explanation why not accessible : -
# Why print(obj2.var5) gives an error:
# We are trying to access a variable that was never attached to the object neither (self) nor class (cls).
# Python looks for var5 in the object’s attributes and doesn’t find it. Because var5 is created within the
# same scope (inside the method), it is accessible only there(inside the function).

# var5 is a local variable.
# It only exists inside the method define_func3().
# Once the method finishes running, var5 is destroyed.
# That’s why we cannot access it using obj2.var5 or LocalClassVariable.var5.



print(obj1.define_func4())  # Accessing returned value from static method (similar working style like regular method)
# @staticmethod( define_func4 ) == Regular method inside the class( define_func4 )


# explanation : - Why both are similar @staticmethod == regular functional
# The static method 'define_func4()' does not use `self` or `cls` so it cannot access instance or class
  variables directly. However, it works like a regular function inside the class.

# We can access its internal data (like var6) outside the class by using a return statement, just like we do in
  a normal method.

# In this way, both `@staticmethod` and a regular method (without self) behave similarly when it comes to handling
  local variables.

# They are functionally the same in terms of scope and access — either can access object or class attributes unless
  explicitly passed.

_______________________________________________________________________________________________________________________


"""




