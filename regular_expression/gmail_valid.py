from re import fullmatch

mail_id=input("Enter mailid :")

pattern="[a-z]+[a-z0-9]{5,63}?@gmail.com"

matcher=fullmatch(pattern,mail_id)

print("invalid "if matcher==None else "valid")
    
