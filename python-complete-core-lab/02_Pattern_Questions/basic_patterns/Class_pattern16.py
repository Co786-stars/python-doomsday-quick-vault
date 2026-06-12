#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *            *
#     *       *
#       *   *
#         *

class HollowPattern:

    def __init__(self):
        """use to initilize attributes"""

    def hollow_diamond_pattern(self):     
        user = int(input("Enter row of Hollow Dimoand : - "))
        if user%2 == 1: # condition is use to manage even and odd value 
            user += 0
        else:
            user += 1
        spc = user
        for i in range(1, user+1): # value of i = 1 2 3 4 5 6(else) 7 8 9
    
            if i <= (user//2)+1: 
                for j in range(1, spc+1): # value of spc 9, 7, 5, 3, 1 > loop is use to print row pyramid
                    print("-", end="")
                
                for k in range(1, 2*i): # loop is use to print the column of dimond pattern
                    
                    if k == 1 or k == 2*i-1:  # condition is use to left and right upper astrisk of pyramid
                        print(f"*", end=" ")
                    else:
                        print("-", end=" ")
            else:
                for j in range(1, 2*i-user+1): # 4, 6, 8, 10 > loop is use to print the row of inverted pyramid
                    print("-", end="")

                for k in range(1, user+spc):  # This is use to print the astrisk as a column
        
                    if k == 1 or k == (user+spc)-1:  # condition is use to manage left and right lower astrisk
                        print("*", end=" ")
                    else:
                        print("-", end=" ")
            print()
            spc -= 2 # value of spc >> 7 5 3 1, -1, -3, -5, -7

#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
class Pattern(HollowPattern):
    
    def  __init__(self):
        self.user = int(input("Enter Row for pyramid : "))
        self.store = self.user
        i = 0 
        while i < self.user:
            j = 0
            while j < self.store:
                print("-", end="")
                j += 1 
            k = 0
            while k < 2*i+1:
                print(f"{chr(65+k)}", end="")
                k += 1
            print() 
            i += 1
            self.store -= 1
    

holopat = HollowPattern() 
holopat.hollow_diamond_pattern() 
pat = Pattern()  # out the program coded under the child class 


