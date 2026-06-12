
'''
---------------------Method overriding----------------Method overriding----------------Method overriding-----------Method overriding
------Method overriding----------------Method overriding----------------Method overriding-----------Method overriding---------------
---------------------Method overriding----------------Method overriding----------------Method overriding-----------Method overriding
'''

"""
Method overriding is a concept used to manage methods that exist in both a parent class and a child class. 
Without inheritance, method overriding is not possible. When we override a method in a single class, errors can occur 
In method overriding, similar methods are defined in both the superclass (parent class) and the subclass (child class).
When we invoke a method from the child class, the corresponding method in the parent class is never executed. 
To achieve this behavior, we provide a specific implementation for the method in the child class. this feature enables polymorphism
The corresponding methods of the parent class and the child class can behave differently based on the object that invokes them . 

Syntax : -

class Superclass:    
    def method1st(self):
        print("This is parents class")

class Child(Superclass):
    def method1st(self):
        print("This is child class")

In the situation of crossponding function childclass method override parentsclass method .  
"""

class Car:

    def features(self):
        x = "beautiful"
        print(f"My car is {x}")

class Electric(Car):

    
    def features(self):

        y = "big"
        print(f"My car is {y}")
        super().features()   # to call the function  from super class when overrriding is exist 
                            
pobj = Car()
pobj.features()

cobj = Electric()
cobj.features()   
