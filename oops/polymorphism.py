# method overloading

class Operation:
    
    def add(self,num1,num2):
        
        print(num1+num2)
        
    def add(self,num1,num2,num3):
        
        print(num1+num2+num3)
        

obj=Operation()

obj.add(10,12,56)

obj.add(10,25)
        
    