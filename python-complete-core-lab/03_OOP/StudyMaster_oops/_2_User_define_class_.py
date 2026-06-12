"""
> In this module we are going to Discuss __________User define class__________
How to create the class in python ?

step 1.>  Use class keyword to Initialize class
step 2.>  Use class name to create class
          note : - In most case class name is given in Title Case style.
step 3.>  use colon to end the class
step 4.>  Use indentation to provide the attribute and method of class

NOW : -
> Class_name is the Identifier for class keyword
> attribute means variable and methods (the functions define inside the class) means function
> The process of making object from class called instantiation and we work with instances
> Passing of argument from object it's all are depend upon us except memory reference (arguments)

syntax  : --
----------------------------
class Class_name:
    #attributes
    #methods

obj1 = Class_name(args) # the process of making object from class called ...instantiation...
obj2 = Class_name(args)
------------------------------

"""
class City:
    """This is Doc-string"""
    pass
obj, obj2 = City, City()
print(obj)         # <class '__main__.City'>
print(type(obj2)) # <class '__main__.City'>
print(obj2)      # <__main__.City object at 0x0000017FC69C6F90>

"""
obj :-
The object obj is an instance of the City class, and that class was defined in the main script you're running.

City :-
Name of our class

__main__ :-
The name of the current Python file that we are Running (the main program).

<class '__main__.City'> :- 
Python is saying the class name City is defined in main file(_2_User_define_class_.py / __main__)

<__main__.City object at 0x0000017FC69C6F90>  :-
object at 0x0000017FC69C6F90 is the memory address where the object is stored during that program run.

"""
# Important:-
# How to find the memory location 0x0000017FC69C6F90 in my system?

# This memory address shows where Python keeps the object in your computer's memory (RAM) while the program is running.
# It is temporary and managed internally by Python.

# Can we access or locate it directly 0x0000017FC69C6F90 in our file system or OS?
# ❌ No, we cannot.

# Why memory address(0x0000017FC69C6F90) is not accessible ?
# - The memory address is not stored on disk.
# - It exists only in volatile memory (RAM).
# - Python uses it to manage objects during runtime.
# - Once the program ends, the memory is released and no longer accessible.

# Summary:
# The address like 0x0000017FC69C6F90 is just a snapshot of where the object lives in memory during execution.
# It's useful for debugging, but not something we can trace or open in our system.

print(bin(id(obj)))
# Shows the memory address of 'obj' in binary format.
# - This memory address exists only while the program is running.
# - It points to where the object is stored in RAM (volatile memory).
# - Once the program ends, Python releases that memory.
# - So, you cannot access or find this address after the program finishes.

