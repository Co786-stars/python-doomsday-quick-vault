import Class20_Inheritance as x # pls checkout module 20 for more detail concept 

class Book:

    def __init__(self, name, price):
        self.bookname = name
        self.bookprice = price

    def programming():
        _list = []
        for i in range(True):
            book = str(input("Enter the book name : "))
            pice = int(input("Enter price of book : "))
            if i == "q":
                break
        print(_list)
    
    def storywritten():
        _set = list()  # assign list in in set variable 
        for i in range(True):
            if i == "q":
                i = False
            bok = str(input("Enter the name of book : "))
            price = int(input("Enter price of book : "))
        print(list(_set)) #  loop is use because list are immutable 

class Notes(Book):
    
    def programming():   # programming method is a corrosponding method so it (child method) overid the parents method >> go module 20
        print("Enter your notes below : - \n")
        mynotes = str(input())
        x = mynotes.split(' ')
        ''.join(x)   # method in Python is a string method that takes all items in an iterable and joins them into one string >> module 20 for  
        for i in x:  # for more concept 
            captal = i.capitalize()
            print(captal, end=" ")
        
        print()

obj = Notes
obj.programming()

        