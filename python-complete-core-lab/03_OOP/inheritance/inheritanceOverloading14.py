# ____________OVERLOADING____________OVERLOADING__________________OVERLOADING_________
# METHOD OVERLOADING__________
# OPERATOR OVERLOADING_________

"""
Method overloading : -

In python method overloading is not directly supported  as it is in like some other 
language ex : - c++, Java etc mens python does not support method overloading

Method overloading is a concept where you can define multiple methods (or functions) 
with the same name but different parameter lists

why python does not support method overloading ? 

In Python, the flexibility of handling arbitrary arguments and keyword arguments—via *args and **kwargs—essentially fulfills the 
role of method overloading. Consequently, Python doesn't enforce traditional method overloading as some other languages do. 
If method are call with incorrect number of argument then error are occur at the runtime,  error name is type error 
"""
# Syntax : - 

class Car:

    def __init__(self):
        """..."""
    
    def MotorCar(self):
        """..."""
        return f"This is my 1st car"
    
    def MotorCar(self):
        """...."""
        return f"This is my 2nd car"

    def MotorCar(self): # it always excute last method means current method read by interpreter
        """..."""
        return f"This is my 3rd car"
    
obj = Car()
x = obj.MotorCar()  # this example is show the overloading example if we give extra parameter in method then error are generate  
print(x)            # only last method are excute other then nothing this process is use for java and c++ only it show how overloading
                    # works if it works simple like a function in oops overloading is not use in python


