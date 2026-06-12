# To clear the concept of super function it's very important to read about MRO in Inheritance. to understand the
# concept of MRO need to read file PyCore-Functional-OOPs-Toolkit\Class_Related\Class25_MRO_Inheritance.py
"""
> In this module we are going to clear the concept of `super()` function in Python : -
  Topic 1 : - Understanding super()
  Design an object-oriented program in Python to demonstrate the use of `super()`:
  -> Use a base class with an `__init__` method and a member function.
  -> Use a derived class that inherits from the base class and calls the parent class methods using `super()`.
  -> Show how `super()` helps in reusing and extending functionality of the parent class.
  -> In the `main` function, create objects of the derived class to demonstrate how `super()` works.
"""

"""
# super() is used in a child class to run code from its parent class.
# super() function in Python is a built-in function that is used to call methods from a superclass inside a subclass.
    > It returns a proxy object that delegates method calls to the next class in the Method Resolution Order (MRO), 
      making it essential for cooperative multiple inheritance and avoiding redundant code.
# Key benefits:
    -> Avoids hardcoding parent class names.
    -> Works with single, multiple, and multilevel inheritance.
    -> Ensures proper initialization across complex hierarchies.
    -> Improves maintainability and reusability.
# In simple way : -
    # super() is used in a child class to run code from its parent class, letting us access and extend inherited functionality.
"""
##Examples :-
# Single Inheritance Constructor Call:
class Student:
    """defining the super function"""
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class TopStudents(Student):
    """defining the name of top student"""
    def __init__(self, id, roll, grade):
        super().__init__(id, roll)
        self.grade = grade
obj = TopStudents("Wizard", 123, 'A')
print(obj.name, obj.roll,obj.grade)

# """
# Detailed Flow:
# 1. Interpreter reads class definitions (Student, TopStudents).
# 2. When obj is created, Python calls TopStudents.__init__.
# 3. Inside child constructor, super() looks at MRO [TopStudents, Student, object].
# 4. Finds Student.__init__ and executes it with (id, roll).
# 5. Parent assigns self.name = "Wizard", self.roll = 123.
# 6. Control returns to child, assigns self.grade = 'A'.
# 7. Final object has all three attributes: name, roll, grade.
# 8. print → Wizard 123 A
#
# Hidden Gem:
# - super() doesn’t mean “parent only”, it means “next in MRO”.
# - self is always the same object (child instance), so parent attributes live in child too.
# """




##Example :-
# Single Inheritance Constructor Behavior:
class Device:
    """define the name of top Device"""
    def __init__(self):
        """Constructor Initialize the attribute"""
        self.var = "variable"
        self.num = 20
        print(self.var, self.num)

class Tools(Device):
    """class is define the tools"""
    def tools(self):
        """defining the tools"""
        pass

class Concept(Device):
    """try to clear the concept of super function"""
    def __init__(self):
        super().__init__()

obj2 = Tools()   # output → variable 20
obj3 = Concept() # output → variable 20


# Note(obj2) :-
# When we create an object of Tools(Device), Python sees that Tools has no __init__ defined so interpreter automatically
# executes the parent’s constructor (Device.__init__), so the child object gets var and num initialized
# from the parent.

# explain(obj3) :-
# 1. Inside Concept.__init__, call super().__init__().
# 2. MRO for Concept is [Concept, Device, object].
# 3. super().__init__() finds Device.__init__ next in MRO and executes it.
# 4. Device.__init__ sets self.var = "variable", self.num = 20 and prints "variable 20".
# 5. Control/interpreter returns to Concept.__init__; Concept does no extra assignments.
