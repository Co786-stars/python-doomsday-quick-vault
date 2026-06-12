"""
What is parameters in function ?
A parameter is an object that holds its position in a function definition. It is used to carry or pass a small amount of
information during function execution when the function is called


What is arguments ?
An argument is the object provided in a function call, typically in the form of a number, string, boolean, or other
datatype. It is used to pass a value to the corresponding parameter during function execution.


How many type of arguments in python ?
There are the many way to pass the argument in function definition
1) Positional argument
2) Keyword argument
4) Default argument
5) Arbitrary argument

"""
# -----*
# ----***
# ---*****
# --*******
# -*********

# display the full pyramid pattern with function or without function
#>> without function
x,i = 5,1
while i < x+1:  # 1 > 2 > 3 > 4 > 5
    """outer loop is control the row of pyramid"""

    spc = 1
    while spc <= (x+1)-i: # spc = 1, 2, 3, 4 5 >> 1, 2, 3, 4 >> 1, 2, 3, >> 1, 2 >> 1
        print(" ", end="")
        spc += 1

    j = 1
    while j < 2*i:  # 1 > 12 > 123 > 1234 > 12345
        """loop is use to control col of pyramid"""
        print(f"{'*'}", end="")
        j += 1
    print()
    i += 1


#>> with function parameter and argument concept
def full_pyramid(p1): #function declaration or function definition >>>> positional arguments
    """method is display the full pyramid pattern"""
    for i in range(1, p1+1):
        """Outer loop control the row"""
        for j in range(1, (p1+1)-i):
            """first inner loop take space for each row"""
            print(" ", end="")

        for k in range(1, i+1): # 1 2 3 4 5 >> 2, 12, 1 2 3, 1 2 3 4, 1 2 3 4 5
            print(f"{chr(64+k)}", end=" ")
        print()

value1 = int(input("Enter the row number : "))
full_pyramid(value1) # function call
"""value1 is positional argument pass from p1 parameter"""


