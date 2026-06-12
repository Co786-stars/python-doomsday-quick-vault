# WAPP to perform arthmatical operation ? addition and division

#_______________________________________________________________________________________#

x = 5  # task oriented
y = 2
print(x+y) # 7
print(x/y) # 2.5

# _______________________________________________________________________________________#

def addition():  # functional programming 
    """function body handle addition operation"""
    value1 = float(input("Enter the 1st value : "))
    value2 = float(input("Enter the 2nd value : "))
    sum = value1+value2
    return f"Sum of {value1} and {value2} is  : {sum}"
add = addition()
print(add)


def division():
    """function body handle division operation"""
    value1 = float(input("Enter the 1st value : "))
    value2 = float(input("Enter the 2nd value : "))
    division = value1/value2
    return  f"Division of {value1}/{value2} is  : {division}"
div = division()
print(div)

# In the both program "addition()" and "division()" we take a value1 and value2
# variables to store user_value for operation  addition and division.
# Then we take a sum and division variable to store addition and division value then 
# we return stored value to the calling function using f string method 
# The return value assign in add or div variable for display using "print()"

# _______________________________________________________________________________________#


class Operations: # object oriented programming
    """class body is perform the operations"""
    def __init__(self):
        
        self.var1 = float(input("Enter 1st number : "))
        self.var2 = float(input("Enter 2nd number : "))

    def sum(self):
        """function body is permorm adding operation"""
        add = self.var1+self.var2
        print(f"Sum {self.var1} + {self.var2} : {add}") 

    def division(self):
        """function body is permorm adding operation"""
        division = self.var1/self.var2
        print(f"Division {self.var1}/{self.var2} : {division}") 

def call_fun():
    """function body is use control the object"""
    obj1 = Operations()
    obj1.sum()
    obj1.division() 

call_fun()

# _______________________________________________________________________________________#

