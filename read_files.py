import random
with open('newfile.txt', 'r') as file:
    print(file.read())
    # print(file.read(20))
    # print(file.readline())
    # print(file.readlines())


# reading files exercise
try:
    f_name = input("Type the file name here: ")
    f =  open(f_name)
    f_content = f.read()
    f_content_list = f_content.split("\n")
    f.close()

    print(random.choice(f_content_list))
except Exception as e:
    print("Error ", e)

