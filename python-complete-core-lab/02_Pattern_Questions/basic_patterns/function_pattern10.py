# Right half pyramid pattern without using function
user = int(input("Enter the row number : "))
for i in range(1, user+1):
    print(" "*i, end="")
    print("* "*user)


# Right Rombus pattern using function : -
def right_pattern(num1):
    """Right Rombus pattern given below"""
    for i in range(1, num1+1):

        for j in range(i):
            print(" ", end = "")

        for k in range(num1):
            print("*", end = " ")
        print()
right_pattern(int(input("Enter Row number of Right pattern : ")))


# Right alpha Rombus pattern using function : -
def right_rombus_pattern(value1, alpha=64):
    for i in range(1, value1+1):

        for j in range(1, i+1):  # for opposite counting (1, (value1-i+2)) logic
            print("-", end="")

        for k in range(1, value1+1):
            char = chr(alpha+k)
            print(char, end=" ")
        print()
usr = int(input("Enter the Row number : "))
right_rombus_pattern(value1=usr)


# Right numeric Rombus pattern with using simple function function

def rombus_pattern(value):
    """Right rombus pattern"""
    for i in range(1, value+1):
        print(" "*i, end="")
        for j in range(1, value+1):
            print(j, end=" ")
        print()
rombus_pattern(5)

# Right Rombus pattern with using simple function 

def rombus_pattern(g_value):
    """Right numeric rombus pattern"""
    for i in range(1, g_value+1):

        for j in range(1, i):
            print(" ", end="")

        for k in range(1, g_value+1):
            print(f"{k}", end=" ")        
        print()
rombus_pattern(10)

