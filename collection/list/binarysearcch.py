arr=[1,2,3,4,5,7,89,12,23,24]

arr.sort()

search_element=int(input("Enter the search element :"))

lowr=0

upr=len(arr)-1



is_searchelement=False

while(lowr<=upr):
    
    mid=(upr+lowr)//2
    
    if search_element==arr[mid]:
        
        is_searchelement=True
        
        break

        
    elif search_element<arr[mid]:
         
         upr=mid-1
         
    elif search_element>arr[mid]:
        
        lowr=mid+1

print(is_searchelement)
        
        