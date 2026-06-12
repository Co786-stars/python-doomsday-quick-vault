Dict = {
    "fruits":"banana",
    "colour": "Red",
    "mouse": "logi"
}
print(Dict)
print(type(Dict))
print(Dict["fruits"])

Dict2 = {"Mobile": "Nokia", "laptop": "Lenovo", "tv": "LG", "tv":"LG"}
print(Dict2)
print(len(Dict2)) # duplicate value are never allow in Dictionary


Dict3 = {
    "Book"     : "Danish Riche",
    "copy"    : "classmate",
    "marker"  : "permanent",
    "color"   : ["Red", "Green", "Yellow" , "blue"],
    "company" : ("google", "microsoft"),
    "book"    : {"c_language", "python_language", "Java_language"}
}
print(Dict3["book"])
print(Dict3["color"])
print(Dict3["company"])
print(Dict3["Book"])

print(type(Dict3))

z = dict(name = "aditya", DOB=2005, Class="BCA")
print(z)









