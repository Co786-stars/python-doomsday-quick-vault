# binary number {:b}
# decimal number {:d}
# scientfic number {:e}
# precentage format {:%} , {:.0%}
# float value {:f} , {:.2f}
"""
1)) Decimal to Binary number {:b}
print("Binary number {} is {:b}".format(15, 15))
num = "Binary of {} is {:b}"
print(num.format(7,7))
print("{:b}".format(100))

2)) Binary to decimal {:d}
print("{:d}".format(0b1111))
x = "binary of {:b} is in decimal {:d} ".format(0b111,0b111)
y = "binary of {:b} is in decimal {:d} ".format(0b101,0b101)
print(x)
print(y)

3)) Decimal to scientfic number
print("The scientfic number {:d} is {:e}".format(5,5))
x = "{:e}".format(80)
print(x)

4 )) Binary to octal
print("Binary of {:b} is {:o} in octal value ".format(0b101, 0b101))

5)) Decimal to octal

print("Decimal of {} is {:o} in octal value ".format(5, 5))
x = "The octal value of 100 is {:o}"
print(x.format(100))

6)) decimal to hexadecimal

print("The decimal value {:d} is {:x} in hexadecimal format".format(11 ,11))
print("The decimal value {:d} is {:X} in hexadecimal format".format(14 ,14))
print("The decimal value {:d} is {:X} in hexadecimal format".format(15 ,15))
x = "{:x}".format(12)
print("value of 12 in hexa :", x)

7)) precentage format {:%} , {:.0%}
num = "precentage format {:.0%}"
print(num.format(0.25))

8))  float value format string

value = "this is float {:f}"
print(value.format(64))

value = "this is float {:.2f}"
print(value.format(64))

value = "this is float {:.1f}"
print(value.format(64))

"""

