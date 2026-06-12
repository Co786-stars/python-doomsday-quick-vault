x = {
    "Name" : "Wizard",
    "Roll" : 1234567,

    "y" : {
        "Fruit" : "Orange",
        "color" : "Red",
        "Cost"  : 5
    }
}
w = {
   "College" : "Arcade",
    "Roll"   : 22003344
}
z = {
    "copy" : "Python",
    "book" : "python",
    "Roll" : 2345456
}
total_dict = {
    "z" : z,
    "w" : w,
    "x" : x

}
print(total_dict)
print(total_dict["z"]["copy"])
print(total_dict["w"]["Roll"])
print(x["Name"])
print(x["y"])
print(x["y"]["color"])

