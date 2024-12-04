employee={"id":100,"name":"ramu","department":"hr","salary":25000}

print(employee["salary"])

product={"id":1,"name":"iphone","price":200000}

print(product["price"])

# update method

product["price"]=150000

print(product["price"])

product["mfg"]="2/10/2024"

print(product)

product["offer"]=10

print(product)

if "offer" in product:
    
    product["offer"]=5
    
else:
    
    product["offer"]=15

print(product)