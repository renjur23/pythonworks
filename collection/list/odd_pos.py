arr=[100,200,300,400,500,600,700,800]

# odd_pos_elements=[num for index,num in enumerate(arr) if index%2!=0]


# odd_pos_elements.reverse()

# print(odd_pos_elements)

# i=1

# for index,num in enumerate(odd_pos_elements):
    
#     arr[i]=num
    
#     i+=2
    
# print(arr)

# another method

left=1

right=len(arr)-1

if right%2==0:
    
    right-=1
    
while(left<right):
    
    arr[left],arr[right]=arr[right],arr[left]
    
    left+=2
    
    right-=2
    
print(arr)





