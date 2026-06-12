print("hello")

x  = [1,2,3,4,5,6,7,8,9]
for i in x:
    print(i , end="  ")
print("\n")

x1 = [1, 3, 4, 5, 6, 7, 8, 9]
new_x1 = []
for i in x1:
    new_x1.append(i)
print(new_x1)


words = ["flagrant", "mitigate", "sherewed", "intelligent"]
new = [x for x in "flagrant"] # print word as a list 
print(new)

new = [x for x in words if words != "mitigate"]
print(new)

new_word = ["Zany", "Bizzare", "Eccentric", "uncontrolled", "surprising", "mollted"]
x = [x for x in new_word]
print(x)

x = [x for x in range(len(new_word))] # again using range() function 
print(x)
x = [new_word[x].upper() for x in range(len(new_word))] # again using range() function 
print(x)

y = ["familiar", "sensible", "apathy", "Indifferent", "Indifference", "wistful", "Nostalgic", "contemplative"]
x = ["wizard" for x in range(len(y)) if x < 5] 
print(x)


k = ["zest", "enthusiasm", "gutso", "gusto", "eagerness", "energy"]
x = [x if "zest" not in x else "gusto" in x for x in k ]
print(x)
store = [m if "enthusiasm" != m else print("hello") for m in k ]

words = ["scarp", "tiny", "bit", "whit", "lot", "hug", "sufficent"]
words.sort()
print(words)

words.sort(reverse=True) 
print(words)


x = [1, 2, 3, 4, 5, 6]
x.reverse()
print(x)


