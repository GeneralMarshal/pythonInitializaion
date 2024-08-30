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