# ------------------------------------Multilevel Inheritance-----------------------------Multilevel Inheritance------------------
# ------------------------------------Multilevel Inheritance-----------------------------Multilevel Inheritance------------------
# ------------------------------------Multilevel Inheritance-----------------------------Multilevel Inheritance------------------


""""
syntax : -

class A:
    # attributes of class A

class B(A):
    # attributes of class B
    # acess attributes of A

class C(B):
    # attribute of class C
    # acess attributes of A and B
"""

class A:
    def __init__(self):
        # Initialize any common attributes here
        pass

class B(A):
    def __init__(self):
        super().__init__()  # Call the constructor of class A
        # Add attributes specific to class B
        pass

class C(B):
    def __init__(self):
        super().__init__()  # Call the constructor of class B
        # Add attributes specific to class C
        pass

# Example usage:
obj_c = C()
# Now obj_c has access to attributes from A, B, and C

