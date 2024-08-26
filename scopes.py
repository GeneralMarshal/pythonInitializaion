global_val = 10

def scopes():
    enclosed_val = 2
    def enclosed():
        print("my enclosed value is ", enclosed_val)
    enclosed()

scopes()