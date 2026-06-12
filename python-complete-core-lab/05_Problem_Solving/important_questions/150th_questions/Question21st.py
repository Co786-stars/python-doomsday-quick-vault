# WAPP to find the sum of natural number.
#____________________________________________________________________________________#

def numbers(value = 10):
    """display the sum of natural number"""
    addition = 0
    for i in range(1, value+1):
        addition += i
    print("The total addition is : {0}".format(addition))
x = int(input("Enter the number : "))
numbers(x)

#____________________________________________________________________________________#

class NaturalNumber:
    """Display the sum of natural number"""
    def __init__(self):
        """constructor is initilize attribute"""
        self.num1 = int(input("Enter the number : "))
        self.sum =  0
    def addition(self):
        """body display sum of natural number"""
        i = 1
        while i <= self.num1:
            self.sum += i
            i += 1
        print("Total Sum : ", self.sum)

obj = NaturalNumber()
obj.addition()

# __________________________________________________________________________________#


