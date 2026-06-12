import textwrap as warptxt


class MyIntroduction:

    def __init__(self):
        """try to display the own introduction"""
        text = ("Thanks to give me opportunity to introduce express my words"
                "First of all i am start with my good name "
                "My name is Aditya raj."
                "I am twenty one year old."
                "I like to play Chess as indoor and volleyball as outdoor game."
                "My Favorites programming language is Python and Database language is SQL"
                "and Time to time i will enhance knowledge itself in other computer language also."
                "I am able to speak, read or write Hindi frequently, english proficiency is intermediate "
                "and currently working on german."
                "My hometown is Bihar belongs to vaishali district, commonly known as city of knowledge."
                "My current location in Noida sector 62 near in Uttar pradesh"
                
                "Now i am taking about my educational Qualifications : - "
                "I am pursuing Mca from jain university bengaluru with data analyst specialization."
                "Before that i was complete my Bachelor's eduction in computer science engineering from Arcade"
                " business college affiliated through Patliputra university "
                "I was complete intermediate from R.N college affiliated through Baba Sahib B.R ambedkar university located in Muzaffarpur"
                "before that i was complete matriculation from Indraprastha international school located in Muzaffarpur"
                "Now i am taking about my external certification's and Qualification")
        # warp = warptxt.fill(text, width=40)
        # print(text.strip())
        print(text)
# obj = MyIntroduction()

class X(MyIntroduction):

    def hello(self):
        print("hello")

obj1 = X()  # if we create object of Child class then __init__ is auto initialize from parents class.
obj1.hello() # But when we access the method using object from child class then in those case __init__ is not initialize

# print("Helllo")