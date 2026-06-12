# 1.> Print list in reverse order using a loop.
# 2.> Find the sum of the series up to n terms
# 3.> Find the Fibonacci series: 0  1  1  2  3  5  8  13  21  34
x = """import user define function in this module we define a function and import in other module using import keyword"""
# with open('testing.txt', 'w') as f2:
#     f2.write(x)
# import subprocess
# subprocess.Popen(['notepad.exe', 'testing.txt'])

def rev(): # check module 1stimportmodule.py file previous module
    """use to display list item in reverse order"""
    item = []
    i = True
    print("if you want to exit enter q button ") # indication to exit() from loop 
    while i:
        user = str(input("Enter multipal value : ")) # user input value as a string 
        if  user == 'q': 
            item.pop() # use to pop last extra value q which was all ready inserted in list 
            i = False   # i contain false value to stop loop iteration 
        else:
            item.append(user)         # append or store user value to list 
    print(f"orderwise list : {item}") # display list item on output
    item.reverse() # function is use to reverse list item in reverse order 
    print(f"reversed list : {item}") # use to display reverse list on output screen 

 
def srizesum():
    N = int(input("Enter the number : "))
    i, sum = 1, 0
    while i <= N:
        sum += i
        i += 1
    print(sum)


def fibonacci():
    user = int(input("Enter the number : ",))
    n1, n2 = 0, 1
    for i in range(user):
        print(n1, end= " ")
        v = n1 + n2
        n1 = n2
        n2 = v

