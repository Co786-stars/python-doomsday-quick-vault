# ------------------------all about function in this file-----------------
"""
def is a keyword that inform python we are ready to defining function. so thats why we call 
this line is function definition.

In function definition we declear the name of function followed by parentheses which can includes 
parameter-value the function can uses when it runs.

The Indented line follow the function definition is commonly known as body of given function .

The docstring is a special type of multiline comment that appears at the beginning of a function, 
class, or module that describe the job of function 

when we want to execute  function body from function definition then we use the name of function with 
without indentation called function call or calling function

A function call follow by any necessary information in parentheses  fthat tells python to execute 
block of code that perform specific job or task in function . 
"""
def square_pattern():
    """Printing the pattern by using square bracket"""
    row = int(input("Enter the row num : "))
    col = int(input("Enter the col num : ")) 
    mat = []
    for i in range(row):  # loop for row of mat
        mat1 = []
        for j in range(col): # loop for col of mat
            user = input(f"Enter your item >> [{i}][{j}] : ")
            mat1.append(user)
        mat.append(mat1)
    for k in mat:  #loop to print the matrix     
        print(k)
        
square_pattern()


