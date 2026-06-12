#  Types of method in oops : -
#  Instance method 
#  Class method
#  Static method 

# If any problem then read the toic we only read  :>> How to create method, What is method, type of method 
# read topics that given below : -  
 
# (1) How to call class methods and static methods 
# (2) what is the difference between all of three method
# (3) When we use instance, static or class method and why we use 

""""
Instance Methods: Use the self parameter and are defined without any decorator. They operate on an instance of the class.
def instance_method(self):
    pass
    
Class Methods: Use the cls parameter and are defined with the @classmethod decorator. They operate on the class itself.
syntax : -
@classmethod
def class_method(cls):
    pass

Static Methods: Don't use self or cls and are defined with the @staticmethod decorator. They don't operate on an instance or the class.
syntax : -
@staticmethod
def static_method
"""
# indetails : --------------

"""
In Python class methods and static methods are two types of methods that are not bound to an instance of a class. 
They are used for different purposes and have different behaviors.

But when we talk about Instance method this is bounded to an instance of a class. 

Instance method : - 

__init()__, function(self) >> instance method used in most class  
Instance methods are typically used in most classes and are accessed through an instance of the class, not directly by the class name.
This is because instance methods operate on data that is unique to each instance of the class. 
So, you need to create an object of the class to call these methods.


Class method : -
@classmethod
Class methods are methods that are bound to the class itself rather than its object. 
They can modify the class state that applies across all instances of the class. 
To define a class method, you use the @classmethod decorator, and it takes cls as the first parameter. 
The cls parameter points to the class, not the object instance. Class methods can access and modify 
class variables but not instance variables.


Static method : -
@staticmethod
Static methods, on the other hand, do not take cls or self as the first parameter. They are also bound to the class, not the object, 
and cannot access or modify the class state. They are used to create utility functions that perform a task in isolation. 
Static methods are defined using the @staticmethod decorator.
"""

"""There are the three type of method in oops instance , class, static """
# ----------------------------------------------Instance method----------------------------------

class Device:
    """This is instance method """     
    # instance method required object of class to access it automatically
    def __init__(self):
        "method is use to initilize attribute "
        self.d_name = "mobile"
        self.d_price = 50
    
    # class method
    def device_info(self):
        print(f"Device name is : {self.d_name} and Device price is : {self.d_price}")
dobj1 = Device()
dobj1.device_info()




# ------------------------------------------------Class method

class Books:
    """This is class method"""
    
    @classmethod
    def book_info(cls):
        cls.b_name = "python"
        cls.b_price = 1800
    
    @classmethod
    def book_name(cls):
        print(f"Book name is : {cls.b_name} and Book price : {cls.b_price}")
bobj1 = Books()

# Books.book_name() 
# Books.book_info()
"""
consider calling them out of order (like Books.book_name() before Books.book_info()).
In this case, the book_name() method is executed first.
Since the attributes(variable) haven't been created yet (because book_info() hasn't been called), 
an “AttributeError” occurs.
"""
Books.book_info()
Books.book_name() 


# ------------------------------------------static method 

class Continent:
    """This is static method"""
    
    @staticmethod
    def asia():
        name = "Asia"
        print(f"This is {name} continent")
sobj1 = Continent()
sobj1.asia()

"""_______________________________VVI__________________________________________VVI_______________ EXAMPLE_________________"""
# Instance methods are typically used in most classes and are accessed through an instance of the class, not directly by the class name.
# This is because instance methods operate on data that is unique to each instance of the class. 
# So, you need to create an object of the class to call these methods.

class Modifications:
    """use body use to provide modification"""
    #instance method is used 
    def __init__(self):
        pass

    # instance method 
    def collections(self):
        set1 = { 1 : 'add()',
                 2 : 'clear()',
                 3 : 'copy()',
                 4 : 'difference()',
                 5 : 'difference_update()',
                 6 : 'discard()',
                 7 : 'intersection()',
                 8 : 'intersection_update()',
                 9 : 'isdisjoint()',
                'a': 'issubset()' 
                }
        return set1
    
    
    # class methods used
    @classmethod
    def collections2(cls):
        set2 = {
            1 : 'issubset()',
            2 : 'issuperset()',
            3 : 'pop()',
            4 : 'remove()',
            5 : 'symmetric_difference()',
            6 : 'symmetric_difference_update()',
            7 : 'union()',
            8 : 'update()',
            9 : 'frozenset,()',
           'a': 'len()'
        }
        return set2
    
    #static method is used 
    @staticmethod
    def collections3():
        set3 = {
            1 : 'all()',
            2 : 'any()',
            3 : 'enumerate()',
            4 : 'filter()',
            5 : 'forzenset()',
            6 : 'reduce()',
            7 : 'map()',
            8 : 'round()',
            9 : 'abs()',
           'a': 'zip()'            
        }

        return set3


obj = Modifications()
x = obj.collections2() # it contain memory refrance
for i in x:
    print(i, x[i])

