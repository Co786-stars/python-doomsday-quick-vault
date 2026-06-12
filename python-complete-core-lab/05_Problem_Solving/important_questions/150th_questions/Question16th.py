# WAPP to print the factorial of a number ?
# _______________________________________________________________________#
num1 = 1
user = int(input("Enter number : "))
if user == 0:
    print("Factorial of zero is 1")
elif user > 0:
    print(f"Factorial of {user} => ", end= "")
    for i in range(2, user+1):
        """factorial of a number"""
        print(f"{i}! ", end=" ")
        num1 = num1*i  # num1 is store the valuse and multiply with existing value of i
    print(f": {num1}")
else:
    print("Factorial is not exist")

# _______________________________________________________________________#
class FactNumber:

    def __init__(self):
        self.fact = int(input("Enter the Number : "))
        self.num = 1
    
    def factorial(self):
        """display the factorial of a Number"""
        if self.fact > 0: # condition is check number is positive or not
            for i in range(1, self.fact+1):
                self.num = self.num*i
            print(f"Factorial of a integer {self.fact} is : {self.num}")
        elif self.fact == 0: # in case number is equal to 0 thendisplay 1 
            print("Factorial of integer {0} is : {1}".format(self.fact, 1))
        else: # number is negative then display factorial not exist
            print("Factorial of Negative integer does Not exist ")
obj = FactNumber()
obj.factorial()

