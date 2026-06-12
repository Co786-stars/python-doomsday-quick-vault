x = (1,2,3)
(aditya, rohan, mohan) = x
print(aditya) 
print(rohan)
print(mohan)

# Unpack tuple
wizard = ("ram", "shyam", "suresh", "Dhaniya", "sohan", "rohan")
(rajesh, mahesh , *suresh , mohan) = wizard
print(suresh)


print(type(rajesh))
print(type(mohan))
print(mohan[0])

x = (1, 2, 3, 4)
(p , *q, r) = x
print(q)

#Output : --
# 1 
# 2 
# 3 

# ['suresh', 'Dhaniya', 'sohan']

'<class str>'
'<class str>'

# r
# [2, 3]