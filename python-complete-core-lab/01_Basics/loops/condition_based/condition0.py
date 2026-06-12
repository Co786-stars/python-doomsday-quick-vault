fruits = ["banana", "apple", "orange", "mango"]
for fruit in fruits:
    if fruit == "banana":
        print(fruit.upper())
    else:
        print(fruit.title())

y =[]
for t1 in fruits:
    if t1 == "banana":
        y.append(t1.title())
    else:
        y.append(t1.upper())
print(y)

min_age = 18
max_age = 45
if (min_age >= 18) and (max_age <= 45):
    print("You are able to give vote")
else:
    print("you are not eligible for vote")
#________________________________________________________________________________

pizza_name = ["onion", "mashroom", "chicken", "pineapple"]
fav_pizza = "chicken"
if fav_pizza in pizza_name:
    print(f"This is your {fav_pizza} pizza")
else:
    print("where is my pizza")

fruits = "apple"
print("is fruits == 'apple' ?") # i am predict False
print(fruits == "apple") # True
print(fruits == "audi")

x = 10
y = 20
for z in range(5):
    if x == 10:
        print("True")
    if (y == 20):
        print("False")
x = ["Coconut", 1991, ]
if "Coconut" in x:
    print("Yes")
else:
    print("No")

if "wizard" not in x:
    print("Yes")

if "Cocont" == "coconut":
    print("ji")
else:
    print("ni")

x[0].lower()
if "coconut".lower() == "coconut":
    print("Lowercase")

num1 =100
num2 =500
if num1 > num2:
    print(f"{num1} greater {num2}")
if num1 ==  num2:
    print(f"{num1} Equal {num2}")
if num1 < num2:
    print(f"{num1} smaller {num2}")
if num1 != num2:
    print(f"{num1} not equal to {num2}")

