# WAPP to print the fibonacci sequence
# fibonacci sequence : 0 1 1 2 3 5 8 13 21 34 55 89 144..nth

# ________________________________________________________________________________________#

var1, var2 = 0, 1
var3 = int(input("Enter the value : ")) 
for i in range(1, var3+1):
    print(var1, end=" ")
    var4 = var1 + var2
    var1 = var2
    var2 = var4
# ________________________________________________________________________________________#

class FiboNacci:
    """Display the fibonacci sequence"""
    def __init__(self):
        """constructor is initilize attribute"""
        self.user = int(input("Enter the number : "))
        self.num1 = 0
        self.num2 = 1
    def fibonacci(self):
        """display the fibonacci series"""
        for i in range(1, self.user+1): # loop count the fibinacci to nth term 
            print(self.num1, end=" ")
            self.store = self.num1 + self.num2  # store the addition of num1 and num2
            self.num1 = self.num2   # store the value of num2 in num1 
            self.num2 = self.store  # store the value of store variable in num2

fibo = FiboNacci()
fibo.fibonacci()

# __________________________________________________________________________________________#
            
