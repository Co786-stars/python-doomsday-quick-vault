# How to access the dictionary in python with for loop

body = {

    "leg" : {
        "Left"  : "90 degree",
        "Right" : "90 degree",
        "Both"  : "90 degree"
    },

    "chest" : {
        "position": "flat",
        "blood_c" : "bottom",
        "direction": "downward"
    }
}

print("\n")

for x in body.values() :
    print(x)
print("\n")


for x in body.items(): # by this process the whole of body is store in x
    print(x)
print("\n")

print("********************************************************")

for x,y in body.items():
    print(x)
    for z in y:
        print(">>>>", y[z])










