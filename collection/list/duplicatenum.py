arr=[1,2,2,2,1,4,5]

arr.sort()

dupllicate_num=[]

for i in range(0,len(arr)-1):
    
    j=i+1
    
    result=arr[j]-arr[i]
    
    if result==0:
        
        if arr[i] not in dupllicate_num:
            
            dupllicate_num.append(arr[i])
        
        

     
print(f"The duplicate numbers are {dupllicate_num}")
    
    
    
    
    
    