"""
Type of variable in oops : -
>> In functional programming we see local variable Global variables .
   Now In OOPs there are two type of variable instance variable and class variables 

1)) Instance variable : -
    
  >> variable made for particular instance
  >> saperate compy is create for every object 
  >> modification of one object never effect to other object 
  >> value of variable differ from object to object 

2)) Class variable : --
   
  >> class variable are the variable that made for entire class 
  >> To create the class variable we give variable name and value at top of the class
  >> For instance variable nth number of copy are created (number of object = number of copy )But 
     For Class variable  one copy are  created for each object or each object share information with 
     class variable
  >> Class variable is a variable that is eaisly accessibal by every onject  
  >> Class variable is a type of variable that is same for every object 

     Syntax : -
     class class_name:
        class_var_name = 'value'

        def __init__(self):
        
        
        def 
"""

class School:
    vacation = "dawali" # class variable is a variable that is same for every object.
    """information about school"""
    def __init__(self, name, roll, location):
        """ Initlize attributes """
        self.studentname = name   #attribute
        self.studentroll = roll   #attribute
        self.studentlocation = location  #attribute
    
    def student(self):
        """information about student"""
    
    @classmethod
    def sports_student(cls): # cls work like a self but in cls we pass the class refrence 
        print(cls.vacation) 
        cls.vacation = "holi"
        return cls.vacation
        pass

object1 = School("wizard", 123, "india")
object2 = School("hacker", 456, "amrica")
object3 = School("Aditya", 789, "london")
print(object1.__dict__) # use to display value of attribute 
print(object1.student.__doc__) # use to print the dos string of student
print(object3.studentname) # from memory address of object3 we access studentname
object3.studentname = "gita" #
print(object3.studentname)  # use for modification of attribute of object3 dfdfrom class School class 
# class variable
# >> in class variable value made for entire class (all object)
# >> only one copy is created and distributed to all objects
# >> modification in class variable impact on all object 
""" Class variable """

""" For accessing the class variable we have a two ways first using class refrence(address) 
    and second is object refrence(address) """
    
""" But For modification class variable we have only one way using class refreance (address)"""
print(School.vacation) # Use to access the class variable using class refreance  >> ( class_name.class_var_name )
print(object3.vacation) # Use to access the class variable using object refrence >> ( objectname.class_var_name )
School.vacation = "Happy new year" # use for modification of class variable 
print(School.vacation) # after modification we access the class 
object1.vacation = "durga puja" # modification using object
print(object1.vacation) # after modification only value is modify for object1
print(School.vacation) # there is no modification in class variable 

"""For accessing and modification of class variable we have also a other option like class method """
School.sports_student() # use to access the the method of class suing class refrence
School.sports_student() # use to access the method of class using class refrence 
