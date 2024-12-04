num1=int(input("Enter num1"))

num2=int(input("Enter num2"))

try:
    
    result=num1/num2
    
    print(result)
    
except Exception as e:
    
    print(e)
    
    # if num2==0:
        
    #     num2=int(input("Enter a number greater than 0"))
        
    #     result=num1/num2
    
    #     print(result)
        
finally:
    
    print("Try all ways ")