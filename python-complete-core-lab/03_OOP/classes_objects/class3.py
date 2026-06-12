# What is constructor ? 
# Types of constructor ?
"""
A constructor is a special type of method in object-oriented programming that is automatically called when an object of 
a class is created

when we create a object __init__ method is automatically called this method is used to initialize the object's attributes. 
It is  one of the special methods in Python, often referred to as a “magic method” because it has double underscores before 
and after its name.

we always use self as a first parameter in __init__() constructor

There are the three type of constructor in python : -
Default constructor           : - A class that does not have an __init__ method relies on the default constructor provided by Python
Parameterized constructor     : - A constructor that has more than one parameter, including self, is called a parameterized constructor
Non-parameterized constructor : - A constructor that does not have any parameters except self is called a non-parameterized constructor


"""


# ----------------------------------------------------------------------------------------------------------------------------------

class Dress:
    pass                        # Default constructor

shirt = Dress()

'''
Explanation : -
In this case, the class Dress does not have an __init__ method, so Python uses a default constructor.
'''

# ---------------------------------------------------------------------------------------------------------------------------------

class Books:
    """information about book"""
    def __init__(self):               # This is Non parameterized constructor
        self.name = "Ankit kumar"
        self.price = 2000

emp1 = Books()
print(emp1.__dict__)

'''
Explanation : --
when we create a object (emp1) then __init__  method is automatically called and initilize the two variable for emp1 first is 
name and second is price  

'''


# ----------------------------------------------------------------------------------------------------------------------------------

class Toys:
    """Name of toys"""
    def __init__(self, name, price, size, shape ):                      # This is parameterized constructor 
        """ Function is use to provide information about toys"""
        self.name_of_toy = name
        self.price_of_toy = price
        self.size_of_toy = size
        self.shape_of_toy = shape

ifo1st = Toys("Doll", 1000, f"{23}cm", shape="circle" )
print(ifo1st.__dict__)

'''
Explanation  : --
we create object from Toys class using __init__ constructor that initialize variable or attributes and store the parameter valuse 
one by one .s

'''

# -----------------------------------------------------------------------------------------------------------------------------------