#WAPP to display the armstrong number from 1 to nth term 

#___________________________________________________________________________________#

class Armstrong:
    """display the armstrong number"""
    def __init__(self):
        self.range = int(input("Enter the first rage  : "))

    def display(self):
        """function body is to display armstrong number"""
        num = str(self.range)
        store = 0
        for i in range(len(num)):
            store += int(num[i])**int(len(num))
        if self.range  == store:
            print("Armstrong")
        else:
            print("Not Aramstrong")

if __name__ == "__main__":
    obj1 = Armstrong()
    obj1.display()

#___________________________________________________________________________________#

class Number:
    """display the armstrong number"""
    def __init__(self):
        """constructor is initilize attribute"""
        self.num1 = int(input("Enter the number : "))

    def armstrong(self):
        """display the all armstrong number"""
        for i in range(1, self.num1+1):
            self.num2 = 0 
            self.num3 = i   # store the value to perform armstrong actions
            if i > 0:
                for j in range(len(str(i))):
                    self.num2 += (self.num3 % 10)**len(str(i))
                    self.num3 = self.num3 // 10
            if i == self.num2: # check the all number one by one arm strong or not 
                print(f"{self.num2}")

if __name__ == "__main__":
    obj = Number()
    obj.armstrong()

#___________________________________________________________________________________#