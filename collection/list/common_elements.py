arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

# common elements with out using in

# for i in range(0,len(arr1)):
    
#     for j in range(0,len(arr2)):
        
#         if arr1[i]==arr2[j]:
            
#             print(f"the common element is{arr1[i]}")
            
            
# or

arr1.sort()

arr2.sort()

p1=0

p2=0

while (p1<len(arr1)) and p2<len(arr2):
    
    if arr1[p1]==arr2[p2]:
        
        common_element=arr1[p1]
        
         
        print(common_element)
        
        p1+=1
        
        p2+=1
       
        
    elif arr1[p1]<arr2[p2]:
        
        p1+=1
        
    elif arr1[p1>arr2[p2]]:
        
        p2+=1
        
