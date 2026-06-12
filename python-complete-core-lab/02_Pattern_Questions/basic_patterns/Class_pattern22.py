# Pant style pattern 
# 5 4 3 2 1  1 2 3 4 5

# 5 4 3 2      2 3 4 5

# 5 4 3          3 4 5

# 5 4              4 5

# 5                  5

class Pattern:
    """class body is use to handle pant style pattern"""
    def __init__(self):
        self.var1 = int(input("Enter the row number for Pant style patern : "))
    
    
    def pantstyle(self):
        """function body is use to print the pant style pattern"""  
        y = self.var1 
        for i in range(1, self.var1+1):
            
            for j in range(1, y+1):
                print((self.var1-j)+1, end=" ")
            x = (self.var1-j)+1
            
            for spc in range(1, 3):
                print(end=2*x*" ")

            for k in range(y):
                print(x, end=" ")
                x += 1
            
            y -= 1
            print("\n")
            
pant = Pattern()
pant.pantstyle()



