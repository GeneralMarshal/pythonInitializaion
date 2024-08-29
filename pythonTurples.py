# the key difference between list and turples is that turple values are immutable

myTurple = (1, "strings", 4.5, True, "strings")
# note that you can also declare a turple without the parenthesis

print(myTurple[2])

# to find the number of times a specific item appears in a turple
print(myTurple.count("strings"))

# to find the index of a particular item on the turple
print(myTurple.index("strings"))