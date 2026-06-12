"""
--------------- Return value concept of Interpeter -------------- Return value concept of Interpeter------------------------- 
"""

# def course():
#     """the return value pass list from function call"""
#     x = [1, 2, 3, 4, 5]
#     x.reverse()
#     return(x.reverse())
# y = course()
# print(y)


# Passing a list 

"""def colors_name(colors):
    for color in colors:
        print(f"my favorite color is {color}")

list1 = []
for i in iter(str, 1):  # iter is use to create/ iterate infinete loop 
    print("Enter 'exit' to remove : ")
    s = str(input("Enter color name : "))
    list1.append(s)
    
    if s == 'exit':
        i = False
        list1.pop()
        break
    print(i)
print(f"My List : {list1}")
colors_name(list1)


# passing the list in python 
def greeting_users(names):
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

user_names = []
for i in iter(str, 1):
    username = str(input("Enter the str value : "))
    user_names.append(username)

    if username == 'exit':
        user_names.pop()
        break

greeting_users(user_names)
    
"""

# x  = ["red", 'green', 'blue', 'yellow']
# y  = []

# while x:
#     z = x.pop()
#     print(f"color : {z}")
#     y.append(z)
# #  display the all module a.c to list 
# print(y)
# for color in y:
#     print(f"Your favroite color is : {color}")


def make_pizza(size, *order):
    print(f'Make {size} ich pizza with given orders : -')
    for extra in order:
        print(f"- {extra}")


