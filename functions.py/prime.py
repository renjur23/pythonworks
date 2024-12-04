def prime(num):
    
    is_prime=True
    
    for i in range(2,num):
        
        if num%i==0:
            
            is_prime=False
            
            break
    
    return(f"{num} is a prime number" if is_prime==True else f"{num} is not a prime number")

num=int(input("Enter the number: "))

result=prime(num)

print(result)