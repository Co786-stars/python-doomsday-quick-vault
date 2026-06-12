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

->  The 'as' keyword in the import statement used to create an alias for the imported module or function.

->  The name alias ['as'] means alternate name for the function that can make your code more readable or help avoid 
    naming conflicts.

"""

# ------------------------------------------------------------------------------------------------------------------------------------
# 3)) using as to given a function as alias  >> syntax  : from module_name import  function_name  as fn 
#     using as to given a function as alias >> syntax  : from module_name import fun_name1 as fn1 , fun_name2 as fn2 ..etc 
# -------------------------------------------------------------------------------------------------------------------------------------
 

from modle1 import multiply as multi_ply  # given a  function an alias >> syntax : ( from module_name import function_name as fn )  

x  = multi_ply(10, 20) 
print(x) 


import modle2 as m1 # given a module an alias  >> syntax : ( import module_name as mn )

