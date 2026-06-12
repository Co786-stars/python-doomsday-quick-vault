# ---------*
# -------*   *
# -----*       *
# ---*           *
# -*               *
# ---*           *
# -----*       * 
# -------*   *
# ---------*
def hollow_diamond_pattern(usr_val = 9):
    """Hollow dimoand pattern"""
    if usr_val%2 == 0: # condition is use to manage the even value and odd value 
        usr_val += 1
    else:
        usr_val += 0
    spc = usr_val 
    for i in range(1, usr_val+1):
        # use to initilize the row number of dimoand
        if i <= usr_val//2+1:
            # only uper part is printed according to this condition 
            for j in range(1, spc+1): # this loop is use for uper space of dimaond  (loop use as a space)
                print("", end="-") 

            for k in range(1, 2*i):  # loop is use as a lower space (loop as a column) 
                # condition is use to print the uper hollow part of dimaond
                if k == 1 or k == 2*i-1: 
                    print("*", end=" ")
                else:
                    print("-", end=" ")
        else:
            for j in range(1, 2*i-usr_val+1): # use for col and print space of lower part (loop use as a space)
                print("", end="-")
            
            for k in range(1, usr_val+spc):  # inner loop is use to print the hollow of dimond 
                if k == 1 or k == (usr_val+spc)-1:   # use to print the space astrisk at lower boder of pattern  
                    print("*", end=" ") 
                else:
                    print("-", end=" ") 
        print()
        spc -= 2 
value = int(input("Enter your Row Number : - "))
hollow_diamond_pattern(usr_val = value) 

