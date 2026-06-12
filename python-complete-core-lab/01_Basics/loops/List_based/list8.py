fruits = ["litchi", "papaya", "mango", "pineapple", "banana"]

for fruit in fruits:
    print(fruit)

# copy_value

fall = fruits[:]
print(fall)
print(fruits)

# copy value
fall.append("apple")
fruits.append("pomegranate")

print(fall)
print(fruits)

