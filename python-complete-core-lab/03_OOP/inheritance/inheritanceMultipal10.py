# ------------------------------------Multipal Inheritance-----------------------------Multipal Inheritance------------------
# ------------------------------------Multipal Inheritance-----------------------------Multipal Inheritance------------------
# ------------------------------------Multipal Inheritance-----------------------------Multipal Inheritance------------------
    #    A       B
    #     \     /
    #      \   /
    #        C


"""
Syntax : -

class A:
    # features of A

class B:
    # features of B

class C(A, B):
    # features of A + B + C
"""


class A:  

    def myfunc(self):   
        return "first method"

class B:

    def myfunc2(self):  
        return "second method"

class C(A, B):   
    # inherit attributes from class A and B 
    def myfunc3(self):  
        return "third method"

obj_c = C()
print(obj_c.myfunc3()) 


