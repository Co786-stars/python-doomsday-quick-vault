# --------------------------------------------------------------------------------------------------------------------------------#
# --------------- : User-define class : --------------------- : User-define class : ------------------ : User-define class : -----#
# --------------------------------------------------------------------------------------------------------------------------------#
"""
How to create the class in python 

step 1.>  Use class keyword to Initialize class
step 2.>  Use class name to create class 
          note : - In most case we use class name in capitalize from 
step 3.>  use colon to end the class 
step 4.>  Use indentation to provide the attribute and method of class 

NOW : -
> Class_name is the Identifier for class keyword 
> attribute means variable and methods (the functions define inside the class) means function 
> The process of making object from class called instantiation and we work with instances
> Passing of argument afrom object its all are dpend upon us 



syntax  : --
----------------------------
class Class_name:
    #attributes
    #methods

obj1 = Class_name(args)
obj2 = Class_name(args)
------------------------------


"""


class friends:
    pass

f1 = friends()     # to create the object usally use the name of class like this friends()   
f2 = friends()

print(type(f1))    #  output ::  <class  '__main__.friends'>  :: The object f1 is belongs to friends class 
# The output is show f1 object is belongs to friends class and friends class is exit in __main__ module /file (current_file)     


class students:
    """ syntax of class """
    pass

s1 = students()





# ---------------------------------------------------------------------------------------------------------extra

"""class fruits:
    pass

x = fruits() 
print(x)       # output  :  <__main__.fruits object at 0x0000029687555820> 
print(type(x))  # output : <class '__main__.fruits'>
"""
# -----------------------------------------------------------------------------------------------------------extra
