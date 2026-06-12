# 1. Circle area calculator using class and decorator
    #Write a program to display the area of circle when radius is given using class and decorator.

def areaofcircle(recvr):
    """"""
    def warpper(r):
        obj = recvr(radius = r)
        var1 = obj() # to initilize the __call_ dunde
        return f"The area of circle is {var1:.2f}"
    return warpper 

@areaofcircle
class Circle:
    """"""
    def __init__(self, radius):
        self.radius = radius

    def __call__(self):
        self.area = (22/7)*self.radius*self.radius
        return self.area
    
try:
    roc = float(input("Enter the radius of circle : "))
    _ = Circle(r = roc)  #warpper(r = roc)
    print(_)

except:
    ValueError("Invalid input")




# ------------------------------------------------------------------------------------------
# basic Questions :- using decorator -> area of circle : pi* r* r
def circle_checking(func):
    def inside():
        area_of_circle = func()
        return area_of_circle
    return inside


def circle_area():
    radius  = float(input("Enter the radius of circle : "))
    area_c  = (22/7)*radius*radius 
    return area_c

# decorator use mannualy
circle_checking = circle_checking(circle_area)
total_area = circle_checking() # similar : inside()
print(f"The total area of circle is : {total_area :.2f}")

# ------------------------------------------------------------------------------------------
# decorator use directly  not mannualy -> area of circle : pi* r* r

def circle_checking(func):
    def inside():
        area_of_circle = func()
        print("Circle area : ", area_of_circle)
        return area_of_circle
    return inside


@circle_checking 
def circle_area():
    radius  = float(input("Enter the radius of circle : "))
    area_c  = (22/7)*radius*radius 
    return area_c

# ❓ inside() ko call kaise hota hai?
# Answer: Jab tum circle_area() likhte ho, tum actually inside() ko call kar rahe ho —
#         kyunki decorator ne circle_area ko overwrite kar diya hai.
# circle_area() # calling the decorator function. direct encountred line inside function
# ------------------------------------------------------------------------------------------

