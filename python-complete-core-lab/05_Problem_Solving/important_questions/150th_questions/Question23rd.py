# WAAP to find the HCF.
# The HCF, also known as GCD (Greatest Common Divisor), of two or more numbers is the largest number 
# that divides each of the numbers exactly.
# ex : HCF of 12 and 15 is 3 because 3 is the largest number that can divide both 12 and 15 without leaving a remainder.
# __________________________________________________________________________________________________________________________#

def hcf(x=5, y=10):
    if x > y:
        z = x
    else:
        z = y
    for i in range(1, z+1):
        if ( x % i == 0 ) and ( y % i == 0):
            hcf = i 
    print("HCF : ", hcf)
hcf(24, 54)
# __________________________________________________________________________________________________________________________#

class Number:
    """boy is display the hCf od numbers"""
    
    def __init__(self):
        self.number1 = int(input("Enter the number : ")) # first number
        self.number2 = int(input("Enter second number : ")) # second number
    def hcfnumber(self):
        """function body is display hcf"""
        if self.number1 > self.number2:
            self.greater = self.number1 # store the greater number
        else:
            self.greater = self.number2  # store grater number 
 
        for i in range(2, self.greater+1): # # iterate at the end of greater number(g-1)
            if (self.number1%i == 0) and (self.number2%i == 0) : # find the highest number that is that exact devide both of them 
                self.hcf = i
                
        print(self.hcf)
obj = Number()
obj.hcfnumber()


# __________________________________________________________________________________________________________________________#