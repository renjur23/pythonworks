from re import fullmatch

mobile_number=input("Enter the mobile number:")

# pattern="[0-9]{10}"
# pattern="(91)?[0-9]{10}"
pattern="(91)+[0-9]{10}"

matcher=fullmatch(pattern,mobile_number)

if matcher==None:
    
    print("Invalid mobile number")

else:
    
    print("valid mobile number")