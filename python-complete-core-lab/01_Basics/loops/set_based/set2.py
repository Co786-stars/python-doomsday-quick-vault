x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x.remove(9)
x.remove(4)
print(x)
x.discard(1)

x.discard(9) # in the case of discard we dont see error when item is not exist
# x.remove(9) # in the case of remove we see error when item is not exist
print(x)


x = {"hello", "hii", "whatsup"}
x.pop()
print(x)

x.clear()
print(x)

del x # is deleted now so when we print then we get name error  
# print(x)

