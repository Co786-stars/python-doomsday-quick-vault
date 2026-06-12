"""
------------ self variable ----------------- self variable --------------------- self variable ------------------- self variable --- 

>> self is not a variable a label or pointer which pass memory refrence/address of current object.

"""

# Memory will not be allocated for a class until an object is created for that class
# After creating object memory will  be assign to class otherwise there is no use of class
# without constructor object is not excuted or created so at list one __init__() method is necassary to excute the object  

class Animals:
    """ This is animal class """
    def __init__(self, name, color):
        """ names of animal in this function body """
        self.animal_name = name
        self.animal_color = color

animal = Animals(name="Horse", color="white") 


'''
How interpreter read the code : -
-> first interpreter read line 5 and then it jump into line 12 because class have a no memory allocation.>>  Class Animals
-> after reading line 12 python allocate memory for animal in inside the  heap   >> animal = Animals(name="Horse", color="white")
-> after allocating memory address to animal(object) python check constructor __init__ method is abliable or not in class body if yes
-> then interpreter read first parameter self (from self memory adress is passed as a argument) and horse or White is passed from name
   or color NOTE : - the memory address argument are not visible it is first argument passed from first parameter internally passed 
                     from self parameter >> parameter sequence Animals(memory_address(hidden, "Horse", "white")   
-> then interpeter read the line 12 means >> self.animal_name means self is a memory address and in that memory aniaml_name variable is 
   created and assign the name paramater value 

-> then interpeter read the line 13 means >> self.animal_color means self is a memory address and in that memory animal_color variable is 
   created and assign the color paramater value 

'''

