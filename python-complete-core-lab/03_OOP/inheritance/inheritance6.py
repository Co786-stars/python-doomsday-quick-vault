
# Inheritance Syntax : -
# ________________________________________________________________________________________
class Super:
    """class body is display Parents class"""

    def __init__(self):
        """initialize the attributes"""
        # attribute of parents class
        # attribute method of super class
        # attribute or method of class

class Subclass(Super):
    """class body inherit property from parents class"""
    def method(self):
        """attribute and methods of child class"""
# ________________________________________________________________________________________

class Color:

    var1 = input("Your favorite color is : ")
    def common(self):
        print("In india common favorite color is red")
class Favcolor(Color):

    var2 = input("My favorite color is : ")
    def myfav(self):
        print(f"Your favorite {self.var2}")
        print(f"My favorite {self.var1}")


col = Favcolor()   # parentheses () indicate that you’re invoking the constructor
col.common()
col.myfav()  # object.method() / calling process

# -----------------------------------------------------------------------------------------------

