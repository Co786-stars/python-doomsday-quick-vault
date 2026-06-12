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
Class Polymorphism : -
Class polymorphism in Python means that different classes can be treated as instances of the same class through a common interface. 
Essentially, it allows methods in different classes to have the same name but behave differently based on the object that calls them

"""
# class Polymorphism : - example 1st
class Pet_animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def animal(behaviour):
        behaviour.eating = "Harbivores"
        print(f"Pet animal {behaviour.name} {behaviour.eating} its sound like {behaviour.sound}")

class Wild_animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def animal(self):
        self.eating = "Carnivores"
        print(f"wild animal {self.name} is {self.eating} its sound like {self.sound}")

pet = Pet_animal("Cat", "Meow")
wild = Wild_animal("Lion", "Roar")

for i in (pet, wild):
    i.animal()

