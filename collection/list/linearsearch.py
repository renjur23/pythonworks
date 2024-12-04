arr=[5,7,8,9,6,1,2,3,4]

search_element=int(input("Enter the number :"))

is_search=False

for i in range(0,len(arr)):
    
    if search_element==arr[i]:
        
        is_search=True
        
        break
print(is_search)