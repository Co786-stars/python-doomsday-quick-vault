"""
Topic of file handling : -
1) Creating a File
2) Writing to a File
3) Opening a File
4) Reading from a File
5) Handling Exceptions 
6) Using with Statement 
7) storing Data using JSON (read about it)
7) File Methods

-------------------------------NOW--------------
File handling in Python is a important parts of  programming languange that allows you to work with files for 
reading, writing, and manipulating data.
"""


# Creating a Files
"""
from os import system
system('notepad.exe myfie.txt')  # using this statment we create first notepad file.
"""



# Writing to a file
"""
from pathlib import Path
x = Path("myfile.txt")
x.write_text("This is notepad use to write the text ") # write_txt() function is use to write anythings in file  
# print(x.read_text()) # read_tex() function is sue to read the text that written in file on output screen

y = "My name is saurab rajput"
with open('myfile.txt', 'w') as f:      # open() function is use to take two argument first filename and second flag or format
    f.write(y)  # function is use to write the text in files if we want to see then we use os module and open the notepad 

# import subprocess, os 
# os.system("myfile.txt") 
# subprocess.Popen(["notepad.exe"])
"""


# Opening a file
"""
import os 
os.system("myfile.txt")
"""


# Reading from a file 
"""
str  = "My name is saurab \n"
str += "I am from patna bihar\n"
str += "I like to play chess and vollyball\n"
str += "I am complete my matriculation from interprastra international school with 72.4% marks \n"
str += "then after i am complete intermidate from B.R ambdhker university with 75.9# marks and also i am complete web devlopement\n"
str += "course from patna and recently i am complete my Bachlor BCA from partliputra university and during my BCA course\n"
str += "I was complete 1 yer deploma in the fields of cybersecurity from craw acadmy Now i am taking about my extra skils"
str += "My typing speed is 65wpm . my favorite computer language is Python and Sql but still i known c, c++, java. i am working good with in Linux and windw os \n"
str += "i am ambidextrous written with both hand. i am able to speak three language hindi, english, german and Tamil, now i thinking which is better to learn \n"
str += "telgu or kanada my weakness is minor spealling mistake in most of the time when i am written manually but i am good in syntax of computer language"

import pathlib
pathlib.Path("myfile.txt").write_text(str)
print(pathlib.Path("myfile.txt").read_text())   # use to read the file 
"""

# Handling Expections
"""
|1| ZeroDivisionError
print(6/0)  # zero devision error are occur when we divide any positive natural number with zero if this type of error are occur then use try-except Block to handle it .
try:   # this method is try-except block to handle zeroDevision error
    print(1/0)
except ZeroDivisionError:
    print("You can't devide by zero")

print("Enter q to exit : ")
while True:
    
    num1 = input("Enter 1st number : ")
    if num1 == "q":
        break
    num2 = input("Enter 2nd number : ")
    if num2 == "q":
        break
    try:
        num3 = int(num1)/int(num2) 
        print(num3)
    except ZeroDivisionError:
        print(f"{num1} is not divisibal by {num2}")

|2| FileNotFoundError
from pathlib import Path
x = Path('xyz.txt')  # if the file is not found then fileNotError is generate
try:
    y = x.read_text(encoding= 'utf-8')
    print(y)
except FileNotFoundError:
    print(f"file {x} is not found ")
"""

