# WAPP to swap a two variable without using third temproary variable

x, y = 5, 6
x, y = y, x
print(x, y)

# _________________________________________________________________________________#
class Number:
    """class body swaping"""
    def __init__(self):
        self.x = float(input("Enter the 1st value : "))
        self.y = float(input("Enter the 2nd value : "))
    
    def swape(self):
        """function body display swape value"""
        print(f"x : {self.x} y : {self.y}") # before swaping
        self.x, self.y = self.y, self.x
        print(f"x : {self.x} y : {self.y}")  # after swaping
obj = Number()
obj.swape()
#___________________________________________________________________________________#

