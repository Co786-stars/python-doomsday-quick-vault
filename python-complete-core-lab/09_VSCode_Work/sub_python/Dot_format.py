# All about Placeholder
# {} It is a special symbol that is enclosed with brace
# placeholder is used to mark or hold position where we want to insert value into the string
print("Hacker @ Wizard")
print("Hacker {} Wizard")
print("Hacker {} Wizard".format("@"))
print("Today the Date is : {} ".format(3))
print("This is float value :{}".format(13.9))
print("str value {} and int value {}".format("date", 30))
print("Today is my {} . i am {} {}".format("Birthday", "very", "Lucky"))
print("{} is {} then {}".format(20,"greater", 10))
print("{2} is {1} then {0}".format(20,"smaller", 10))
print("India is {value1} as well as {value2} country".format(value1="beautiful", value2="largest"))
print("This is integer value {value}".format(value=20))
print("This is integer value {x} and it is smaller then {y}".format(x=20, y=10))

x = "hello {}"
print(x.format("Pycham"))

y = "This is value {}"
print(y.format(10))

z = "This is float {}"
print(z.format(5.5))

num_var = "number : {0} string : {2} float : {1}"
print(num_var.format(12, 12.5, "Python"))

num_var = "number : {key1} string : {key3} float : {key2}"
print(num_var.format(key1=12, key2=12.5, key3="Python"))