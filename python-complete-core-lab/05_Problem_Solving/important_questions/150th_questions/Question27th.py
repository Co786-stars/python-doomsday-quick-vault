# WAPP to display Fibonacci Sequence using Recursion
# fibonacci series : 0 1 1 2 3 5 8 13 .....nth
#__________________________________________________________________________________#

def fibonacci(user_value):
    """Display the fibonacci series"""
    var1, var2 = 0, 1
    i = 0 
    while i <= user_value:
        var3 = var1+var2
        print(var1)
        var1 = var2
        var2 = var3
        i += 1
        
#___________________________________________________________________________________# 
# using Recursion          # using Recursion                   # using Recursion  

def fiboseries(num):
    if num <= 1:
        return num
    else:
        return (fiboseries(num-1) + fiboseries(num-2))
    
num = int(input("Enter number : "))
if num <= 0:
    print("Enter positive number")
else:
    for i in range(num):
        print(fiboseries(i))

#___________________________________________________________________________________# 