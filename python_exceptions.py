def divider(a, b):
    return a/b

try:
    print(divider(12,0))
# except:
#     print("something went wrong")
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")


# exercises using exceptions
  # excercise 1
items = [1,2,3,4,5]

try:
    item = items[6]
    print(item)
except Exception as e:
    print("error - ", e, "\nItem does not exist on the list")

    # excercise 2
def divide_by(a, b):
    return a / b
try:
    print(divide_by(40))
except ZeroDivisionError as e:
    print(0)
except Exception as e:
    print("error - ", e, "\nsomething went wrong")

    # excercise 3
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("the file could not be found")


