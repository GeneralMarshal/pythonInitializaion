employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

# create a function to find an employee by their

def find_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return({
                "id": employee[0],
                "name": employee[1],
                "department": employee[2]
            })
        
print(find_employee(12458))

# instead of having to iterate over all the items in the list you can just use a dictionary data structure

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))