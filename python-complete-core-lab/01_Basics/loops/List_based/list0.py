# short hand if statment
a = 4
b = 5
if a < b: print(f"{a} is greater then {b}")

str_list1 = ["coconut", "almonds", "Raisins"]
list = [x for x in str_list1 if x != "coconut"]
if "almonds" in list and "Raisins" in list: print(f"{list[0]} and {list[1]} is mansion in list items ")


# short hand if else statment

a = "hello"
b = "Yellow"
print(a) if a == "yellow" else print(b)

str_list2 = ["cherry", "pine_apple", "custard_apple"]
copy_str_list2 = [y for y in str_list2]
print(f"Yes {copy_str_list2[2]} given in list") if copy_str_list2[2] == "pine_apple" else print(f"Sorry {copy_str_list2[2]} is not in list")

# ternary operator next time
"""num1 = 10
num2 = 11
print(f"{num1} is smaller then {num2}") if num1 < num2: else
"""




