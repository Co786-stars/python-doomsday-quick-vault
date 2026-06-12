# THIS IS FOR PRACTIC HOLLOW DIMOAND AND HOLOW HOURGLASS PATTERN
"""
         *                       1                       A
       *   *                   1   1                   A   C
     *       *               1       1               A       E
   *           *           1           1           A           G
 *               *       1               1       A               I
   *           *           1           1           A           G
     *       *               1       1               A       E
       *   *                   1   1                   A   C
         *                       1                       A 
"""
from Class_pattern21 import HollowHourglass

class PatternP:
    """This class is use to print the Hollow dimond pattern"""
    def __init__(self):
        self.user_value = int(input("Enter the row number : "))
        self.hourglass = HollowHourglass() # create the object  of Hollowhourglass pattern

    # def run_pogram(self):
    #     """use to call all patterns"""
         # use to send the memory reffrence of this class

    def hollowhourglass(self):
        """Function body is use to print hollow hourglass pattern"""
        if self.hourglass.user_input%2 == 0:
            self.hourglass.user_input = self.hourglass.user_input+1
        user = self.hourglass.user_input
        for i in range(1, self.hourglass.user_input+1):
            """loop is use to control row of the Hollowhourglass"""
            if i < self.hourglass.user_input//2+1 : 
                for j in range(1, 2*i):        # 1 3 5 7  9
                        print("", end=" ") 
                for k in range(1, (self.hourglass.user_input-j)+2):
                    if k == 1 or k == user-j+1 or i == 1:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            else:
                for j in range(1, user+1): # 7 5 3 1
                    print(" ", end="")
                
                for k in range(1, 2*i-self.hourglass.user_input+1):
                    if k == 1 or i == self.hourglass.user_input or k == self.hourglass.user_input-j+1:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                user -= 2
            print()


        
    def hollowglass(self):
        """Function body is use to run the program"""
        if self.user_value%2 == 0:
                self.user_value = self.user_value +1
        countspace = self.user_value
        for i in range(1, self.user_value +1): # this loop is use as a row 
            if i < self.user_value//2+1:
                for j in range(1, countspace+1): # this loop print the space
                    print(" " , end="")
                
                for k in range(1, 2*i): # loop is use to print the pattern upper half pyramid
                    if k == 1 or k == 2*i-1: #  logic is use to check the last value and initial value of pattern
                        print(f"*", end=" ")
                    else:
                        print(" ", end=" ")              
            else:
                for j in range(1, 2*i-self.user_value+1): # 3 5 7 9 # this loop print space 
                    print(" ", end="")
                
                for k in range(1, self.user_value+countspace): # this loop is use to print the lower pyramid part
                    if k == 1 or k == self.user_value-j+1: #  logic is use to check the last value and initial value of pattern
                        print(f"*", end=" ")
                    else:
                        print(" ", end=" ")
                        
            countspace -= 2 # -1 -3 -5 -7 
            print()
        

    def floyd_pattern(self):
        """funcion body is use to print the floyd pattern"""
        val = 1
        for i in range(1, self.hourglass.flod_input):
            for j in range(1, i+1):
                print(f"{val}", end=" ")
                val += 1
            print()


    def Horiz_num_table(self):
        """function body is use to print the horizentel table"""
        count = 1
        while count < self.hourglass.h_table+1:
            value = 1
            while value < count+1:
                print(f"{count*value}", end=" ")
                value += 1
            print("")
            count += 1


def function_call():
    hollow1 = PatternP()
    hollow1.hollowglass()
    hollow1.hollowhourglass()
    hollow1.floyd_pattern()
    hollow1.Horiz_num_table()
function_call()


