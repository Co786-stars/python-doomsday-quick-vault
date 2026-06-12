
#-----------------------------Topic of Inheritance-----------------------------------------------Topic of Inheritance------------------
# ----Topic of Inheritance---------------------------------------Topic of Inheritance------------------
# -----------------------------Topic of Inheritance-----------------------------------------------Topic of Inheritance------------------
# ----Topic of Inheritance---------------------------------------Topic of Inheritance------------------

'''
     Inheritance
     Multipal Inheritance
     Multi level Inheritance
     method Overriding in python
     Operator Overloading in python 
     MRO Method Resolution in python
     Super() function in Inheritance

'''


"""
Inheritance : -
Inheritance is an fudmental concept of an OOPs that allow to create a new class based on existing class

Syntax : -

class Parentclass:
    def __init__(self, arg1):
        self.argument1 = arg1

class Childclass(Parentclass):
    def __init__(self, child_arg1):
        self.child_argument = child_arg1

object1 = Parentclass(10)
object2 = Childclass(20)
# object1.child_argument # error are display because we never call child attributes from parent class 
object2.child_argument   # error are not display because child attribute are are callable from child class
object1.argument1        # error are not display because parent attribute are callable from in parents class
object2.argument1        # error are not display because parent attribute are inherit in child class

Parents class : -

Parents class is the class in which we inherit attributes(property) and method to the child class
It is commonly known as Existing class, superclass, parent class or  base clas

Child class : -

Child class is a class that inherits properties (attributes) and methods from another class.
It is commonly known as new class, subclass, child class or derived class .
We use override method in child class from parents class means modify the behabiour of __init__().

syntax : -

[To do this modification we define an __init__() method in the child class. and if we want to keep
the parent's constructor behavior, call the parent's __init__() using super() function]

class Parentclass:
    def __init__(self, arg1):
        # Initialize parent attributes here
        self.arg1 = arg1

class Childclass(Parentclass):
    def __init__(self, child_arg1):
        super().__init__(child_arg1)  # Call parent's constructor with the child's argument
        # Initialize child-specific attributes here (if needed)

Why we use Inheritance ? 
It promotes code reusability and helps organize your code by creating a hierarchy of related classes.
It provide modularity, maintatence, polymorphism and Efficiency Boost in the programs

"""


