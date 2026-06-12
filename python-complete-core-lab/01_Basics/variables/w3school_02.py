x  = {}
# set flag pooling active 
polling = True
while polling:
    name = input("Enter your name : ")
    moun = input("which mountain would you like : ")
    x[name] = moun
    
    repeat = input("Would you like other reperson responce : y/n : ")
    if repeat == 'n':
        polling = False
# final result

for i,j in x.items():
    print(f"{i} whant to climb {j} mountain")


# ........................................other program..............

#  set item access by using wile loop 
var1 = set()
x  = int(input("Enter your Number of item : " ))
i = 0
while i < x:
    inp1 = input("Enter your first item : ")
    var1.add(inp1)
    i += 1
print(var1)

#.................................output  of program..................
#output >> 2 >> 0  1 
#output >> wizard ,hacker
#output >> {wizard, hacker} 


"""# x = {
#     'name': 'aditya',
#     'class': 'Bca',
#     'roll': '20003'
#     }
# for i, y in x:
#     print(f"{x} >> {y}")
"""