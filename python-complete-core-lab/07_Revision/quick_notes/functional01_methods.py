"""
Write a Python program that continuously prompts the user for input. If the user enters "quit", the program
should terminate. Otherwise, it should display the message entered by the user
"""

'''
What is function in python ? 
In Python, a function is a block of code that performs a specific task. 
It helps organize code into reusable and readable segments, making programming simpler and more efficient.


What is function definition in python ?
The function definition is that place where we define the name of a function using simple keyword def means 
definition 'that indicate ready to define the function name' and the function name is followed by parentheses, 
which can include parameters—values the function uses when it runs. and at the end we use colon to end the statement
of function.
syntax : - 
def fun_name():


what is Docstring ? 
A docstring (short for documentation string) is a special type of multi-line string that documents a function,
class, or module. It appears immediately after the definition line and is enclosed in triple double quotes ("""). 
Docstrings explain what the code does and help others (or your future self!) understand the purpose of each 
component.


why we give docstring ? 
Docstrings act as helpful notes for developers. They describe the purpose, behavior, and expected input/output of
functions, classes, or modules. 
we give docstring to define what function, class or component does that serve as helpful notes for developers  
syntax : -
def func_name():
    """This method display hello Python """ 
    print("Hello Python")  
    
    
what is Indentation ?
Indentation in Python refers to the whitespace placed at the beginning of a line to define a block of code. 
It’s not just for style—Python uses indentation to determine code structure. It’s mandatory in functions, loops, 
conditionals, classes, and other code blocks. Consistent indentation tells Python which statements belong together.

syntax : -
def func_name():
    """This is Docstring"""
    i = 1 
    while i <= 5:
        if i % 2 == 0:
            print(f"This is {i}, an Even Number")
        else:
            print(f"This is {i}, an Odd Number")
        i += 1


what is function call ?
when we want to execute the function body from function definition then we use function name follow by parentheses
that includes arguments called function  
 
The function call follow by necessary information in Parentheses that tells python to execute block of code that
perform specific job or task in function.


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

Positional argument : -
Positional arguments are fundamental in passing values to function parameters these arguments are assigned
to parameters based on their order within the function.

When positional arguments are provided in an unordered form, there is a risk of obtaining incorrect output.
Therefore, it is essential to specify the correct order

positional argument are basic argument that passed orderly in parameter if the sequence is unorderly then we get
incorrect output


Keyword argument : -
A keyword argument is an argument that uses a key (parameter name), and each key corresponds
to a specific value passed to the function.

A keyword argument is like a pair of names. The first name is the key, and the second name is
the value. When you use a keyword argument in a function call, you’re essentially saying,
“Here’s a specific value for this particular key

In Python, the order of keyword arguments doesn’t matter because Python knows where each value
should go. each key clarifies the role of its corresponding value from the function call to the
function definition.


Default argument :-
It is the type of argument that use to assign the predefined value to function parameters
if the no value is provided for a parameter during a function call, the default value is used

In simple way if the argument provided for parameter in function call then python use the argument
value if not, it use parameter default value given in function definition.

1) def fun_name(f_name, m_name='', l_name): # when no value pass from function call to m_name default value is automatically passed
2) def fun_name(f_name, l_name, m_name=''): # when parameter(m_name) parameter have no value it passed default value automatically

Arbitrary argument : -
An arbitrary argument lets a function accept a variable number of inputs. It packs those inputs into a single collection like a tuple
or dictionary. This makes the function flexible and able to handle different amounts of data.



How many type of Arbitrary arguments ?
Positional Arbitrary Arguments (*args):
These are denoted by an asterisk * and are used to pass multiple positional arguments to a function.
The arguments are automatically packed into a tuple, which the function can process as needed.

Keyword Arbitrary Arguments (**kwargs):
These are denoted by a double asterisk ** and are used to pass multiple keyword arguments. The arguments are
packed into a dictionary, allowing the function to handle named inputs dynamically.
'''
# write a program to print the 2 x 2 matrix
def matrix():
    """method body is define the class"""
    row = int(input("Enter the row number : "))
    col = int(input("Enter the col number : "))

    matrx = []
    for i in range(1, row+1):
        """outer loop is use to count th row"""
        lst =[]
        for j in range(1, col+1):
            """inner loop is use to count the col"""
            user_value = int(input(f"Enter the value : a{i}{j} : "))
            lst.append(user_value)
        matrx.append(lst)
    for _ in matrx:
        """try to display the matrix in the from of matrix"""
        print(_)

matrix()

"""
Explain : -
matrix function is use to display matrix
1) we create function name matrix with the help of def keyword that followed by parenthesis or end with colon
2) we crea a attributes that store row and col that store row and column of matrix from user
3) after that we create a empty list (Null list) and store in matrx attributes
4) then we use a outer loop to iterate from 1 to user_input value for counting row of matrix
5) outer loop body contain an empty list that store the  value aij from user_value 
6) now user_value is operate through inner loop that iterate 1 to col or append again and again user_value to lst
7) after completing inner loop iteration the value that store in lst append in matrx as a array again and again 
8) now we call the function followed by parentheses to excute the whole program that explain above 
"""
# Dry run : -
# let suppose user enter : - 2, 2 (row, col) row = 2, col = 2
# matrx = [] > [[10, 20], [30, 40]]
# i =  1 : 3(row+1) > 1, 2
# lst = [] > [10, 20] >> [] >>> [30, 40]
# j = 1 : 3(col+1) > 1 2, 1: 3(col+1) >> 1 2
# user_value = 10, 20 (append add item at the end list)
# and after completing the iteration of outer loop we for loop to display matrix as it is.
# then we call matrix follow by parentheses to execute the whole program
