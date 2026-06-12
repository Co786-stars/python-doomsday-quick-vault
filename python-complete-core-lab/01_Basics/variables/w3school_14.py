"""
--------------- Return value concept of Interpeter -------------- Return value concept of Interpeter 

Question ? what will happend when the interpeter read calling function after returned value 

ans))
The interpreter goes back to where the function was called (the loop in my case).
It continues executing the code after the function call.

"""



# using Function with infinite loop while loop :
def flower(fav_flower, flower_col):
    """Function body is use name of favorite flower and color"""
    flow = f"{fav_flower} {flower_col}"
    return(flow.title())

# infinite wile loop for collecting data 

''' while True:
    fav = str(input("Enter favorite flower : "))
    col = str(input("Enter favorite colour : "))
    fav_flower = flower(fav, col)
    print(fav_flower)

'''

while True:
    fav = str(input("favorite flower : "))
    col = str(input("favorite colour : "))
    if fav == 'exit':
        break
    if col == 'exit':
        break
    fav_flower = flower(fav, col)
    print(fav_flower)
