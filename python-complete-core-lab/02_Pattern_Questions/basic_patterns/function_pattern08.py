"""
 * * * * * * * * *
   * * * * * * *
     * * * * *
       * * *
         *
"""

x = int(input("Enter the row number : "))
s = 2*x-1
for i in range(1, x+1):
    
    for j in range(1, 2*i):
      y =  print("-", end="")

    for k in range(1, s+1):
       print("*", end=" ")
    s -= 2   
    print()




# inverted full alphabetical pyramid pattern with space using function
def inverted_full_alpha_pyramid(num1):
    s = 2*num1-1
    for i in range(1, num1+1):
        for j in range(1, 2*i):
            print("-", end="")

        for k in range(1, s+1):
            alpha = chr(64+k)
            print(alpha, end=" ")
        s -= 2
        print()
y  = int(input("Enter the row number for alpha pyramid : " ))
inverted_full_alpha_pyramid(y)



# inverted full pyramid pattern using without space
value = int(input("Enter the value for pyramid : "))
def inverted_numeric_pyramid(i):
    count = 2*i-1
    for x in range(1, i+1):

        for y in range(1, 2*x+1):
            print(" ", end="")

        for z in range(1, count+1):
            print(f"{z}", end=" ")
        count -= 2
        print()
inverted_numeric_pyramid(value)
