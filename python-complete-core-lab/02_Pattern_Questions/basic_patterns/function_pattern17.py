def hollow_hourglass_pattern(row = 9): # function defination
        """Function is use to print the hollow hourglass pattern""" # function body  
        if row%2 == 1:
            pass
        else:
            row += 1
        spc = row
        for i in range(1, row+1): # outer loop use to manage row of hollow patterns 
            if i <= row//2:
                for j in range(1, 2*i): # inner loop for column 
                    print("-", end="")
                
                for k in range(1, (spc-2*i+1)+2): # count from 0 >>  9 7 5 3 >> if counting from 1 then      
                    if k == 1 or i == 1 or k == (spc+2)-2*i: # >> 10, 8, 6, 4 adding +1 when in logic when initilize
                        print("*", end=" ")   # from 1 >> logic use to mangage the hollow patterns 
                    else:
                        print(" ", end=" ")
            else:
                for j in range(1, spc+1):  # loop is use to manage the lower part of hourglass pattern 
                    print("-", end="")

                for k in range(1, (row+2)-spc):
                    if k == 1 or i == row or k == 2*i-row: # logis use to manage the hollow patterns 
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                spc -= 2
            print()

x  = int(input("Enter the row number : "))
hollow_hourglass_pattern(row = x) # function call 
