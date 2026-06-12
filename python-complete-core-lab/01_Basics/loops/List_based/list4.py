color1 = ["red", "green", "blue", "black"]
color2 = ["grey", "bright", "yellow", "pink"]

x = color2.copy()
print(x)

#append()

color2.append("dark")
print(color2)

# clear()
color1.clear()
print(color1)

# copy()
z = color2.copy()
print(z)

color1 = color2.copy()
print(color1)

print(color1.count("grey"))
print(color1.count("red"))
print(color2.count("pink"))
x = color2.count("dark")
print(x)

color2.extend(color1)
print(color2)

color2.remove(color2[1])
print(color2)
x= color2.index("bright")
print(x)
print(color2.index("grey"))

color2.insert(1,"bright")
print(color2)

color2.pop()
color2.pop()
color2.pop(0)
print(color2)

color2.reverse()
print(color2)

