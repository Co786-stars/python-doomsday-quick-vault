# Write a program to swap two number ?
# _____________________________________________________________________________________#

x = 5   # swaping using third variable
y = 6
print(f"x = {x}, y = {y}") # before swaping
z = y 
y = x
x = z
print(f"x = {x}, y = {y}") # after swaping

# _____________________________________________________________________________________#

def number():
    """function body use to swap the number"""
    
    num1 = int(input("Enter 1st number : ")) # 10
    num2 = int(input("Enter 2nd number : ")) # 20
    print(f"Before swaping : num1 {num1} num2 : {num2}") # 10 , 20
    num1 = num1+num2  # 30  # swaping using two variables 
    num2 = num1-num2  # 10
    num1 = num1-num2  # 20  
    print(f"After swaping : num1 {num1} num2 : {num2}") # 10 20
number()

# _____________________________________________________________________________________#


class Swaping:
    """perform swaping program"""
    def __init__(self):
        """initilize the attribute"""
        self.var1 = int(input("1st Value : ")) # 10
        self.var2 = int(input("2nd Value : ")) # 20
    
    def swaping(self):
        """function body is use for swaping"""
        l1 = [] # swaping using array or list
        l1.append(self.var1)
        l1.append(self.var2) 
        self.var1 = l1[1]
        self.var2 = l1[0]
        print(f"1st Value : {self.var1}")
        print(f"2nd Value : {self.var2}")

swap = Swaping()
swap.swaping()

# _____________________________________________________________________________________#
