"""
-------------------- Return value ----------------- Return value --------------------------------
Extra not for Note on youtube  
we return Dictonary in function call and print is use to out the value that assign in store variable
from person_name()

"""

# def format_name(fname, mname='', lname): wrong sequence 
def format_name(fname, lname, mname=''):
    """Use to check the default argument"""

    if mname:
        print(f"{fname} {mname} {lname}")
    else:
        print(f"{fname} {lname}")

format_name(fname="Hacker", mname="@", lname="wizard")
format_name("Hacker", "wizard")


# Return value using Dictonary 

def person_name(f_name, l_name):
    """we use to return the full name of person as a dictonary """
    full_name = {'firstname':f_name, 'lastname':l_name}
    return(full_name)

#calling function
store = person_name('Aditya', 'Raj')
print(store)


# A small change in (Return value using Dictonary)

def full_name(first_name, last_name, age=None):
    """ we use a Default argument """
    name = {'f_name':first_name, 'l_name':last_name, 'current_age':age}
    if age:
        name['current_age'] = age
    return(name)

name_age = full_name("Abhishek", "Sharma")
print(name_age)

name_age = full_name("Abhishek", "Sharma", 22)
print(name_age)