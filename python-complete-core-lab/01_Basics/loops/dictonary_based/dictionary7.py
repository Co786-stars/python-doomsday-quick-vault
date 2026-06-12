import copyreg

x = {
    "Name"  : "Aditya",
    "Class" : "BCA",
    "ROLL"  : 2002,
    "Year"  : 2022
}
print(x)
print(x.items())
x["roman"] = "Rens"
print(x.keys())
print(x.values())

for y in x.items():
    print(y)

for y in x:
    print(x[y])

x.popitem()
print(x)

x.pop("Class")
print(x)
print("\n")
#>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<
copy1 = x.copy()
print(copy1)
print(copy1)

copy1.clear()

copy2 = dict(copy1)
print(copy2)
print(copy2)

