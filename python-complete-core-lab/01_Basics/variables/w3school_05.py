# --------------------- Local variable and global variable in python -------------------------- #
"""
Local Variables:
Local variables are declared within a function.
They have a limited scope and are destroyed when control exits the function.

Global Variables:
Global variables are declared outside of any function.
They exist throughout the entire execution of the program.

---------*
-------* * *
-----* * * * *
---* * * * * * *
-* * * * * * * * *
Local and Global variable concept using Pyramid pattern
"""
x = int(input())  # global variable 
def pyramid_pattern(value1):
    # global spc    # global keyword is use to make local variable into global for access variable globally 
    spc = 2*value1-1  # Local variable 
    """use to display the pyramid pattern"""
    for i in range(1, value1+1):
        
        for j in range(1, spc+1):
            print('-', end="")
        
        for k in range(1, 2*i):
            print("*", end=" ")
        spc -= 2
        print()
pyramid_pattern(x)

