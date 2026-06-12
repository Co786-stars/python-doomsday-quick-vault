# for loop using in list . 

x = ["modest", "custom", "prolong", "hustle", "solemn", "imply"]

for i in x: # i is a argument that store all value one by one from x list 
    print(i) 

for i in range(len(x)): # store value using len function 
    print(x[i], end="  ")

# while loop using in list 

y = ["Ramble", "Beneficial", "Flare", "Negligent", "Allof"]
print("\n")


i = 0
while i < len(y):
    print(y[i])
    i += 1
print("\n")


z  = ["congregate", "utter", "negligible", "placid", "rake", "dupe"]
[print(x) for x in z]  # loop comprension using shorthand loop in python 


l1 = ["Fetter", "Hamper"]
z  = [x for x in l1]
 

l2 = ["shrewd", "intelligent"]
for i in l2:
    l2.append(l1)





