"""
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
An arbitrary argument lets a function accept a variable number of inputs. It packs those inputs into a single collection like a tuple \
or dictionary. This makes the function flexible and able to handle different amounts of data.

How many type of Arbitrary arguments ?

Positional Arbitrary Arguments (*args):
These are denoted by an asterisk * and are used to pass multiple positional arguments to a function.
The arguments are automatically packed into a tuple, which the function can process as needed.

Keyword Arbitrary Arguments (**kwargs):
These are denoted by a double asterisk ** and are used to pass multiple keyword arguments. The arguments are
packed into a dictionary, allowing the function to handle named inputs dynamically.

"""

#Positional arguments : -
#write program in sort way of full pyramid using positional argument?
def pyramid(user):                                           #  Function declaration/definition
    """function body is display full pyramid pattern with positional argument"""
    for i in range(1, user+1):
        """outer loop control row iteration"""
        print(((user-i)+1)*" ", end=" ") # i = 1 2 3 4 5 >> -----, ----, ---, --, -
        print((2*i-1)*"*")  # - */n-- ***/n--- *****/n---- *******/n----- *********\n
pyramid(5) # Simple program to perform [ positional argument ]   Function call


#write a program to print the right half pyramid pattern
def right_half_pyramid(g_value):
    """function body display the example of positional argument"""
    i = 0
    while i < g_value:
        """outer loop control row behaviour"""
        j = True
        while j :
            """inner loop control th space"""
            print(" ", end="")
            break
        k = 1
        while k < 2*(i+1): #  k =
            """second inner loop display the star pattern"""
            print(f"*", end="")
            k += 1
        print()
        i += 1
user = int(input("Enter the row number : "))
right_half_pyramid(user) # this is the example positional argument




#Keyword argument
# write a program to display the addition of matrix using keyword arguments?
def matrx1st(x, y):   # function declaration/definition
    """function body is display the first matrix"""
    mat1 = []
    for i in range(1, x+1):
        """outer loop manage row of matrix"""
        matrow = []
        for j in range(1, y+1):
            """inner loop manage column"""
            user = int(input(f"Enter the value of : a{i}{j} : "))
            matrow.append(user)
        mat1.append(matrow)
    print("First matrix : -")
    for i in mat1: # first matrix
        """extra outer loop to display value as a matrix"""
        print(i)
    return mat1
value1st = int(input("Enter the row number of : matrix1st : "))
value2nd = int(input("Enter the col number of : matrix1st : "))
user_first_matrix = matrx1st(y = value1st, x = value2nd)  # example of keyword argument function call use parameter name that contain user value(argument)


def matrx2nd(a, b): # function definition/declaration (second matrix)
    """function body is display the second matrix"""
    mat2 = []
    for i in range(1, a+1): # outer loop (row)
        """outer loop control row of matrix"""
        row = []
        for j in range(1, b+1): # inner loop (col)
            """inner loop control the col of matrix"""
            usr = int(input(f"Enter the value of : b{i}{j} : "))
            row.append(usr)
        mat2.append(row)
    print("Second matrix : - ") # matrix 2nd
    for k in mat2: # extra outer loop ( display row as a form of matrix )
        """extra outer loop to display values as a matrix"""
        print(k)
    return mat2
var1 = int(input("Enter the row number of : matrix2nd : "))
var2 = int(input("Enter the col number of : matrix2nd : "))
user_second_matrix = matrx2nd(a = var1 , b = var2)  # example of key word argument that contain parameter name and value as  argument.

# Addition of matrix : -
def addition():
    """function is display addition of the matrix"""
    addition_of_matrix = []
    for i in range(len(user_first_matrix)): # 2 = 0, 1
        addition_row = []
        for j in range(len(user_first_matrix[0])): # 2 = 0 1 ; 2 = 0 1
             var = user_first_matrix[i][j]+user_second_matrix[i][j]
             addition_row.append(var)
        addition_of_matrix.append(addition_row)
    print("Addition of matrix1st and matrix2nd : -")
    for _  in addition_of_matrix:
        """display the addition of matrix mat1 and mat2 in the from of matrix"""
        print(_)
addition()

# Default argument
# Default Parameter Example with Local variable and Global variable
def sum(x=5, z=3, y=5): # example of default argument
    addition = x+y+z
    return addition
add = sum(z=5, y=7)
print(add) # total output is 17 (the value of z is a default)


