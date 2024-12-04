def perfect_num(num):
    
    total=0
    
    for i in range(1,num):
        
        if num%i==0:
            
            total=total+i
            
            
    return(f"{num} is a perfect number" if total==num else f"{num} is not a perfect number")

number=perfect_num(int(input("enter the number : ")))

print(number)