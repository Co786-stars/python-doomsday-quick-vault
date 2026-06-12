# WAPP to find LCM .
#____________________________________________________________________________________#

def lcm(a=5, b=10): # default parameter value is use in this fucntion 
    if a > b:  # check the number is greater or not
        g  = a
    else: 
        g = b 
    for i in range(a, b):
        if g % a == 0 and g % b == 0:  # devide the common numer
            lcm = g
        g += 1
    print("LCM : ", lcm)

lcm()  # function call

# LCM of two or more numbers is the smallest multiple that is exactly divisible by each of the numbers. 
# ex : LCM of 4 and 5 is 20 because 20 is the smallest number that both 4 and 5 can divide without leaving a remainder.
# LCM means the smallest number that exactly devisible by two or comman devisior 6, 4 divisor of 
# 12 (nereast number divisible by both)

#____________________________________________________________________________________#

class LCM:
    """Display the sum of the number"""
    
    def __init__(self):
        self.number1 = int(input("Enter the 1st number : "))  # first number
        self.number2 = int(input("Enter the 2nd number : ")) # second number
    
    def lcmnumber(self):
        """body is find the lcm number"""
        if self.number1 > self.number2:
            self.greater = self.number1  # check the number is greater or not .
        else:
            self.greater = self.number2  # check the number is greater or not

        while True:
            # Use to find the common number that exactly divisible by both of them 
            if (self.greater % self.number1 == 0) and (self.greater % self.number2 == 0):
                lcm = self.greater
                break
            self.greater += 1  # if number is not divisible the excced 1 again and agin
        return print(f"The Lcm of {self.number1} and {self.number2} is {lcm}")
            
obj = LCM()
obj.lcmnumber()

#____________________________________________________________________________________#


