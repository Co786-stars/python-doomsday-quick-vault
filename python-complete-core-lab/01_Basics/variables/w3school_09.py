## There are the many way to pass the argument in function definition 
# 1)) Positional argument
# 2)) Keyword argument
# 4)) Default argument
# 5)) Arbitary argument
"""
__________Keyword argument________

A keyword argument is an argument that uses a key (parameter name), and each key corresponds
to a specific value passed to the function.

A keyword argument is like a pair of names. The first name is the key, and the second name is 
the value. When you use a keyword argument in a function call, you’re essentially saying, 
“Here’s a specific value for this particular ke

In Python, the order of keyword arguments doesn’t matter because Python knows where each value 
should go. each key clarifies the role of its corresponding value from the function call to the 
function definition.
 
"""
# 2
# 2
# mat2 >> [20, 30] >> [40, 50]
# mat2 >> [[20, 3], [40, 50]]
# [20, 30]
# [40, 50]
print("Enter the row and column to print matrix")
x = int(input("Enter the row number for matrix : "))
y = int(input("enter the col number for matrix : "))
mat1 = []

def matrix(row, col):
    """ mtrix using function for key word concept"""
    for i in range(1, row+1):
        mat2  = [] 
        for j in range(1, col+1):
            x = int(input(f"Enter the value of matrix : [{i}][{j}] : "))
            mat2.append(x)
        mat1.append(mat2)
    print(mat1)

    # use to print in the matrix format 
    for matrix in mat1:
        print(matrix)

matrix(row=x, col=y)  # In keyword arguments the key (row) conation value (x) and pass from 
matrix(col=y, row=x)  # function defenation (matrix(), name of the function)
