"""
1)) what is real number ?
>> union of rational and irrational number called real number .
>> Rational number : The number in the form of p/q and (q != 0) or (q > 0) for ex  3/4,5/3...etc
>> Irrational number : The number that can not be expressed in the form of ( p/q , p:q ) q!=0 for ex √3 ,√2 ,pi...etc

# float value ( decimal value )
var1 = 99.999
var2 = 99.900
var3 = 99.009
var4 = .99
print(var1 , var2, var3, sep="___")
print(format(var2,"f"))
print(format(var4,"f"))


2))  what is complex number ?
>> The combination of Real number and imaginary number is called complex number .
>> complex is in form of (a+ib) and (a+jb)  for example ( 9i ), (9+9i) for python>> 9j , 9+9j , 9-9j = real= 9 , img=-9 .

# complex number (a +ib) >> programming ( a+jb)
comp1 = 10+5j
comp2 = 15j-10
comp3 = 10j
comp4 = 9j
print(comp1 , comp2, sep="   ")
x = format(comp3,"f")
y= format(comp3,".1f")
print(x)
print(y)

3)) what is integer ?
>> The whole number as well as natural number is called integer .

# integer (negative and positive )
int1 = 1991
int2 = -1991
print(int1)
print(int2)

4)) what is Boolean ?
>> The value or object display only two value ' True '= 'on' = 1 = 'active' and 'False'='off'=0 = 'Inactive'
# boolean (based on True and False value )
bool1 = True
bool2 = False
print(bool1)
print(bool2)
x = "wizard"
print(x.isupper())
print(x.islower())


"""
#01)) format()   it use to give the format of object value using format string value
"""
var1 = 500000
var1 = 50000000.12345
print(format( var1, "_"))
print(format(var1,","))
var2 = "{:_}"
print(var2.format(18000))
# var3 = "hackerwiard"
# print(format(var3, "-"))

"""
#02)) type()     it use to define the property or class of object or value

"""
print(type(0))
print(type(-121321))
print(type(True))
print(type(False))
print(type("Hacker @ wizard"))
print(type([1,2,3,4]))
print(type(["hello", "yellow",23 , 50.5]))
"""


#03)) int()      it use to create or denote int type value and change other object in integer

"""
print(20)
print(int(20))
print(int(20.234))
print(int("hacker @ wizard"))
print(int($))"""


#04)) float()    it use to create or denote float type value and change other object in float

"""
print(40.99)
print(40.0000000000000)
print(format(30, "f"))
print(format(40.0000000000000 , ".13f"))
print(float(88))
print(float(int(88.0)))
print(float("welcome to wizard circus"))
print(float("%"))"""


#05)) complex()  it use to create or denote complex type value and change other object in complex

"""print(2+7j)
print(type(2+7j))
print(complex(10))
print(complex(20+70j))
print(complex(10j))
# print(complex("hacker wizard"))
print(complex(int(80.8)))
print(complex(float(80.0))) # 80+0j
print(complex(float(80.89654))) # 80.89654+0j
print(complex(int(float(int(float(11))))))"""


#06)) bool()     it use to check the value is True or false .

"""print(50>40)
print(10>20)
print(bool(50>20))
print(bool("welcome to this course"))
print(bool(3))
print(bool(60==100))"""


#07)) isupper()  it use to check the given value is in upper or not ( work on boolean value )

"""print("HELOO".isupper())
print("HELOO".islower())
x = "Hacker 2 wizard"
print(x.isupper())
x = 10
print(x.upper())"""


#08)) islower()  it use to check the given value is in lower or not ( work on boolean value )

"""print("welcome to wizard session".islower())
print("welcome to wizard session".isupper())
x = "welcome to Wizard Session"
print(x.islower())
y = 4
print(y.islower())"""


#09)) istitle()  it use to check the given value is in title or not ( work on boolean value )
"""
print("Hacker @ Wizard".istitle())
print("Hacker @ wizard".istitle())
z = 30
print(z.istitle())
print("sdjkbhdfihu sfvskjvbfs sdkbsgdfsdgfkjhidsfu ".istitle())"""


#10)) upper()    it use to change value in upper case ( captial alphabet letter A,B,C...... )

"""print("Hacker @ WIZARD".upper())
x = "india is beautiful country"
print(x.upper())
y = 2+3j
z = 13
print(y.upper() , z.upper())"""


#11)) lower()    it use to change value in lower case ( lower alphabet letter a, b, c...... )
"""print("WIZARD HACKER".lower())
var1 = "THIS  is lower case MeThoD"
print(var1.lower())
int_1 = 78
print(int_1.lower())"""


#12)) title()    it use to change value in title case ( title alphabet letter Ab ,Bc, Cdlkj...... )
"""print("This Is Title Case".title())
print("python is very important for cyberSECurity".title())
x = 5
print(x.title())"""


#13)) len()      it use to find the length of obect or value .
"""
print(len("object"))
x = [10, 20 ,30 , 40 , "Helllo" , 10.10 , 30+40j]
print(len(x))
print(len([20,90]))
# print(len(20))
print(len("Cyberse curity"))
# print(len(complex(90)))
# print(len(20.9))
"""

#14)) casefold()  it use like a lower pre define function ( it use conver to object in lowercase or casefold )

"""x = "Wizard"
print(x.casefold())
x = "CYBERSECURITY COURSE"
print(x.casefold())
x = 9
# print(x.casefold())
"""
