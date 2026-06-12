def operators(a, b):
    print(f"{a+b}")
    print(f"{a-b}")
    print(f"{a*b}")
if __name__ == '__main__':
    try:
        n1 = int(input(f"Enter the value of a : " ))
        n2 = int(input(f"Enter the value of b : " ))
        operators(a=n1, b=n2)
    except:
        print("Pls enter valid number")

'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())


class Operators:
    """class body perform the operations on operands a and b"""

    def __init__(self, a, b):
        """constructor is initialized the operands"""
        self.num1 = a
        self.num2 = b

    def Performs_actions(self):
        """method is try to work on the actions"""
        if self.num1 == int(self.num1) and self.num2 == int(self.num2):
            self.sum_ = self.num1 + self.num2
            self.difference = self.num1 - self.num2
            self.product = self.num1 * self.num2
        else:
            return f"pls enter valid number"


class Display(Operators):
    """child body from Operators try to display the actions on operands"""

    def _display(self):
        """method is try to display the actions that we perform on operands"""
        super().Performs_actions()  # invoked the parents method
        print(self.sum_)  # display addition
        print(self.difference)  # display the substraction
        print(self.product)  # display the multiplication


try:
    userEntry = Display(a, b)  # argument is passed via user
    userEntry._display()  # output is shown on screen
    # userEntry.Performs_actions() #Noresponce is out in screen

except ValueError:
    errorMsg = f"Pls enter the Valid number"
    print(errorMsg)
'''

# Task/Question
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.



# Extra :- other method
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a + b)
#     print(a - b)
#     print(a * b)
