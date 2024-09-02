import random
with open('newfile.txt', 'r') as file:
    print(file.read())
    # print(file.read(20))
    # print(file.readline())
    # print(file.readlines())


# reading files exercise
f =  open('testFile.txt')
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()

print(random.choice(f_content_list))

