# WAPP to check the number is Armstrong or No ? 
# number that equal to the sum of own digit each rise to the power equal to the 
# number of digits in the number . ex : - 153 = 1^3 + 5^3 + 3^3 = 153

# __________________________________________________________________________________#

class ArmNumber:
    """check the number is armstrong or not"""
    def __init__(self):
        """constructor is use to initilize attribute"""
        self.var1 = int(input("Enter the number : ")) # 153
        self.store = 0

    def strongnumber(self):
        """function is display armstrong number"""
        self.itr = self.var1  # 153 it = 153
        for i in range(len(str(self.var1))): # 0 1 2
            value = self.itr%10 # 3 5 1 # store the reminder # value = 3 5
            self.store += value**len(str(self.var1)) # 3^3 = 27 : 5^3 = 125 : 
            self.itr = self.itr//10 # decrease the last value # itr = 15 

        if self.var1 == self.store:
            print(f"{self.var1} is armstrong number")
        else:
            print(f"{self.var1} is not armstrong number")
obj1 = ArmNumber()
obj1.strongnumber()

# __________________________________________________________________________________#
# Another method

class StrongNumber:
    """check the number is armstrong or not"""
    def __init__(self):  # constructor is initilize the attributes
        self.num1 = int(input("Enter the number : ")) # 
        self.num2 = 0

    def armstrong(self):
        """body display the arm strong number"""
        self.value = str(self.num1)  # store given number as str to check lenght  
        for i in range(1, len(self.value)+1): # condition iterate equvlent to length of given number
            self.num2 += int(self.value[i-1])**len(self.value) # store all numbers and add it 
            
        if self.num2 == self.num1: # condition check number is equvlent to given or no
            print("{0} is armstrong number".format(self.num1))
        else:
            print("{0} is not armstrong number".format(self.num1))
                        
obj = StrongNumber()
obj.armstrong()

#______________________________________________________________________________________#