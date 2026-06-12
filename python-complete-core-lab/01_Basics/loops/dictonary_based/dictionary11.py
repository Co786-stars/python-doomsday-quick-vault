proper_Dict = {
    "fruits" : {
        "name": "orange",
        "color": "Red",
        "mineral": "potash"
    },

    "vegetable": {
        "name":"cucumber",
        "color":"Green",
        "mineral":"none"
    }
}


for x , y in proper_Dict.items():
    print(x)
    for z in y:
        print(" >>> ", y[z])



