employee={"e_id":10,
          "name":"devi",
          "salary":20000,
          "department":"testing",
          "experience":3}

print(employee)

employee["contact"]=12364789

print(employee)

if employee["experience"]>5:
    
    employee["salary"]+=10000

else:
    
    employee["salary"]+=5000
    
print(employee)