x  = {"throttle", "smother", "gag"}
y  ={"tirade", "invective", "diatribe"}
z = x.union(y)
print(z)

a = {"xnophobic", "yank", "zany", "vitiate"}
b = {"chuvinisam", "jingoism", "Animosity","yank"}
z = a.intersection(b)
print(z)

c = {"virulent", "venimous", "Fatal", "Malicious","spoil", "spoil"}
d = {"vitiate", "spoil", "anihilate","spoil","venimous"}
z = c.difference(d) # it use to keep the item of first that is not in other set 
print(z)

z = x.symmetric_difference(d)
print(z)
