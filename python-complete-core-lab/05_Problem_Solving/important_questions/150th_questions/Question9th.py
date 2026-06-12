# WAPP to solve quadrtic equation ? 
# standard from of Quadratic equation ax^2 + bx + c = 0
# where a,b and c are real numbers and a != 0

import math
class Equations:
    """class body is display equation"""
    def __init__(self):
        """initilize the attribute"""
        # Input cofficent of a, b, and c 
        self.a = int(input("Enter the cofficent a : "))
        self.b = int(input("Enter the cofficent b : "))
        self.c = int(input("Enter the cofficent c : "))
    
    def quadratic(self):
        """function body display quadratic equation"""
        self.D = self.b**2-4*self.a*self.c # discrimant : b^2-4ac
        if self.D > 0:
            # Two real and distinct roots
            self.eq1 = -self.b + math.sqrt(self.D)/2*self.a
            self.eq2 = -self.b - math.sqrt(self.D)/2*self.a

        elif self.D == 0:
            # one real root is repreated
            self.eq1 = -self.b/2*self.a
        
        else:
            # Complex rooots when discrimant is negative
           real_val = -self.b/2*self.a  # -b/2a
           img_val =  math.sqrt(abs(self.D))/2*self.a # D/2a
           print(f"{real_val} + {img_val}i") 
           print(f"{real_val} - {img_val}i")

quad = Equations()
quad.quadratic()

