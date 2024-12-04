from re import fullmatch

aadhar_number=input("Enter the aadhar number :")

pattern="[0-9]{12}"

matcher=fullmatch(pattern,aadhar_number)

if matcher==None:
    
    print("Invalid aadhar")
    
else:
    
    print("Valid aadhar number")