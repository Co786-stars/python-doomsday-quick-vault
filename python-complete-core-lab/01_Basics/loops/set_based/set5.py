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
x = obj.collections() # it contain memory refrance
for i in x:
    print(i, x[i])

obj2 = Modifications.collections2()
for i in obj2:
    print(i, obj2[i])

obj3 = Modifications.collections3()
for i in obj3:
    print(i, obj3[i]) 

# Go to next module for set function >>>>>>>>>>>>>>>>>>>>>>>>>>>----------------------> Next module set7.py 
# If any problem then read the toic (1) How to call class methods and static methods 
# and                               (2) what is the difference between all of three method
# and                               (3) When we use instance class or static method and why we use 
""""
Instance Methods: Use the self parameter and  defined without any decorator. They operate on an instance of the class.
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

