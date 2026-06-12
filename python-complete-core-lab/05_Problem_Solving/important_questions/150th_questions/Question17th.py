# WAPP to display the multipalication Table .
#____________________________________________________________________________#
for i in range(1, 11):
    print(2, "x", i, "=", 2*i)  # Table of 2 

#____________________________________________________________________________#
class SequenceTable:
    """Display the table"""
    
    def __init__(self):
        """initilize the attributes"""
        self.number = int(input("Enter the number : "))
    
    def table(self):
        """function is use to display table"""
        for i in range(1, 11):
            print(f"{self.number} x {i} = {self.number*i}")
obj = SequenceTable()
obj.table()

#____________________________________________________________________________#