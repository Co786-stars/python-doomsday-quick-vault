#practic previous pattern 8 inverted full pyramid using star with space
#-* * * * * * * * * 
#---* * * * * * * 
#-----* * * * *
#-------* * *
#---------*
def inverted_pattern(num1):
    z = 2*num1
    for i in range(1, num1+1):

        for j in range(1, 2*i):
            print("-", end="")
        
        for j in range(1, z):
            print(f"{chr(j+64)}", end=" ")
        z -= 2
        print()
usr = int(input("Enter your number : "))
inverted_pattern(usr)

"""______________________________________________________________________________________________"""

# Left Rombus pattern using without using function

x = int(input("Enter your number for left pattern : "))
for i in range(1, x+1):
    print(" "*(x-i+1), end='')
    print("* "*x)

# Left Rombus pattern using without function other method
y = int(input("Enter your number for left pattern : "))
for i in range(1, y+1):    # i =  1  2 3 4 5
    for j in range(1, (y-i+2)):  # = 1 2 3 4 5 >> 1 2 3 4 >> 1 2 3 >> 1 2 >> 1
        print("-", end="")

    for k in range(1, y+1):     # 1 to 6 >> 1 2 3 4 5
        print("*", end=" ")    # * * * * * >> * * * * * >> * * * * * >> * * * * * >> * * * * *
    print()

# -----* * * * *
# ----* * * * *
# ---* * * * *
# --* * * * *
# -* * * * *

# Left alpha Rombus pattern using function given below : --
def rombus_pattern(num1):
    for i in range(1, num1+1):
        for j in range(1, (num1-i+1)+1):
            print("-", end="")

        for k in range(1, num1+1):
            print(f"{chr(k+64)}", end=" ")
        print()
x = int(input("Enter the value : "))
rombus_pattern(num1 = x)



# Left numeric Rombus pattern using function given below : --

print("Enter the numeric value for numeric Rombus  : -")
numeric = int(input("Enter the Row number for rombus pattern :  "))
def numeric_pattern(num2):
    """Numeric rombus pattern"""
    i = 0
    while i < num2:
        j = num2
        while j > i:
            print("", end="-")
            j -= 1
        k =0
        while k < num2:
            print(f"{k+1}", end=" ")
            k += 1
        print()
        i += 1
numeric_pattern(numeric)

# -----1 2 3 4 5
# ----1 2 3 4 5
# ---1 2 3 4 5
# --1 2 3 4 5
# -1 2 3 4 5


# Left numeric Rombus pattern using other logic given below : --
