"""
syntax : -
import modulename
import modulename as aliasname
from modulename import functionname
from modulename as aliasname import functionname as aliasname
from modulename import * >>  use to import all function and classes of module
"""

# Built_in Module >> Import function 

x = """check out module1, module2, module3 file in P_FOLDER for more about import module pls""" """>>> Built-in function <<< """
# with open('testing.txt', 'w') as f : # use to write or import text to notepad file 
#     f.write(x)

import math # this is math module use to import mathmatical calculation
# print(math.sqrt(36)) # sqrt use to find squareroot
# print(math.cbrt(216)) # cbrt use to fund cuberoot
# print(float(math.factorial(3))) # factorial use to find factorial

import operator
# operator.add(5, 2) # function is use to add value 
# operator.mul(5, 2) # function is use to multiply two value 
# operator.add(5, 2) # function is use to add value  
# operator.sub(5, 2) # function is use to subtract value 


import os # this is os module use to perform action according to gicen code 
# os.system('notepad.exe') # use to open notepad in means perform I/O function
# os.system('notepad.exe testing.txt') # use to create new notepad file
# os.startfile('testing.txt') # use to open notepad file 
# os.system('start microsoft-edge:') # use to open microsoft edge
# os.system('mspaint.exe') # sue to open ms paint
# os.system('start winword') # use to open microsoft word in system 


import subprocess # this is subprocess powerful module that use to connect i/o of os 
# subprocess.Popen(['notepad.exe', "testing2.txt"]) # use to create new notepad file
# subprocess.Popen(['notepad.exe']) # use to open notepad 
# subprocess.Popen('mspaint.exe') # use to open mspaint



import time # this is time module use to provide time related function to perform task  
# for i in range(10): 
#     print(i, end=" ", flush = False) # flush is False means number is buffring means excute whole output after 2 second
#     time.sleep(2) # sleep time is given 2 secod means each iteration take 2 second for excution if flush is true 


import webbrowser
# url = 'http://www.google.com' # use to open google browser 
# url = 'http://www.microsoft.com' # use to open microsoft browser
# dns = '8.8.8.8' # use to open googel domain name service
# webbrowser.open(url) 
# webbrowser.open('start : microsoft-edge')




import platform # us as a powerful tool for gaining insights into the system environment where a Python program is execute
# print(platform.processor()) # Get the system's processor information
# print(platform.python_version()) # Retrieve the Python version
# print(platform.python_compiler()) # Indicates the compiler used for compiling Python
# print(platform.release()) # Fetch the system's release version
# print(platform.platform()) # Obtain detailed platform information



import json # use for storing and exchanging data.
# print(json.dumps("Hacker wizard")) # json use as a text, written with JavaScript object notation.
# print(json.dumps(50)) # json is predefined package that use in python for work with JSON data
# x = '{"name":"Wizard", "Roll":1002, "semster": "3rd"}'
# y = json.loads(x) 
# print(y['name']) 

"""_____________________________________________pathlib function ______________________________________________________________"""
import pathlib #  path provides an object-oriented interface for working with paths and file
x = pathlib.Path('testing.txt')  # Path is a module that lie in pathlib laibrary 
r = x.read_text() # read_txt function is lie in Path module and use to read the txt file code on output screen  
w = x.write_text("Hello every one my name is aditya") # write_text() is use to write the single line in file means it take single argument
print(pathlib.Path("testing.txt").read_text())  # plathlib libarary /Path module / read_text() we can also use write_text()

# import os
# os.startfile("testing.txt")
# from pathlib import Path
# x = Path("testing.txt")
# y = x.write_text("Hello world")
# print(x.read_text())

"""_____________________________________________Date time module ______________________________________________________________"""


import datetime # use to handle date and time in python
# var = datetime.datetime.now() # use to provide current date > [yy-mm-dd]and time > [h.m.s.ms]
# birthday = datetime.datetime(2002, 2, 3) # use to update datetime 
# print(var.year) # use to display only year 
# print(var.date()) # use to display only date
# print(var.time()) # use to display only hour


from datetime import datetime, timedelta # timedelta and datetime is a function 
# dt = datetime.now()
# nx = timedelta(days=10) # argument is use to provide date manuplation  
# a10x = dt + nx # use to add next ten days in time delta 
# print(dt, nx, a10x) # use to display date and time 
# format = dt.strftime("%Y/%m/%d %H:%M:%S") # use to provide format of datetime
# format = dt.strftime('%d %m %Y %H:%M:%S') 
# print(format) 
 

# import pytz________
# from datetime import datetime___
# utc = datetime.now(pytz.utc)___
# print(utc)______

"""________________________User define functions import in value _____________________________________"""

import secondndimportmodule        # use to import user-defined module secondimportmodule >> module means file 
# secondndimportmodule.rev()  # use to import user-defined function syntax : functionname.import
# secondndimportmodule.srizesum() # use to print the sum of n number of serize


from secondndimportmodule import fibonacci # use to import a  specfic function 
# secondndimportmodule.fibonacci() # use to call function fibonacci syntax : modulename.functionname


"""_______________________Import functions class and methods ___________________________________________"""

import random


from thirdimportmodule import Numbers # use to import class from module thirdimportmodule
# obj = Numbers(30) 
# obj.primenumber() 
