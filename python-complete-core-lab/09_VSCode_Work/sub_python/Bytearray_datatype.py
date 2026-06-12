# Empty Bytearray
# bytearray(b'')
var1 = bytearray()
print(var1)

# Int Bytearray
# bytearray(b'\x00\x00\x00')
var2 = bytearray(3)
print(var2)

# list Bytearray
# bytearray(b'\x01\x02\x03\x04\x05')
# bytearray(b'\x06\x07\x08\x09\x10\x13')
var3 = [1, 2, 3, 4, 5]
var4 = [6, 7, 8, 9, 10, 13]
print(bytearray(var3))
print(bytearray(var4))
print("hacker\x09\x09wizard")
print("hacker\t\twizard")
print("\x61, \x62, \x63")

# 1,  2,  3,  4,  5,  6,  7,  8,  9, [10 = A, 11 = B, 12 = C, 13 = D, 14 = E, 15 = F]
# [16 = 10,  17 = 11,  18 = 12 ........ ] A,  B,  C,  D,  E,  F   10 ,  11,  12.....

# string bytearray
var4 = "hacker @ wizard"
print(bytearray(var4, 'utf-8'))
print(bytearray(var4, 'utf-16'))

