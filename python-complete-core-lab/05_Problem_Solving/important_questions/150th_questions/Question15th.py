# WAPP to print the whole prime number from 1 to nth .
# prime number : 2 3 5 7 11 15 

class PrimeNuber:
    """display the all prime number"""
    def __init__(self):
        """constructr is initilize attributees"""
        self.user_value = int(input("Enter value : "))

    def allnumbers(self):
        """function is display all prime numbers"""
        for i in range(1, self.user_value+1):
            if i > 1:
                for j in range(2, i):
                    if i%j == 0:
                        break
                else:
                    print(i, end=" ")

obj = PrimeNuber()
obj.allnumbers()



# class UserNumber:
#     """display the prime numbers"""
#     def __init__(self):
#         """initilize the attributes"""
#         self.unumber = int(input("Enter the user number : "))
    
#     def primenumber(self):
#         """display the all prime number"""
#         if  self.unumber<=1:
#             flag =True
#         else:
#             flag = False
            
#         for i in range(2, self.unumber):
#             if self.unumber%i == 0:
#                 flag = True
#                 break 
#             else:
#                 flag = False    

#         if flag:
#             print("Number Is Not Prime")
#         else:
#             print("Number Is Prime")
# prime = UserNumber()
# prime.primenumber()

