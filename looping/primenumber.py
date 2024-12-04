num=int(input("Enter the number: "))

is_prime=True

for i in range(2,num):
    
    if num%i==0:
        
        is_prime=False
        
        break
        
print(f"{num} is a prime number" if is_prime==True else f"{num} is not a prime number")