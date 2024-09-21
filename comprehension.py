data = [2,3,5,7,9,11,13,15,17,19,23,29,31]

# list comprehension
data = [x+3 for x in data]
print(data)

new_data = [x*2 for x in data]
print(new_data)

fourx = [x for x in new_data if x%4 == 0]
print("divisible by four", fourx)

four_minus_onex = [x-1 for x in new_data if x%4 == 0 ]
print("divisible by four minus one", four_minus_onex)

nines = [x for x in range(100) if x%9 == 0]
print("divisible by 9", nines)

# dictionary comprehension
# note the zip function joins two lists to froma dictionary

# dict = { key:value for key, value in <sequence> if <condition> } 
using_range = { x:x*2 for x in range(10) }
print(using_range)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

one_input_dic = {x:x**2 for x in number}
print(one_input_dic)

months_dic = {key:value for (key,value) in zip(number,months)}
print(months_dic)

# set comprehension
set_a = {x for x in range(10,20) if x not in [12,17,19]}
print(set_a)

# generator comprehension
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for x in gen_obj:
    print(x, end=" ")