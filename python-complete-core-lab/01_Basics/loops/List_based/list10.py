x = [
    [10, 20, 30, 40], # 0
    [50, 60, 70, 80], # 1
    [90, 10, 15, 18], # 2
]

# print(x[0][2])
# print(x[0][0])

for i  in x:
    print(i)
print("\n")



for i in range(len(x)): # 0 1 2 3
    for j in range(len(x[i])): # 0 1 2 >> 0 1 2 >> 0 1 2 
        print(x[i][j], end= " ")



# k = -1
# for i in x:
#     k += 1
#     if k < len(x):
#         for j in range(len(i)):
#             print(x[k][j], end=" ")






