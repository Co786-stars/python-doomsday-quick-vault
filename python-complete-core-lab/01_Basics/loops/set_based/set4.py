
# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< update and union function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# y = {10, 20, 30, 40, 50, 60, 70, 80, 90}

# union = x.union(y)
# print(union)
# x.update(y)
# print(x)

# set1 = {10, 11, 12, 13, 14, 15}
# set2 = {16, 17, 18, 19, 20}

# set1.update(set2)
# print(set1)

# # union symbol
# set3 = set1 | (set2)
# print(set1)

# # union between tuple set and tuple
# se_tup1 = {1, 2, 3, 4} # it does not contain duplicate value
# se_tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # it passes some duplicate value in that all ready exist in se_tup1
# unicon = se_tup1.union(se_tup2)
# print(unicon)

# # multiple set joint with union function

# x = {1,2,3,4,5}
# y = {'a', "b",'c'}
# z = {2+2j, 3+3j, 4+4j, 5+5j}
# set = x.union(y, z, unicon)
# x.update(y, z)
# print(set)
# print(x)

# # >> in simple way
# x = {1, 2, 3}
# y = {4, 5, 6}
# z = {7, 8, 9}
# e = ('a' "b")
# # x.update(y,z,e)
# multi_joint = x.union(y, z, e)
# print(multi_joint)

# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< intersection and intersection function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # symbols of union and intersection are only allow to join set to set not valid for set to tuple
# x = {"prakash", "vikash", "sanjay"} # it only allow duplicate value which is available in x and y both
# y = {"vikash", "sanjay", "aditya"}
# inter = x.intersection(y)   # it is use for intersection
# amper = (x)&(y)             # it  is also use for intersection
# print(inter)
# print(amper)

# x = {1,2,3,4,5,6,7}
# y = {1,2,3,9,8,10.11}
# x.intersection_update(y)
# print(x)

# x = {1,2,3, False}
# y = {0,2,True}
# z = (x)&(y)
# print(z)

# y = {0, 1}
# x = {True, False} # output 0 and 1 because interpreter read 0 = true and 1 = false
# z = (x)&(y)
# print(z)


# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Difference or symmetric_difference >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# z  = {"chandan", "rohan", "rohit"}
# y =  {"rahul", "mangal", "mohan", "rohan"}
# x  = z.difference(y)
# print(x)

# P = x-y
# print(P)

# # f = z.difference_update(y)
# z.difference_update(y) # output None
# print(z)


# set1 = {"a", "b", "c", "d", "e"}
# set2 = {"b", "a", "f", "g", "h"}
# x = set1.symmetric_difference(set2) #Symmetric_difference
# y = (set1) ^ (set2) # Symmetric_difference symbol
# print(x)
# print(y)

# # same work like symmetric_difference but after using it the value of prefix set is permanently change
# set1.symmetric_difference_update(set2)
# print(set1)

set1 = set("123", "456", "789", '1011')
print(set1)