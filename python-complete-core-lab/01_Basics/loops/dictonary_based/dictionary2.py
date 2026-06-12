book = {
    "Book": "Computer language",
    "Name": "C++ language",
    "Price": 2500
}
# store = book["Price"] # both give same result
store = book.get("Price") # both give same result
print(store)

x = book.keys() # use to store all the key in the dictonary
print(x)


exam = {
    "BCA": 2022,
    "BBM": 2024,
    "BSC": 2025,
    "BBA": 2030
}

print(exam.keys())
print(exam.values())
print(exam)

exam["B-TEC"] = 2025
exam["B-COM"] = 2022  # meathod use to add the key_value in dictonary
exam["CS"]    = 2030 # it use to add new key_value in dictonary
print(exam)




x = {
    "company" : "Lenovo",
    "Product" : "Laptop",
    "Version" : 11.10,
    "Year":     2023
}

print(x)
x["Year"] = 2020
x["company"] = "Nokia"  # method use to update the given value or change the value
print(x)


y = x.items() # to check the total item in Dictnory
print(y)

print(x)
print(x.items())
x["configuration"] = "500mh"
print(x.items())



