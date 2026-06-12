#Write a program to display the two number and their sum using inheritance.
class SumOfNumber:
    """class body try to display the sum of number"""
    def __init__(self, a, b):
        self.uservalue1 = a
        self.uservalue2 = b
        print(f"The sum of {self.uservalue1} + {self.uservalue2} is : {self.uservalue1+self.uservalue2}")

class Sum(SumOfNumber):
    
    def __init__(self):
        self.value1 = int(input("Enter the 1st number  : "))
        self.value2 = int(input("Enter the 2nd number  : "))
        super().__init__(self.value1, self.value2)

try:
    obj = Sum()
except Exception  as e:
    print("Error : ", e)

        


