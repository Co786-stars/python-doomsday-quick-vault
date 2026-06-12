"""
1) enumerate()
# enumerate() function is use to add counter an iterable and return enumerate object
x = {10, 20, 30}
y = {40, 50, 60}
for i, j in enumerate(x, start=5):
    print(i, j)
# (0 10)  >> 1 10
# (1 20)  >> 2 20
# (2 30)  >> 3 30

# 2) max() and min()
# max function is use to find maximum value in datatype
# min function is use to find minimum value
x = {10, 20, 30, 50}
y = {40, 50, 60}
print(min(x))  # 10
print(max(y))  # 60

# 3) frozenset()
x = {40, 50, 60}
x.add(70)
print(x)  # {40, 50, 60, 70} # we modify it when we use set datatype
# frozenset() : It is a pre-defined function that use to create immutable set datatype
# to use frozenset() we use use frozenset()
x = frozenset([10, 20, 30])
# x.add(40)  # attribute Error are generate because we never modify when set is in the from frozenset() datatype
print(x)  # frozenset({10, 20, 30})

# 4) sorted()
x = {10, 20, 50, 60, 40, 30}
print(set(sorted(x)))

"""


