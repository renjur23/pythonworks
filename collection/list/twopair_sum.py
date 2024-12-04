num=[2,3,4,5]

sum=7

for i in range(0,len(num)-1):
    
    for j in range(i+1,len(num)):
    
       current_sum=num[i]+num[j]
       
       if current_sum==sum:
           
           print(num[i],num[j])
           
           break