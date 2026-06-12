#Adding Dictionary Items
DICT = {
    "NUM1" : 1,
    "NUM2" : 2,
    "NUM3" : 3,
    "NUM4" : 4,
}

DICT["NUM0"] = 0
print(DICT)

DICT.update({"NUM1": 2})
DICT.update({"NUM2": 3})
print(DICT)

# Remove iteam from dictionary
DICT.pop("NUM1") # Use to remove the iteam of the dictonary
print(DICT)

DICT.popitem() # Delete or remove the last item of the dictionary
print(DICT)

del DICT
# print(DICT) Error is generate because there is no DICT are available now its a delete with del keywords


le = dict(course = "CS" , fee = 5000, Date = "03-01-2005")
print(le)
le.clear()
print(le)


le["hello"] = "Wizard"
print(le)

