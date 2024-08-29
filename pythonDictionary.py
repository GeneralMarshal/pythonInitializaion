# does not allow duplicate keys, overwrites it instead

myD = {
    1: "Test",
    "Name":"Jim"
}

print(myD[1])

for key, value in myD.items():
    print(value + str(key))