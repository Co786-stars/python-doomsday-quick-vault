"""
#----------------- How to access class member --------- How to access class member ----------- How to access class member -------------#

whenever the object is created then memory allocation is always return to object   

Class members mens attribute(variabe) and actions(function) present inside the class 
We access the class member by using outside the class 

Syntax to access the class member : -
accessing_attribute : - object_name.variable_name
accessing_method    : - object_name.method_name()

"""

class Colors:

    def __init__(self, name, type):

        self.color_name = name
        self.color_type = type
                        # self parameter is a memory address/reference for current object .    
    def output(self):   # def output(self) is a method and >> method is just a function inside the employed class               
        print(f"My favrorite {self.color_type} color is {self.color_name}") # we give the variable name with object address that contain self. 
 
var1 = str(input("Enter color name : ")) 
var2 = str(input("Enter color type : ")) 

fav_col = Colors(var1, var2)

# How to access the attribute outside the Class  
print(fav_col.color_name) #  this line is use to access the attribute of class syntax : obj_name.attribute_name 
# print(fav_col.output())  # this line is use to access the method(function/action) of Color class 

# How to access the  method outside of class 
fav_col.output()   # first memory address of fav_col(object) comes under the parantheses as a argument and pass from self parameter  
                   # in output(self) function >> self contain memory referance/address as a argument after calling fav_col.output()

# How to modifie the value of attribute 
fav_col.color_name = "Yellow"     # updating attribute 
print(fav_col.color_name)

"""
explanation : --
starting from line number 26 : -
>> after making fav_col (object)  >> By default memory is allocated in os for fav_col( Object) >> and create two variable 
   color_name and color_type 

>> fav_col.color_name (accessing) >> from the memory address of fav_col(object) python access the value of color_name(variable) using
   dot (selector operator)


"""
# ----------------------------- Extra ------------------------- Extra -------------------Extra---------------------#
class Dog:
    """simple class of Dog"""
    def __init__(self, name, age): # we take any name at the self but self is by default it is only use to pass the memory address as a argument
        """initalize name and age attribute"""
        self.dog_name = name
        self.dog_age =  age

    def sit(self):  # we use sef at the place of self because we use first parameter to pass the argument (memory referance/address)
        """Simulate a dog sitting in response to a command """
        print(f"{self.dog_name} is now sitiing")
    
    def roll_over(self):
        """Simulate rolling over in response to acommand"""
        print(f"{self.dog_name} role over")
    
dog1 = Dog("Tomy", 20) # creating the object 
dog1.sit()






