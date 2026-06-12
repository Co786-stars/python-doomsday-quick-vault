# 1
# 2 3 
# 4 5 6 
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 10 21  
# 22 23 24 25 26 27 28 

class Pattern:

    def __init__(self, row):
        self.user = row
    
    def floydpatt(self):
        value = 1
        for i in range(1, self.user+1): # i = 1, 2
            for j in range(1, i+1): # j = 1 to 2 > 1 ,  
                print(f"{value}", end=" ") # value = 1 
                value += 1
            print("")

x  = int(input("Enter value for Floid Pattern : "))
obj = Pattern(x)
obj.floydpatt()


# ______________using While loop ______________________________________

class FloydPattern:
    """Class is use to print the class pattern"""
    def __init__(self):
        """init is use to initilize the attributes"""
        self.user = int(input())
    
    def  pascalpattern(self):
        """function body use to print pascal pattern"""
        row, count = 1,1
        while  row < self.user+1:
            col = 1
            while  col < row+1:
                print(count, end=" ")
                count += 1
                col += 1
            print()
            row += 1

def runfunction():
    floyd = FloydPattern()
    floyd.pascalpattern()
runfunction()