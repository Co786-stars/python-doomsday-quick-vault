companys = ["Del", "Hp", "Lenovo", "Intel", "Logi"]
for company in companys:
    print(company)

friends = ["Jorg", "peter", "donald", "macon"]
for friend in friends:
    x = f"My friend {friend} is not belongs from india "
    print(x)

wizards = ["Kamlesh", "Rohan", "Rocky", "Rajesh", "Raja"]

wizards[0] = wizards[0].upper()
print(wizards)


for wizard in wizards:
    print(f"Hello my friend {wizard.upper()}")
    print(f"I am surprise from your magic trick ")
    print(f"are fine {wizard.upper()} \n")


for i in range(len(wizards)):
    if i <= len(wizards):
        wizards[i] = wizards[i].upper()
    else:
        wizards.clear()
print(wizards)

wizards = [x.lower() for x in wizards]
print(wizards)

#...............Avoding indentation error .....................#


list = [j for j in range(5)]
print(list)

list = ["raju", "Nitesh", "Mangal", "Mukesh"]
#for li in list:
# print(li)  indentation error happend






