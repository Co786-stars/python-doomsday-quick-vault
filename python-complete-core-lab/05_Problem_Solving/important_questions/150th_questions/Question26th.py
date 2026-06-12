# WAPP to make a simple calculator with four basic mathmatical operations
#___________________________________________________________________________________#

class Calculator:
    """make a simple calculator"""

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operations(self):
        print("1 for add")
        print("2 for sub")
        print("3 for mul")
        print("4 for div")
        while True:
            num = input("select a number : 1/2/3/4 : ")
            if num == '1':
                self.c = self.a + self.b
                print(f"{self.a} + {self.b} : ", self.c)
            elif num == '2':
                self.c = self.a - self.b
                print(f"{self.a} - {self.b} : ", self.c)
            elif num == '3':
                self.c = self.a * self.b
                print(f"{self.a} x {self.b} : ", self.c)
            elif num == '4':
                self.c = self.a / self.b
                print(f"{self.a} / {self.b} : ", self.c)
            else:
                print("Invlid Numbers")

            value = input("are you exit ? : yes/no : ") 
            if value == 'yes':
                break
                
obj = Calculator(20, 10)
obj.operations()

#___________________________________________________________________________________#