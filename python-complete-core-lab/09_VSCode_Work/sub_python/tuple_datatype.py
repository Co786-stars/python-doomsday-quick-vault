# 1) How to create Tuple or Tuple items

"""var1 = () # empty tuple
print(var1)
var2 = (10, 20, 30, 40, 50)
var2 = ("str1", "str2", "str3")
var2 = (19.0, 12.3, 15.5, 17.9)
var2 = (2j, 2+2j, 3+3j, 5+9j)
var2 = (True, False)
print(var2)

# 2) How to access Tuple or Tuple items

x = ("str1", 50, 8j, 20.9, False)
print(x[3])
print(x[1])
print(x)
print(x[1:4])  # (50, 8j, 20.9)
print(x[-1])
print(x[-4:-1])
y = (15,)
# y = ("str1") # str1
print(y)
print(y[0])
z = (10, 20, 10, 20)
print(z) # tuple allow duplicate value or element


# 3) How to update Tuple items

color = ("red", "blue", "green")
color = list(color)
color[0] = "pink"
color = tuple(color)
print(color)

device = ("mobile", "monitor", "computer")
device = list(device)
device.append("router")
device = tuple(device)
print(device)

"""

