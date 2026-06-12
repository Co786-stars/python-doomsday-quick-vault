# 1)) with the help of UNICODE
# 2)) with the help of CLDR NAME
# 3)) with the help of emoji libary

# With the help of UNICODE
x = "\U0001F49D"
print(x)

# With the help of CLDR ( comman Local Data Respository)
# print("\N {name of emoji}")
print("\N{heart with ribbon}")
print("\N{broken heart}")
x = "\N{blue heart}"
y = "\N{yellow heart}"
z = "\N{sparkling heart}"
p = "\N{purple heart}"
print(x, y, z , p)

# With the help of emoji libary
import emoji
print(emoji.emojize(":grinning_face_with_big_eyes:"))
x = emoji.emojize(":grinning_face_with_big_eyes:")
print(x)

