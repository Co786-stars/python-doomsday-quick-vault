# WAPP to check the Number is positive Negative or Zero

# ___________________________________________________________________________________#

def myfun():
    num = int(input("Enter the number :"))
    if num  > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Nither positive Nor Negative")
myfun()

# ___________________________________________________________________________________#

class NumberCheck:
    """class body display +ve, -ve, integer"""
    def __init__(self):
        """constructor is initilize the attribute"""
        self.num1 = int(input("Enter the number : ")) 
    
    def display(self):
        """function body is check and display number"""
        if self.num1 < 0:
            print(f"{self.num1} is Negative")
        elif self.num1 > 0:
            print(f"{self.num1} is Positive")
        else:
            print(f"{0} is either negative Nor Positive")
obj1 = NumberCheck()  # creating the object obj1
obj1.display()

# ___________________________________________________________________________________#

