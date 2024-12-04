num=[1,3,4,5]

num.sort()

differnce=1

for i in range(0,len(num)-1):
    
   j=i+1
   
   result=num[j]-num[i]
   
   if result!=1:
       
       print(f"Missing Number ={num[i]+1}")
       
       break
    
    