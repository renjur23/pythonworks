# def person(**kwargs):
    
#     print(kwargs.get("name"))
    
#     print(kwargs.get("price"))
    

# person(name="oneplus",price=24000)

def calculator(*args,**kwargs):
    
    if kwargs.get("operation")=="+":
        
        return sum(args)
    
    if kwargs.get("operation")=="*":
        
        result=1
        
        for num in args:
            
            result=result*num
            
        return result
    
            
print(calculator(10,20,30,operation="+"))

print(calculator(10,20,30,operation="*"))


def student_info(*args,**kwargs):
    
    if kwargs.get("operation")=="avg":
        
        avg=sum(args)/len(args)
        
        return avg

    if kwargs.get("operation")=="total":
        
        total=sum(args)
        
        return total
        
        
    
print(student_info(45,34,35,operation="avg"))

print(student_info(45,48,50,operation="total"))