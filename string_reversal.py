# slice function str[start:stop:step]

trial = "reversal"
newTrial = trial[::-1]

print(newTrial)

# recurssion
def reverseString(str):
    if len(str) == 0:
        return str
    else:
        return reverseString(str[1:]) + str[0]
    
print(reverseString(trial))

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1) + Fibonacci(idx-2)
print(Fibonacci(8))