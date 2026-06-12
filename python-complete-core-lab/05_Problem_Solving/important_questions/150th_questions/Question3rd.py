# WAPP to find the area of traingle ?
# Area of traingle : 1/2(base*hieght)

# _____________________________________________________________________________________#
base = 10 
length = 20
print(1/2*base*length) # 100.0

# _____________________________________________________________________________________#

def traingle():
    """function body print area of trainge"""
    base = float(input("Enter the base of traingle "))
    length = float(input("Enter the length of traingle "))
    area = 0.5*base*length
    print("area of traingle is : ", area)
traingle()

# _____________________________________________________________________________________#

class Traingle:
    """class body is find area of traingle"""
    def area():
        x = float(input("Enter the Base   : "))
        y = float(input("Enter the Length :"))
        z = 1/2*(x*y)
        print(f"Area of Traingle is : {z}")
tri = Traingle
tri.area()

# _____________________________________________________________________________________#