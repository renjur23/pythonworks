num=int(input("enter the number : "))

orginal=num

total=0

count=len(str(num))

print(count)

while(num!=0):
    
    digit=num%10
    
    total=total+(digit**count)
    
    num=num//10
    
print(total)

print(f"{orginal} is an armstrong number "if total==orginal else f"{orginal} is not an armstrong number")
