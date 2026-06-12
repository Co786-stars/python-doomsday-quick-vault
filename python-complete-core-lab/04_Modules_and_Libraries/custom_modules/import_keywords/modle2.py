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

-> The code that not written under the function excute by default in saperate file (modle3) output but the code that 
   written under the function only excute when we import that function using import keyword .  

"""
# ------------------------------------------------------------------------------------------------------------------------
# 2))  importing specific function  >> syntax  : from module_name or file_name import  function_name 
#      importing multipal functions >> syntax  : from module_name or file_name inport fun_name1, fun_name2, ...etc 
# ------------------------------------------------------------------------------------------------------------------------

from modle1 import count_addition
count_addition(5) 


from modle1 import count_addition, multiply

count_addition(3) # calling function from module1 

x = multiply(12, 13)  # calling function from module1
print(x)
