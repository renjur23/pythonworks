# for i in range(10):
#     print(i)
    
# for j in range(10,0,-1):
#     print(j)


start=int(input("enter the start number : "))

end=int(input("enter the end number : "))

if start<end:
    
    for i in range(start,end+1,1):
        
        print(i)
        
else:
    
    for i in range(start,end-1,-1):
        
        print(i)