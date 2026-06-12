# How to change and update Dictionary item in the list .
x = dict(Name = "wizard", Class = "BCA", Roll = 22003 )
print(x.items())
y = x["Section"] = "A"
print(x)

x["Section"] = "B"
print(x)


x.update({"Roll" : 21110})
print(x)

x.update({"Name" : "Aditya"})
print(x)


