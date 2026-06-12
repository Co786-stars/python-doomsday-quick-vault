# In python every thing is object and we use class to manage the objects 
"""
step 1 > First of all we check the predefined datatype class which we all ready use in functional and procuderal programming
         there are the two type of class Bulit-in  and  user-define : -  
""" 
# --------------------------------------------------------------------------------------------------------------------------------#
# -------- : Built -In class : ----------------- : Built -In class : ------ : Built -In class : ----------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------#


x  = [1, 2, 3, 4, 5, 6]  
print(type(x)) # output ::  <class 'list'> 

x = (1, 2, 3, 4, 5, 6)
print(type(x))  #  output :: <class 'tuple'>

x = {1, 2, 3, 4, 5, 6}
print(type(x))  # output :: <class 'set'>

x = { 'p': 1,  'q': 2,  'r': 3}
print(type(x))  #  output :: <class 'dict'> 

x  = 100 
print(type(x)) # output :: <class 'int'>

x = 'hello'
print(type(x)) # output :: <class 'str'>

x = 20.9
print(type(x)) # oputput :: <class 'float'>

x  = 2 + 2j
print(type(x)) # output :: <class 'complex'>

x, y = False, True
print(type(x), type(y))  # output :: <class 'bool'>  <class 'bool'> 


def friends():
    """my all friends name"""
    friend_name = "abhishek sharma"    

x  = friends()
print(type(x))  # output ::  <class 'NoneType'>


x  = friends
print(type(x))  # output  <class  'function'>



# _________________|| 
# _________________|| 
# _________________||  CHECK OUT DIRECTLY CLASS 15 and then 2 3 4 . all
#                  ||  CLEAR A CONCEPT OF FUNCTION IN OOPS 