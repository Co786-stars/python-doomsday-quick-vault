"""
# How to create set() datatype
x = {}  # empty set
y = set()
print(x)  # { no item exist so this is empty set}
print(y)  # set()
z = {10, 20, 30, 40, 50} # unindexed, unindexable
# list = [10, 20, 30, 40, 50] # indexe besed
print(z)  # {50, 30, 10, 20, 40}, {40, 30, 20, 10, 50}
# print(list)  # [10, 20, 30, 40, 50]

p = set("hacker")  # constructor is use to convert any datatype in set
p = set(10) # if we pass numeric value as a single argument from set constructor then error are happen
("hacker", "wizard", "@")
["hacker", "wizard", "@"]
p = set("hacker", "wizard", "@") >> error generate
p = set(("hacker", "wizard", "@")) >>  output as it is but elements place no fixed
p = set(["hacker", "wizard", "@"]) >>  output as it is but elements place no fixed
print(p)  # {'wizard', '@', 'hacker'}
print(p)  # {'h', 'c', 'a', 'k', 'e', 'r'} # unindexed format thats it is not in sequence

q = {10}
q = {"hacker"}
q = set("hacker")
print(q)

# How to access set items

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
z = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# print(x[0], x[5:9])  # 10 [60, 70, 80, 90]
# print(y[0], y[5:9])  # 10 (60, 70, 80, 90)
# print(z[0], z[5:9])  # Type error >> because set items are not depens upon index number >> unindexed

# list index based/ element based
for i in range(len(x)):  # i = 0, 1 , 2, 3 , 4.....9
    print(x[i], end= " ") # >>  10 20 30 40 50 60 70 80 90 100
print()

for i in x:  # i = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(i, end=" ") #  10 20 30 40 50 60 70 80 90 100
print()

# tuple index based/ element based
for j in range(len(y)):  # j = 0, 1 , 2, 3 , 4.....9
    print(x[j], end= " ") # >>  10 20 30 40 50 60 70 80 90 100
print()

for j in y:  # j = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    print(j, end=" ") #  10 20 30 40 50 60 70 80 90 100

# set index based/ element based
for k in range(len(z)): # k =  0
    print(z[k])   # Type error

print()
z = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
for k in z:  # k = 10  20 30 40 50 60 70.. 100
    print(k, end=' ') # 10 20 30 40 50 60 70 80 ... 100

"""



