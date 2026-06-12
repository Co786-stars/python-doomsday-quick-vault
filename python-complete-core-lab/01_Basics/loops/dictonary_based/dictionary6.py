collection = {
    "Fruits" : "Apple",
    "Brands" : "Walla",
    "Colour" : "Dark_Red",
    "expiry" : 2025
}



for x in collection:
    print(x)

print("\n")

# print(collection["Fruits"])  example like that

for x in collection:
    print(collection[x])

print("\n")

# to access one by one item of the dictionary
for x in collection.items():
    print(x)

print("\n")

# to access one by one key item of the dictionary
for x in collection.keys():
    print(x)

print("\n")

# to access one by one key item of the dictionary
for x in collection.values():
    print(x)

