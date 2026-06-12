"""
-> An import statement tell python to make the code in a module available in the currently running program file 

-> A module is a separate file that contains functions, classes, and variables, which we create for reuse in other
   programs or modules or importing that module in main program 

-> Storing the function in a saperate file allow to hide the details of programs code and focus on high-level logic  

-> There are many ways to import modules modules : -
   1)) import the entire module
   2)) import the specific function 
   3)) using as to given a function an alias 
   4)) using as to give a module an alias 
   5)) importing all the function in module 

"""

# --------------------------------------------------------------------------------------------------------------------
# 1))  importing a entire module >> syntax  : import module_name or file_name
# --------------------------------------------------------------------------------------------------------------------


import modle  # import entire code of modle.py in this case molde is module and import is keyword 

print("\n")

# when python read the line import then modle tell python to open modle.py file and copy all the function from it into this program
# During the calling first we give the name of module and then we use function related that modules with the help of  
# selector/member operator  

import h   
h.make_pizza(12, "mashroom", "without cheese", "species") 


# ----------------------------------------------------------------------------------------------------------------------



def count_addition(user_value):
    """ addition of count number """
    store_value = 0
    for i in range(1, user_value+1):
        print(f"{i}", end= " ")
        store_value += i
    print()
    print(f"The Total sum of {1} to {user_value} is : {store_value}")
        


def multiply(x , y):
    """ multiplication"""
    z = x*y
    return z

# Calling function in module3.py using import syntax vist the module3.py (file3) for the output of this program 


#######################################################################################
# --------------------------  None datavalue --------- None datavalue -----------------
"""def count_addition(user_value):
        for i in range(1, user_value+1):
            print(f"{i}", end=" ")
            x += i

x = count_addition(10)
print(x)"""  # calling function
#######################################################################################



