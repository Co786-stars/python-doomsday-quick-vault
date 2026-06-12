# This is different topic from OOPs in this topic we cover about Global variable and local variable.

# ___________________________________________________________________________________________________________________________
"""
Global variable : -

A variable that is declared outside of a function is known as a global variable. 
This means the variable has a global scope and can be easily accessed both inside and outside of functions

#syntax : -

global_var = "Data values"

def my_function():
    print(global_var) #accessible inside the function

my_function()
print(global_var) #accessible outside the function too
"""
# __________________________________________________________________________________________________________________________
"""
Local  variable : -

A variable that is declared inside a function is known as a local variable. 
This means the variable has a local scope and can be easily accessed inside functions but not outside them

# syntax : - 
def my_function():
    local_var = "Data values"
    print(local_var)  #accessible inside the function but outside error are happen

my_function()
print(local_var)  #error are generated, local_var is not accessible outside the function

"""
# ________________________________________________________________________________________________________________________________
"""
Global keyword in python : -
The global keyword in Python is used to give a local variable global scope. It acts as a modifier for the local variable, allowing 
it to be accessed and modified from outside the function

syntax : - 

def my_function():
    global my_var
    my_var = "Data value"

my_function()
print(my_var)  # output "Data value" 


"""
# ______________________________________________________________________________________________________________________________

var1  = int(input("Enter your number : "))
var2 = int(input('Enter your number : '))
def color(add = var1+var2):
    return f"The addition of {var1} and {var2} is {add}" # example of global variable 

x = color()
print(x)



def device():
    tech  = 'Computer'
    return f"My favorite {tech} is based on linux os" # example of local variable acessible inside but not outside of function

y = device()
print(y)
# print(tech) # >> error are generate tech is not define < Name error >... / only accessible inside the function because it is local


def animal():
    global favorite
    favorite = str(input("Enter your favorite animal name : "))
    print(f"My favorite animal is {favorite}")

animal()
print(favorite) 