#-----------------------------super function---------------------------------
#-----------------------------super function---------------------------------
#-----------------------------super function---------------------------------

"""
super() function is a built-in or predefine function that allow you to call methods
from a parent or superclass in sub class .

super() function is used to access methods from a superclass that might have been 
overridden in a subclass
"""
# -------------------------------------------------------------------------------------------------------#
# example : -

class Book:
    """all info about Book"""
    
    def __init__(self):
        self.B_name = "Python"
        self.B_price = 2000
    
class Copy(Book):

    def __init__(self):
        super().__init__() # attribute are created directly from parents for school
    
school = Copy()
p = school.B_name
q = school.B_price 
print(p, q)
# ------------------------------------------------------------------------------------------------------------#

# example : -

class Car:

    def __init__(self):
        self.van = "Fortune"
        self.price = 1500000

class Motercar(Car):

    def __init__(self):
        super().__init__()  # attribute are created directly from parents for moter
        self.color = "Red"  # color attribute are created for motercar 

moter = Motercar()
x = moter.van
y = moter.price
z = moter.color
print(x, y, z)

#----------------------------------------------------------------------------------------------------------------#
