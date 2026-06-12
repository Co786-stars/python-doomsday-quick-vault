"""
----------------------------- Return Value ------------------------ Return Value ------------- 
When the Python interpreter encounters a return statement inside a function, it immediately exits 
the function and returns the specified value (calling function ).

"""


# def format(name, lname):
#     """This is dos string use after funtion defenation"""
#     x = f"name : {name} lname :  {lname}"
#     return x.upper()
# x = format("Aditya", "wizard")
# print(x)


# def format1(name, lname):
#     full_name = f"{name} {lname}"
#     return full_name.upper()
# x = format1("Jimi", "wizard")
# print(x)


# -----Most Important vvi---------------for return statment -------

# def my_func():
#     return("Wizard")
# my_func()

# def my_func1():
#     return("Wizard")
#     print("Hello Wizard")
# x = my_func1()
# print(x)

# ------Most Important vvi-----------------for return statment -------
a = int(input("Enter the value of arg1 : "))
b = int(input("Enter the value of arg2 : "))

def color(arg1=20, arg2=10):
    sum  = arg1 + arg2
    return(f"The sum of {arg1} and {arg2}", sum)


print(color(a, arg2=b))
color(a, b)
z = color(a, b)
print(z)

