file = open("testFile.txt", mode = "r")
data = file.readline()
print(data)
file.close()

# or you can use the with open function which is better at exception handling
with open("testFile.txt", mode = "r") as file:
    data = file.readline()
    print(data)