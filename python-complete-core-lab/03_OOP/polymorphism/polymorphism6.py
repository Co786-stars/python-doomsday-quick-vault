"""
Polymorphism : -

Polymorphism means "many forms" the ability of different objects to respond to the same method or function in different ways.
Polymorphism is fundamental concept in OOPs that allow object to process differently based on their datatype or class .

In python Polymorphism is  enhance code flexbility, reusability , readability and basically categorized in four parts 
<1> Functional polymorphism
<2> Operator polymorphism
<3> Class Polymorphism
<4> Polymorphism With inheritance
"""

"""
Inheritance polymorphism : -
Inheritance polymorphism, also known as subtype polymorphism, means ability of a subclass to override a method from a
superclass, allowing objects of the subclass to be treated as objects of the superclass
"""

# example of Polymorphism 

class Colors:
    
    def watercolor(sketch_favorite):
        print(f"My favorite water color is {sketch_favorite}")
    
    def sketchcolor(sketch_favorite):
        print(f"My favorite sketch color is {sketch_favorite}")
    
class Transprent(Colors):

    def watercolor(arg1):
        print(f"water has no color means water is {arg1}")
    
    def sketchcolor(arg2):
        print(f"Sketch color means color with no {arg2}")

class Frequency(Transprent):

    def rayoflight(arg1):
        print(f"Human visible light ray is between 400nm to 700nm")
    
    def sketchcolor(arg2):
        print(f"The first sketch color {arg2}") 


color = Colors
transprant = Transprent


value = str(input("Enter your favorite color : "))
def displayclass(value = "Nothing"):
    for i in (color, transprant): # overide parents class method from child class method when we use second argument 
        i.watercolor(value) # means similar function but different work depend upon instance of a class 

displayclass(value)

