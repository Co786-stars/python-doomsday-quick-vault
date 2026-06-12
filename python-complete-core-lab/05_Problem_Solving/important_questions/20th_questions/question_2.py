# Write a program to display the area of square when side is given  using inheritance.
# area of aquare = side x side
class Square:
    def __init__(self):
        pass

class AreaOfSquare(Square):
    """define the area of square"""
    def area(self):
        side = int(input("Enter the side of square : "))
        return f"The area of square is {side*side}"

square_area = AreaOfSquare()
area_of_square = square_area.area()
print(area_of_square)


