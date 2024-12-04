class Employee:
    
    id:int
    name:str
    salary:int
    age:int
    department:str
    
    def set_employee(self,id,name,salary,age,department):
        
        self.id=id
        self.name=name
        self.salary=salary
        self.age=age
        
        self.department=department
        
    def display_employee(self):
        
        print(self.id,self.name,self.salary,self.age)
        
emp_instance=Employee()

emp_instance.set_employee(100,"Rathin",35000,30,"Developer")

emp_instance.display_employee()

        
