prev=0

current=1

print(prev)

print(current)

for i in range(1,6):
    
    next=prev+current
    
    print(next)
    
    prev=current
    
    current=next


###

num=int(input("enter the number : "))

prev=0

current=1

is_fibonacci=False

for i in range(1,num+1):
    
    next=prev+current
    
    prev=current
    
    current=next
    
   
    
    if next==num:
        
        is_fibonacci=True
        
        break
    
print(is_fibonacci)

