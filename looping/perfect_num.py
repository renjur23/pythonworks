num=int(input("enter the number : "))

total=0

for i in range(1,num):
    
    if num%i==0:
        
        total=total+i   
        
        
print(f"{num} is a perfect number") if total==num else print(f"{num} is not a perfect number")

