x = {"apple", "fruit", "banana", "cherry"}
for i in x:
    print(i)


#--------------------------------------------------------------------#

y = {"aditya", "rohan", "mohan", "sohan"}
if "rohan" in y:
    print("yes rohan in y set datatype")
else:
    print("Rohan is not in y datatype")


#--------------------------------------------------------------------#
#  set item access by using wile loop
# z = {} error occur attribute error
z = set()
p = int(input("Enter the total number of item in set : "))
for i in range(p):
    sto = input("Enter your value of set : ")
    z.add(sto)
print(z)

# output >> 4 >> 0  1  2  3
# output >> wizard , 29+28j , 1250 , True
# foutput>> {'wizard', 29+28j, 1250,True }

#---------------------------------------------------------------------#

p = x.union(y, z)
print(p)

