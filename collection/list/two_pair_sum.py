num=[2,3,4,5,6]

sum=int(input("Enter the sum = "))

left=0

right=len(num)-1

count=0

while(left<right):
    
    current_sum=num[left]+num[right]
    
    if current_sum==sum:
        
        print(num[left],num[right])
        
        # break
        
        left+=1
        
        right-=1
    
    elif current_sum > sum:
        
        right-=1
        
    elif current_sum < sum:
        
        left+=1
        
    count+=1
    
print(count)
        
        