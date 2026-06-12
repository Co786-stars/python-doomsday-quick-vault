# - A decorator in Python is simply a function that takes another function as input and
# returns a new function (usually wrapping or modifying behavior).
# - Decorators are used to modify the behavior of a function without changing its source code.
# - They are often used for logging, access control, memoization, and other cross-cut

"""def x(a):
    a()

def fun():
    print("wizard")

obj = x(fun)
"""



def xyz(arg):
    def pqr():
        var = arg()
        print(var)
    return pqr

def abc():
    return f"i have no words to explain any {1} line about u"
xyz(abc)()



# another version : -
def xyz(arg):
    def pqr():
        var = arg(2, 3)
        print(var),
    print("hello")
    return pqr

def abc(a, b):
    return (a+b)
xyz(abc)()  # basic concept first function is execute then the second one is executed
