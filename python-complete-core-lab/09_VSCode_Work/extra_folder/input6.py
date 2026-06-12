# list of fruits 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1) # simple method to print list item s a list 

list2 = [10, 20, 10, 30, 10, 50]
print(list2) # list are ordered and allow duplicate value
print("length list1", len(list1), "length list2", len(list2)) # USE TO FIND LENGTH USING len()

#datatype in list 
d1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
d2 = ["string1", "string2", "string3"]
d3 = [1+2j, 39+3j, 5j, -1j+6, 31+31j, 7j]
d4 = [2.3, 0.4, 1.9, 6.8, 5.3, 3.9, 4.0]
d5 = [[1,2,3,4,5], [5, 4, 6], [1,2,3,9]]
d6 = [{1,2,3,4}, {"a", "d", "g"}, {"3h"}]
d7 = [(1,2,3,4,5), (5,4,3,2,1), (10, 90)]
d8 = [True, False, True, False]

print(type(d1))  # type() function is use to define the type of data value 
print(type(d1[0])) 
# print(type(d6[1][0]))  error generate because tuple does not work on index value 
print(type(d5[0][0]))

print(list(d1))  # create list using list function 
print(list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))) 

# accessing of list 

print(d1[1])  # 20
print(d1[0])  # 10
print(d1[-1]) # 90
print(d1[-2]) # 80
print(d1[1:6])# [20, 30, 40, 50, 60]
print(d1[-8:-3])# [20, 30, 40, 50, 60]
print(d3[:5])
print(d3[3:])
print(d3[-3:]) 

# with loop check item in list or not 
if 30 in list2:
    print(f"yes the {list2[-3]} in list")
else:
    print(f"sorry {list2[-3]} not in list")

if 3+3j in d3:
    print(f"yes {d3[-5]} is in list")
else:
    print(f"{d3[-5]} Not abliable in list ")

x  = [1, 2, 3]
x[0], x[1], x[2] = 10, 20, 30  # change item of the list 
print(x)
x[0:4] = [5, 6, 7, 8]   # change multipal item of the list 
print(x)


list3 = ["str1", "str2", "str3", "str4", "str5"]
# print(list3.insert(3, "string")) output is none datatype 
list3.insert(2, "string")
print(list3) # use to insert the new item without arffecting other item of the list 


list4 = [10, 30, 50, 70, 90]
list4.append(10)  # append is use to add the element at the end of the list 
print(list4)
# print(list4.append(60)) none datatype occure 
list4.append(60)
print(list4)

l1 = ["apple", "banana", "papaya"]
l2 = ["Negligent", "laperwaha", "careless"]
print(l1.extend(l2)) # none data type occure 
l1.extend(l2)
print(l1) 



# remove list items 

x  = ["modest", "humble", "custom", "habit"]
y  = ["stigma", "stain", "reside", "dwell"]

x.extend(y)
print(x)
x.append("dupe")
print(x) 

x.remove("humble")  # remove function is use to remove excatly one argument 
print(x)
x.remove("custom") 
print(x) 

x  = ["convetous", "Greedy", "abide", "endure"]
y  = ["rake", "scoundrel", "resolve", "decide"] 
y.extend(x)
print(y)
y.pop() # pop() is use to remove the last item of list 
print(y)
y.pop(0) # we also remove item using pop by  item or index value 
print(y)

del x # del is use to delete the list form its own place . 
print(y)
y.clear() # clear is the type of method that use to clear the list or empty the list .
print(y)

