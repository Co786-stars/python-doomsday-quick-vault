"""
In this module we are discussed _________multi leval inheritance_____________How we use this____________________
Inheritance : - 
Multi level Inheritance ✅
syntax : -
class A:
    # attributes of class A
class B(A):
    # attributes of class B
    # access attributes of A
class C(B):
    # attribute of class C
    # access attributes of A and B
"""
# What is multi leval inheritance ?
# Multi-Level Inheritance is an object-oriented programming inheritance model where a derived class inherits from
# another derived class, creating a hierarchical chain of inheritance with three or more levels of classes in a linear,
# sequential manner.

# In simple way : -
# A class is derived from another derived class, and this chain of inheritance keeps continuing.


# Visualization of Chain structure Multi leval Inheritance : -
# Parent Class_1
#       |
#       +------→ Parent Class_2 (inherits from Class_1)
#                     |
#                     +------→ Parent Class_3 (inherits from Class_2)
#                                   |
#                                   +------→ Parent Class_4 (inherits from Class_3)
# First class has original properties → passed to Second → then Third gets (First + Second properties) →
# finally Fourth gets (First + Second + Third properties).
# •→ Class 1 = own
# •→ Class 2 = Class 1 + own
# •→ Class 3 = Class 1 + Class 2 + own
# •→ Class 4 = Class 1 + Class 2 + Class 3 + own



# ➡➡➡➡➡➡➡➡➡➡➡➡➡➡  Multi leval Inheritance ➡➡➡➡➡➡➡➡➡➡➡➡➡➡➡
#➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡
class Grandparents:
    """this is grandparents class"""
    def __init__(self, name="grandparents"):
        self.name = name

class Parents(Grandparents):
    """Represents parents with an age attribute."""
    def __init__(self, age=30):
        super().__init__("parents")
        self.age = age

class Child(Parents):
    def __init__(self, occupation="analyst"):
        super().__init__(10)
        self.occupation = occupation

c = Child() # actually name and age is override via parents
print(c.name, c.age, c.occupation) # output : parents,  10, analyst
#➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡ ➡



# CODE/SYNTAX : -
class LibraryItem:
    """Represents a generic library item"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        """Display basic info"""
        return f"Title : {self.title} Author : {self.author}"

class Book(LibraryItem):
    """Represents a book in the library"""
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.generation = genre

    def display_info(self):
        """Display book info"""
        return (f"My book title is {self.title} with {self.generation} "
                f"generation and his author is {self.author}")

class BorrowedBook(Book):
    """Represents a borrowed book"""
    def __init__(self, title, author, genre, borrower_name):
        super().__init__(title, author, genre)
        self.borrower_name = borrower_name

    def display_info(self):
        """Display borrowed book info"""
        return (f"Book {self.generation} generation book title name is {self.title} "
                f"and his author is {self.author} now borrowed via {self.borrower_name}")

try:

    # Creating an object from BorrowBook
    book = BorrowedBook("crash course", "luther", "5th", "Wizard")

    var = book.display_info()
    print(var) # display the single line statement
except ValueError:
    print("Pls enter the correct value")


