
def sumOf(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        sum += v
    return (round(sum, 2))

print(sumOf(cake=33.7, coffee = 2.9, juice = 23.3))