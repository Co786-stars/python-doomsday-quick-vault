# There are the many way to pass the argument in function definition 
# 1)) Positional argument
# 2)) Keyword argument
# 4)) Default argument
# 5)) Arbitary argument
"""
__________ Default argument________

It is the type of argument that use to assign the predefined value to function paramenters
if the no value is provided for a parameter during a function call, the default value is used

In simple way if the argument provided for parameter in function call then python use the argument
value if not, it use parameter default value given in function defination.


In the both function mname is default argument but we can not give the sequence like 1st line.
2nd line paramenter sequence is write .

1) def formmat_name(fname, mname='', lname):
2) def formmat_name(fname, lname, mname=''):

"""

x = int(input("Enter your value first   : "))
def my_function(x ,y=5):
    a  = x+y
    print(a)

my_function(x=5)
my_function(x=5, y = 7)


def student(firstname, lastname='Mark', standard='Fifth'):
    print(f"{firstname} {lastname} studies in {standard} Standard")

# Example calls:
student('John')  # John Mark studies in Fifth Standard
student('John', 'Gates', 'Seventh')  # John Gates studies in Seventh Standard


