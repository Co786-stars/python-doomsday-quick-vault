# center align {:^} with circumfex symbol
# Right align {:>} with Greater then symbol
# left align {:<} with smaller then symbol
#plus indicator {:+} use for integer value
#negative indicator {:-}  use to give negative symbol in negative integer
#negative-_pos+ value {:=} use to give negative symboll as well positive symbol
#Thoustand seprator {:_} and  {:,} us to seprate value on thousand place

"""
1)) center align

print("Hacker @ wizard")
print("Hacker {:^} wizard".format("@"))
print("Hacker {:^4} wizard {:^4}".format("@",151))
print("Hacker {caret:^} wizard".format(caret="@"))
x = "india is very {0:^10} country".format("powerful")
print(x)

2)) Right align

print("hacker {} wizard".format("@"))   # Normal text
print("hacker {:^} wizard".format("@")) # center align
print("hacker {:>} wizard".format("@")) # right align
print("hacker {:>10}  wizard".format("@")) # right align
x =  "Temprature is {:>8} coll".format("very")
print(x)


3)) left align
print("india is {} country ".format("beautiful"))
print("india is {:^15} country ".format("beautiful"))
print("india is {:>15} country ".format("beautiful"))
print("india is {:<15} country ".format("beautiful"))

x = "{key1:>10} is equal to {key2:<10}"
print(x.format(key1=20, key2=20))

4 )) plus indicator

print("Today the maximum Temprature is {}".format(27))
print("Today the maximum Temprature is {:+}".format(27))  # plus indicator format string
x = "Today the day is cold approx {:+} degree".format(20) # plus indicator format string in with variable
print(x)

5)) negative indicator {:-}

print("This is negetavie value {:-}".format(+50))
print("This is negetavie value {:-}".format(-50))
x = "{:-} is smaller then {:-} but {:+} greater the bot number "
print(x.format(-50, 50, 100))

6)) pos+_neg- value
print("{:-} is Equal  to {:-}".format(-10, +10)) # negative align
print("{:+} is Equal to {:+}".format(-10, +10))  # positive align
print("{:=} is greater then {:=}".format(-10, +10)) # neg-_pos+ align

7))  comma and underscore thousand seprator

#using underscore ( seprator )
x = "{:_}"
print(x.format(300000000000))
# using comma ( seprator )
x = "{:,}"
print(x.format(300000000000))

"""