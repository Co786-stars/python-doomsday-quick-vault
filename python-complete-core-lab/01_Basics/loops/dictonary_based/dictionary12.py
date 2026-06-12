x  = {
    "y" : {
    "Name": "Aditya",
    "Class" : "BCA",
    "Roll" : 12345
    },

    "z" : {
        "Fruits": "Apple",
        "Veg" : "Cucumber",
        "Flow" : "Lotus"
    }
}

for i in x:   # for is use to pull the value x dict in i that is y and z
    print(i)

# Output : --
# y
# z


print("\n")
for j, k in x.items():   # In this loop x.items() is use to pass the key and value(as a set)
    print("key : ", j)   # for loop pull the key in j and value in k then print is use to out the key
    print("\t\tValue : " , k) # and in this line print is use to out the value (as a set)



for l , m  in x.items(): #  pass the key value  in l and m
    print(l)            # use to out the value of l that is key
    for n in m:         # value of m (as a set) pass one by one as a key in n
        print("\t\t", n)  # us to print the value of n that is key of dict


for l , m  in x.items(): #  pass the key value  in l and m
    print(l)            # use to out the value of l that is key
    for n in m:         # value of m (as a set) pass one by one as a key in n
        print("\t\t", m[n])  # us to print the value of n that is value of key in dict


