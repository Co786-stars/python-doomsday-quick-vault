# full pyramid pattern basic code in function body
def full_pyramid_pattern(x):
    """Function body is use to print full pyramid pattern"""
    for i in range(1, x+1):         # This line is Use to show the row of pyramid pattern
        print((x+1-i)*"-", end="")  # after using the i am using end parameter because of adding next line
        print("*"*(2*i-1))
full_pyramid_pattern(x = 5)


# full pyramid using function with other logic or method
g_value = 10
def pattern_full_pyramid(row):

    spc = g_value
    for i in range(1, g_value+1):
        for j in range(1, spc+1):
            print("-", end="")

        for k in range(True):
            print("*"*(2*i-1), end="")
        print()
        spc -= 1
pattern_full_pyramid(row=g_value)


# full pyramid alphabetical numeric pattern using python

value = int(input("Enter your row number for full pyramid : "))
def full_pyramid(x, y):
    k = 1
    for i in range(1, x+1):            # This is for loop use to repeat the statement given below for space and print it
        print("-"*(value-i), end=" ")  # end parameter is used to add the next statement line 35  which is char of AB...
        for j in range(1, k+1):        # This line is use as a column for repeat the value with 1, 123, 12345...for  odd
            alpha = chr(y + j)         # use to exceed the value 1 from initially number 64 like 64, 65, 66,...etc and
            print(f"{alpha}", end="")  # char function is used to convert the value in character or print using f string
        print()
        k += 2
x, y = value, 64
full_pyramid(x, y)


# full pyramid alphabetical numeric  pattern using python code

row = int(input("Enter the row of full pyramid : "))
def alpha_full_pyramid(num, alpha):
    space = num
    count = 1
    for i in range(1, num+1):
        for j in range(1, space+1):
            print("-", end="")

        for k in range(1, count+1):
            char = chr(alpha+k)
            print(f"{char}", end="")
        print()
        count += 2
        space -= 1
alpha_full_pyramid(num=row, alpha=64)

# full pyramid for Numeric pattern using python code with while loop

x = 5
i = 1
count = 1
while i < x+1:
    print(" "*(x+1-i), end="")
    j = 1
    while j < count+1:
        print(j, end="")
        j += 1
    count += 2
    print()
    i += 1

# full pyramid for numeric data pattern using python code with wile loop
v_store = int(input("Enter your row number for numeric pattern : "))
def numeric_pattern_pyramid(row):

    i = 1
    num1 = 1
    while i < row+1:
        print("_"*(row+1-i), end="")

        for j in range(1, num1+1):  # we also use simple from like logic 2*i = 2, 4, 6, 8, 10
            print(j, end="")
        print()
        num1 += 2
        i += 1
numeric_pattern_pyramid(row=v_store)
