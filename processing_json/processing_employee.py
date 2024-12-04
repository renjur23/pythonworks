from json import load


f=open("D:\\Pythonworks\\datasets\\employee.json")

data=load(f)

# for emp in data:
    
#     print(emp)

salary=[salary.get("salary")for salary in data]

print(salary)

salary=[salary.get("salary") for salary in data if salary.get("salary")<15000]

max_salary=max(data,key=lambda d:d.get("salary"))

print(max_salary)
