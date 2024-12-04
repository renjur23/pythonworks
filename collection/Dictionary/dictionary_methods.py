# dictionary methods

employee={"id":100,"name":"rathin","department":"developer","age":24,"salary":20000}

# get method

print(employee.get("Name"))

print("test message")

# pop method

employee.pop("salary")

print(employee)

# return all keys

for k in employee.keys():
    
    print(k)
    
# return all values

for v in employee.values():
    
    print(v)
    
# return key and values

for k,v in employee.items():
    
    print(k,v)

