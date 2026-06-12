# WAPP to check the Number is Odd or Even 
# _________________________________________________________________________________#

num1 = int(input("Enter Number : "))
if num1%2 == 0:
    print(f"{num1} is a Even integer")
else:
    print(f"{num1} is a Odd integer")

# _________________________________________________________________________________#

class EvenOdd:
    """class body is check number is or or even"""
    def __init__(self):
        """constructor is use to initilize the attributes"""
        self.user = int(input("Enter the Number : "))

    def check(self):
        """function body display number even or odd"""
        if self.user%2 == 0:
            print(f"{self.user} is even number")
        else:
            print(f"{self.user} is Odd number")
obj = EvenOdd()
obj.check()

# _________________________________________________________________________________#
