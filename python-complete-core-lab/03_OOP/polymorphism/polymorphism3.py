"""
Polymorphism : -

Polymorphism means "many forms" the ability of different objects to respond to the same method or function in different ways.
Polymorphism is fundamental concept in OOPs that allow object to process differently based on their datatype or class .

In python Polymorphism is  enhance code flexbility, reusability , readability and basically categorized in four parts 
<1> Functional polymorphism
<2> Operator polymorphism
<3> Class Polymorphism
<4> Polymorphism With inheritance
"""

"""
Operator polymorphism : -

Operator polymorphism allows the same operator to behave differently based on the context, especially when dealing with different
data types or objects     

In Python Operator Polymorphism explain how operator (+, -, *, **, /, // ) can be used for different types of operations based on 
the operands (the object of mathematical operation)

"""

# example : - 1st : -

x = 20 + 10
y = "2" + '3'
z = "Wiz" + "ard"

print(x, y, z) # output >> 30, 23, Wizard


# example : - 2nd : -
class Poly :
    """class body use to define about polymorphism topic"""
    
    def __init__(self, x = None, y= None, z = None):
        self.xvalue = x 
        self.yvalue = y
        self.zvalue = z
    
    def operator_poly(value):
        """use to return value"""
        x = 20 + 10
        y = "2" + '3'
        z = "Wiz" + "ard"
        return x, y, z


obj = Poly()   # after object creation memory is allocated for obj in os and first memory refrance assign as a argument
#              when we call class
x = obj.operator_poly()
print(x)


# explanation : - VVI
# In this example, we have a single or smae operator ( + ) is used to add two integers, concatenate two strings of digits
# and concatenate two alphabetic strings means this example define how the same operator can perform different operations 
# depending on the context (operands)



"""
# extra example : -
# Using the + operator for different purposes

# Adding two integers
result_int = 5 + 10
print(result_int)  # Output: 15

# Adding two strings
result_str = "Hello, " + "world!"
print(result_str)  # Output: Hello, world!

# Adding two lists
result_list = [1, 2, 3] + [4, 5, 6]
print(result_list)  # Output: [1, 2, 3, 4, 5, 6]

"""