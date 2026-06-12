#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1


class Pattern:
    """class is use to print pattern"""
    def __init__(self):
        self.user = int(input("Enter the row of pascal pattern : "))
    
    def pascalpattern(self):
        value = 1
        for i in range(1, self.user+1): # use to print space
            
            for k in range(1, self.user-i+2):  # use to print space
                print("", end="_")
            
            value = 1
            for j in range(1, i+1):  # use to print column
                # if i == 1  or j== 2*i-j:
                    print(f"{value}", end=" ")
                    value = value*(i-j)//(j)   # formula value*(i-j)//(j+1) 
                # else:
                    # print(f"{j}", end=" ")    
            print()

def runprogram():
    pascal = Pattern()
    pascal.pascalpattern()
runprogram()

