x = ((1, 2), (3, 4), (5, 6), (7, 8))

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=" ")

y  = set(x for x in x)
y = tuple(x for x , i in x)
print(y)
y = tuple(x for x , x in x)
print(y) 


