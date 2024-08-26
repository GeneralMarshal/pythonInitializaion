list1 = [1, 2, 3, 4, 5, 6]

# function for adding an item to a list with a given index
list1.insert( len(list1), 7)


# just adds the item to the end of the list
list1.append(8)

# used to extend the list with some values after
list1.extend([9, 10, 11, 12])

print(list1)

list2 = [1, 2, 3, 4, 5, 6]

# used to delete an item while specifying the index in a list
list2.pop(2)
del list2[2]

print(list2)

for x in list2:
    print("value ", x)