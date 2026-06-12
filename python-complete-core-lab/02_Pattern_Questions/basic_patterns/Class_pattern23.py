# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
#    1 
#    1    2    1 
#    1    2    4    2    1 
#    1    2    4    8    4    2    1 
#    1    2    4    8   16    8    4    2    1 
#    1    2    4    8   16   32   16    8    4    2    1 
#    1    2    4    8   16   32   64   32   16    8    4    2    1 
#    1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #
# .__________________________next time________________next time____________________next time___________________next time_________ #

def squarepattern(user):
    "function body is use to print the square pattern number"
    if user%2 == 0:
         user += 1
    for i in range(1, user+1):

        for j in range(1, user+1):
            print("*", end=" ")
        
        for j in range(1, 4):
              print(" ", end=" ")

        for j in range(1, user+1):
                print(f"{j}", end=" ")
        
        for j in range(1, 4):
              print(" ", end=" ")
              
        for j in range(1, user+1):
                print("<>", end="")

        for j in range(1, 4):
            print(" ", end=" ")
            
        if i <= user//2+1:
              for k in range(1, i+1):
                print("*", end=" ")
        else:
             for _ in range(1, (2*k-i)+1):
                print("*", end=" ")
                                    
        print()
squarepattern(15) # function call