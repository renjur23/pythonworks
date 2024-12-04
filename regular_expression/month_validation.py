from re import fullmatch
month=input("Enter the month :")

pattern="([0-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

if matcher==None:
    
    print("invalid")
    
else:
    
    print("Valid")