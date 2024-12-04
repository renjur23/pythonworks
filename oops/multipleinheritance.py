class Person:
    
    def __init__(self,name,age):
        
        self.name=name
        
        self.age=age
        
    def person_info(self):
        
       print(self.name,self.age)
    
class Employee:
    
    def __init__(self,emp_id,salary):
        
        self.emp_id=emp_id
        
        self.salary=salary
        
    def employee_info(self):
        
        print(self.emp_id,self.salary)
    
class Manager(Person,Employee):
    
    def __init__(self,name,age,emp_id,salary,department):
        
        Person.__init__(self,name,age)
        
        Employee.__init__(self,emp_id,salary)
        
        self.department=department
        
    def display_manager_info(self):
        
         self.person_info()
         
         self.employee_info
         
         print(self.department)
         
         
manager_instance=Manager("hari",28,"emp01",25000,"HR")

manager_instance.display_manager_info()