"""
1)) How to check existing item in a list using conditional statement

x = ["hindi", "english", "tamil", "german"]

if "tamil" in x:
    print("Yes tamil language in list x ")


if "sanskrit" in x:
    print("Yes sanskrit in list x ")
else:
    print("No sanskrit not in list x ")


 2 )) How to change list item with positive indexing.

y = ["wizard", "hacker", "cybersecurity"]
print(y[0])
print(y)
y[0] = "Happy"
print(y[0])
print(y)
y[1] = "New"
y[2] = "Year"
print(y)

z = [10, 20, 30, 40, 50]
print(z)
z[1:4] = [200, 300, 400]
print(z)

3 )) How change item with negative indexing

List1 = ["apple", "banana", "guava", "papaya"]
print(List1)
List1[-4] = "pineapple"
print(List1)

List1[-3:] = ["muskmelon", "watermelon", "cucumber"]
print(List1)



4)) append() : It is a predefine function that use to add element or item at the end of list

list2 = [10, 20, 30, 40]
print(list2)
list2.append(50)
print(list2)

list3 = []
print(list3)
list3.append("laptop")
list3.append("computer")
list3.append("mobile")
print(list3)
print(list3[0].upper())

5 )) # insert() : It is a predefine function that use to insert element or item in a list without affecting any existing element .

x = [100, 200, 300 ,400 ,500]
print(x)
x.insert(2, 1000)
x.insert(0, 1000)
print(x)

6)) # extend() : It is predefine function that use to append two list item as single list without affecting any other list item .

l1 = [1+9j, 3+2j, 5+5j, 6j, 3+9j]
l2 = [100, 200, 300, 400, 500, 600]

print(l1)
print(l2)
l1.extend(l2)
print(l1)
print(l2)

7 )) # pop() : It is a predefined function that use to remove last item of the list .
x = ["apple", "mango", "banana", "papaya"]
x.pop() # use to remove last item in list
print(x)
x.pop(0)
print(x)


8)) # del : It is a type of keyword that use to delete the list
y = [1, 2, 3, 4, 5]
print(y)
del y # use to delete the list
print(y)


9 )) # remove(..item_name..) : It is a predefined function  that use to remove item or element of the list .
colors = ["red", "blue", "green", "sky"]
print(colors)
colors.remove("sky")
colors.remove(colors[2])
colors.pop()
print(colors)


10)) # clear() : It is predefined function that use to remove all item of the list at a same time ( empty list)
language = ["hindi", "english", "german", "tamil"]
print(language)
language.clear()
print(language)


11 )) #sort() : It is predefined function that use modify or arrange permanently list item in ascending order .
num = [10, 40, 20, 30, 60, 50, 70, 80, 90, 100]
print(num)
num.sort()
print(num)

12 )) #sorted() : It is predefined function that use modify or arrange temporary list item in ascending order .
           # when we use sorted function then there is no effect on original arrangment of  list item .

num1 = ["a", "c", "b", "h", "p", "e", "f"]
print(num1)
print(sorted(num1))  # sorted() use as a argument in print function
print(num1)


13 )) # reverse() : It is a predefined function that use reverse the item of the list .
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
x.reverse()
print(x)

y = ["basketball", "football", "vollyball"]
print(y)
y.reverse()
print(y)


14 )) # copy() : It is the type of predefined function that use to copy the list and assign in other variable
x = ["camera", "keyboad", "enter_button", "num_paid"]
y = x
print(y)
z = y.copy()
print(z)

15 )) # index() :  It is a predefined function that use to out  index value of list item and always carry single arugment
number = [10, 20, 30, 40, 50, 60, 70, 80]
print(number)
print(number.index(50))
print(number.index(80))

z = number.index(30)
print(z)


16)) # min() : It is a predefined function that use to find minimum value in list
17)) # max() : It is a predefined function that use to find maximum value in list

x = [10, 20, 30, 40, 50, 60]
print(min(x))
print(max(x))

18)) # list() : It is the type of function that use to create list.  for creating the list we use small bracket
z = list((10, "wizard", 1+2j, 2.9))
print(z)
print(list(( 1, 2, 3, 4, 5, 6)))

"""


