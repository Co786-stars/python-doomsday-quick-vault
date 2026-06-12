# print full pyramid pattern without function or with function
def pyramid_pattern():
    """ use to print the full pyramid """
    row = 5
    for i in range(1, row+1):
        print(" "*(row-i), end="")
        print("*"*(2*i-1)) # 2*5 = 10-1 = 9 x * 
# output >> i = 1  2  3  4  5
# output >> ----*
# output >> ---***
# output >> --*****
# output >> -*******
# output >> *********
pyramid_pattern()


# print full paramid pattern with using function 
"""
The variable passed in the function definition is called a parameter, and it represents the piece of information 
that the function needs to perform its tasks

The variable passed in function call is called argument and On the other hand, the value provided to the function 
when calling it is called an argument

The interpreter reads the function definition first, and then you can call the function as needed. that allows you 
to organize your code and reuse the same logic in multiple places.


"""
def full_pyramid(row):
    """use to print the full pyramid """
    for i in range(1 , row):
        print(" "*(row - i), end="")
        print("*"*(2*i-1))
x = 6
full_pyramid(x)


