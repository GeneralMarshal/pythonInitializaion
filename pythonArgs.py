# instead of having to pass variables you can just use args
def sumOf(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sumOf(1, 2, 3))