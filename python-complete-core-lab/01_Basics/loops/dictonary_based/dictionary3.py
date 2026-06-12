x = {
    "BOOK": "Hindi",
    "COPY": "ENGLISH",
    "EXAM": "COMPUTER"
}

y = x.items()
print(y)

x["DATE"] = "03-01-2022"
print(y)

if "COPY" in x:
    print("yes copy is in x")
elif "EXAM" in x:
    print("yes english is in x ")
else:
    print("it is not in x")
