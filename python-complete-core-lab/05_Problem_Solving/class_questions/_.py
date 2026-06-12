# Question 1st : -
"""
Make a class called Restaurant The __init__ method should store two attribute a restaurant_name and 
a cuisine_type. Make a method called describe_restruant() that print this two pieces of information and a
method called open resturant() that prints a message indicating that the restaurant is open 
Make a instanse called restaurant from your class print the two attributem individually and then called both
method

# """
# class Restaurant:
#     """body contain info about restaurant"""
#     def __init__(self, name, type=' '):
#         """function body initilize attribute """
#         self.restaurant_name = name
#         self.cuisine_type = type
    
#     def describe_restaurant(self):
#         """function body provide info about restaurant"""
#         print(f"{self.restaurant_name} restaurant is open")

# restaurant = Restaurant(name= "Wizard")
# print(restaurant.restaurant_name, restaurant.cuisine_type)
# restaurant.describe_restaurant()

# # _________________________________________________________
# # Question 2nd : -

# """
# Now
# create three different instance from the class, and call describe_restaurant()
# for each instance
# """

# instance1 = Restaurant("wizard") # this line create the object 1st
# instance2 = Restaurant("wannon") # this line create the onject 2nd 
# instance3 = Restaurant("winwiz") # this line create object 3rd
# # Now  calling time using all instance 
# instance1.describe_restaurant()
# instance2.describe_restaurant()
# instance3.describe_restaurant()
 
# Question 2

class User:
    """class body store use information"""
    def __init__(self, fname, lname):
        """constructor __init__ create two attribute"""
        self.first_name = fname
        self.last_name = lname
    
    def describe_user(self, age):
        self.my_age = age
        print(f"My name is {self.first_name} {self.last_name}")
        print(f"I am {self.my_age} year's old")

    def greet_user(self):
        print(f"You are more vlauable for me ")

my_info = User("Aditya", "Raj")
my_info.describe_user(20) # use to call method 
my_info.greet_user()
