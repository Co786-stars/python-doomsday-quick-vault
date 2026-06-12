#  * * * * * * * * *
#    *           *
#      *       *
#        *   *
#          *
#        *   *
#      *       *
#    *           *
#  * * * * * * * * *

class Pattern:

    def __init__(self, row = 9):
        """init is use to initilize attributes"""
        if row%2 == 1:
            pass
        else:
            row += 1
        spc = row
        for i in range(1, row+1):
            if i <= row//2:
                for j in range(1, 2*i):
                    print("-", end="")
                
                for k in range(1, (spc-2*i+1)+2): # count from 0 >>  9 7 5 3 >> if counting from 1 then      
                    if k == 1 or i == 1 or k == (spc+2)-2*i: # >> 10, 8, 6, 4 adding +1 when in logic when initilize
                        print("*", end=" ")   # from 1 
                    else:
                        print(" ", end=" ")
            else:
                for j in range(1, spc+1):
                    print("-", end="")

                for k in range(1, (row+2)-spc):
                    if k == 1 or i == row or k == 2*i-row:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                spc -= 2
            print()
            
hologram = Pattern(row = int(input("Enter row number : "))) # there are two argumnet passs from __init__ when
# object is hologram is created first is memory referance/address from self parameter and second is  user 
# input from row (using keyword agrumenta and default value is also given 9 (means default argument))



