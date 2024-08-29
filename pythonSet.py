# sets are like lists but they don't allow duplicate values && sets is not a sequence

setA = {1,2,3,4}

# used for adding items (not duplicate) to sets
setA.add(5)

# used for removing specific values from a set
setA.remove(2)

print(setA)

setB = {1, 3, 4, 5, 7}
setC = {2, 3, 4, 8, 9}

# used for carrying out mathematical operations
print(setB.union(setC)) # can also be represented using the or symbol |
print(setB.intersection(setC)) # can also be represented using the and symbol $$
print(setB.difference(setC)) # can also be represented using the minus symbol -
print(setB.symmetric_difference(setC)) # can also be represented by ^

