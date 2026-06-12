""" Wap to print the Square pattern using oops method"""

class Pattern:
    """This class is use to print pattern using oops method"""
    
    @staticmethod
    def square_pattern():
        """This body is use to print the square pattern"""
        user  = int(input("Enter row number for  square   : "))
        for row in range(1, user+1):
            for col in range(1, user+1):
                print("* ", end=" ")
            print()
    
    @classmethod
    def pyramid_pattern(cls):
        """ This body is use to print the pyramid pattern"""
        cls.user = int(input("Enter row number for pyramid : "))
        spc = 2*cls.user-1
        for row in range(1, cls.user+1):

            for col in range(1, spc+1):
                print("-", end="")
            
            for astrisk in range(1, 2*row):
                print("* ", end="")
            print()
            spc -= 2 
    
    def __init__(self):
        """This body is use to print inverted half pyramid"""
        self.user = int(input("Enter the row number for inverted : "))
        self.ast = 2*self.user-1
        for row in range(1, self.user+1):

            for spc in range(1, 2*row):
                print("-", end="")
            
            for astrisk in range(1, self.ast+1):
                print("* ", end="")
            self.ast -= 2
            print()

            
pobj1 = Pattern()
pobj1.square_pattern()
pobj1.pyramid_pattern()

