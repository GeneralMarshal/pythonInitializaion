menu = ["espresso","mocha","latte","cappuccino","cortado", "americano"]

def findCoffee(coffee):
    if coffee[0] == "c":
        return coffee
    
for x in map(findCoffee, menu):
    print(x)

    
for x in filter(findCoffee, menu):
    print(x)
