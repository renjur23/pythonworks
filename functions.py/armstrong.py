def armstrong(num):

    orginal=num
    
    total=0
    
    count=len(str(num))
    
    while(num!=0):
        
        digit=num%10
        
        total=total+(digit**count)
        
        num=num//10
        
    return(f"{orginal} is an armstrong number "if total==orginal else f"{orginal} is not an armstrong number")


num=int(input("enter the number : "))

print(armstrong(num))
    