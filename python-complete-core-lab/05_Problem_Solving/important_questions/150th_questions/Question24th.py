# WAPP to convert Decimal to Binary, octal, Hexadecimal
# _____________________________________________________________________________#

def num(value = 10):
    print(f"Binary of {value} is {value:b}")
    print(f"octal of {value} is {value:o}")
    print(f"Hexadecimal of {value} is {value:x}")
num(20)


# _____________________________________________________________________________#

class NumberConversion:
    """display the number in other formats"""
    
    def __init__(self):
        self.number = int(input("Enter the number : "))
    
    def numbers(self):
        b = bin(self.number)  # for binary numbers
        o = oct(self.number)  # for octal
        h = hex(self.number)  # for hexa decimal
        print("Binary {0} Octal {1} HexaDecimal {2}".format(b, o, h))
obj = NumberConversion()
obj.numbers()

# _____________________________________________________________________________#