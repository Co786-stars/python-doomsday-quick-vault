
# WAPP to convert the Celsius to Fahrenheit and kelvin?
# F = (9/5 x C) + 32
# C = 5/9 x (F - 32)
# C = K - 273
# K = C + 273

# ___________________________________________________________________________________#

c = 15.56
k = c + 273
f = (9/5*c)+32
print(f"The temprature {c} Celsius is equal to {f} Fahrenheit and {k} Kelvin")

#______________________________________________________________________________________#

def temprature():
    cel = float(input("Enter degree celsius : "))
    fra = (9/5*cel)+32 # celsius is convert into fahrenheit
    print(f"The {cel} celsius is Equal to {fra} Frhrenheit")
temprature()

# _____________________________________________________________________________________#

class Temprature:
    """class body is display temprature in celsius"""
    def __init__(self):
        """constructor is initilize attributes"""
        self.celsius = float(input("Enter temprature  : "))
    
    def fahrenheit(self):
        """function bod disply temprature in fahrenheit"""
        self.f = (9/5*self.celsius)+32
        self.k = self.kelvin()

    def kelvin(self):
        """function bod disply temprature in kelvin"""
        return self.celsius+273
    
    def display(self):
        """function body display celsius to kelvin or Fahrenheit"""
        self.fahrenheit()
        print(f"Temprature {self.celsius} celsius is equal to {self.f:2} Fahrenheit")
        print(f"Temprature {self.celsius} celsius is equal to {self.k} Kelvin")

temp = Temprature()
temp.display()

# ___________________________________________________________________________________#
