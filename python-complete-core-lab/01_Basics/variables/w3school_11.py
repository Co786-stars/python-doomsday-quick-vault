# There are the many way to pass the argument in function definition 
# 1)) Positional argument
# 2)) Keyword argument
# 4)) Default argument
# 5)) Arbitary argument

"""
---------------------------- Arbitary argument ----------------------------------
Atribatry argument is denoted with an astrisk (*) that allow a function to accept variable 
function to accept a variable number of argument   

The arguments are packed into tuple which the function can then process as needed  

it provides flexibility for handling different quantities of input without explicitly specifying 
them in thefunction signature  

we use Atribatry argumet to pass the tuple so thats why we use astrisk(*) symbol to handling packed data as in 
the form of tuple .   

we use arbitrary argument to pass tuple as argument from parameter using * in  packed form 
commonly known as positional arbitrary argument  .

we use arbitrary argument to pass dictionary as argument from parameter using ** that is 
commonly known as keyword arbitrary   : -

"""



# def fun_1(*y):
#     print(y)
# fun_1()


def fun_2(*y):
    print(y)
fun_2(10, 20, 30)


# def fun_3(**y):
#     print(y)
# fun_3(i=10, j=20, k=30)


# def fun_4(x, *y):
#     print(x, end=" ")
#     print(y)
# fun_4(10, 20, 30)


# def fun_5(x, **y):
#     print(x, end=" ")
#     print(y)
# fun_5(x=10, j=20, k=30)




# -------------  Positional arbitrary argument --------------------- #
def make_pizza(*clint_pizza):
    """summarize the pizza of client"""
    print("\n You pizza order given with the following :- ")
    for pizza in clint_pizza:
        print(f"-> {pizza}")

make_pizza("pepperoni", 'little cheese')
make_pizza('mushroom', 'green pepper', 'extra cheese')


def making_pizza(size, *pizza_name):
    """ Ordering pizza for client program """
    print(f"Make {size} inch pizza :", end=" ")
    for pizza in pizza_name:
        print(f"-> {pizza}")
# order of client
pizza_order_1st = ("veg", "extra chess", "with salad")
pizza_order_2nd = ("Non_veg", "without_chess", "salty")
# function call pass from parameter size and pizza_name
making_pizza(19, pizza_order_1st) # take the order of client
making_pizza(17, pizza_order_2nd)

# -------------  keyword arbitrary argument --------------------- #


def profile(first, last, **user_info):
     """Use to containing everything which we know about user """
     user_info['first_name'] = first
     user_info['last_name'] = last
     return user_info

user_profile = profile("Aditya", "saurab",
                       location = "patna",
                       field = "CS branch")
print(user_profile)
