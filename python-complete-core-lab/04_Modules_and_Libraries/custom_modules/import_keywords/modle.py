"""
-------------------- <: VERY IMPORTANT SESSION TOPiC NAME :>-----------
    
A file that encapsulates a collection of related functions, instructions, class and commands and used in other 
parts of a program to promote code  reusability.

The purpose of a module is to organize code and make it reusable .

-------------------- <: STORING YOUR FUNCTION IN MODULES :> -----------
"""
#  WAP TO STORE MULTIPAL NUMBER AND OUT THAT NUMBER WHICH IS DIVISIBAL BY 5

# def fun_num(user1):
#     """Dosstring : storing your function """
#     x = []
#     for user in user1:
#         if user%5 == 0:
#             x.append(user)
#     return x

# list1 = [i for i in range(10, 21)]
# Divisibal_of_five = fun_num(list1)
# print("The devisibal of {5} between {10} and {20} is : -")
# print(f"{list1} ==> {Divisibal_of_five}")

# >>>>>>>>>>>>>>>>  check the module_1.py >>>>>> next file  

def addition(x, y):
    sum = x+y 
    return sum

num1 = int(input("Enter number 1st : "))
num2 = int(input("Enter number 2nd : "))
total = addition(num1, num2)
print(f"Total sum : {total}")


