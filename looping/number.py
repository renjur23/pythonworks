start=int(input("enter the start number : "))

end=int(input("enter the end number : "))

reverse=True if start>end else False

print(reverse)

i=start

while(i<=end if reverse==False else i>=end):
    
    if i%2==0:
        
        print(i)
    
    if reverse==False:
        
        i=i+1
        
    else:
        
        i=i-1
