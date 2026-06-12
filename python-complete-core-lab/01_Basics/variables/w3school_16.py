"""
---------------------------------- styling function using def keyword ----------------------------------

"""

def function_name(parameter_1, parameter_2=" "):
    """ This is dos string always give parameter in lowercase """
    x  = parameter_1+parameter_2
    return x

store = function_name(2, 3)
print(store)



def function_name2(
        parameter_1, parameter_2, parameter_3,
        parameter_4, parameter5, parameter_6 ):
    """ This is dos string multipal parameter we write like this """
    x = parameter5+parameter_1+parameter_3+parameter_4+parameter_2+parameter_6
    return x 
Z  = function_name2(4, 5, 9, 3, 4, 5)   
print(Z)
