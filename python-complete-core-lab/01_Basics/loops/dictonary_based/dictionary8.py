profile_items = {
    "Fruits" : {
        "mango"  : "Yellow",
        "Banana" :"green",
        "Apple"  : "white",
    },
    "language": {
        "C"   : 1972,
        "C++" : 1983,
        "Python" : 1991,
        "Java" : 1995,
    },
    "Skills": {
        "Medical"   : "NEET",
        "COMP-S"    : "B-TEC",
        "CS"        : "M-COM",
        "C-Service" : ""
    },
    "jobs": {
        "Python_Developer" : "Programmer",
        "Java_Developer"   : "Java",
        "PHP_Developer"    : "PHP",
        "JScript_Developer": "JS"
    }
}

print(profile_items)
print(profile_items["jobs"])

for access , value in profile_items.items():
    print(f"Key {access} \n value : {value}")


