from re import  fullmatch

vehicle_number=input("Enter the vehicle number :")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,vehicle_number)

if matcher==None:
    
    print("Invalid Vehicle number")
    
else:
    
    print("Valid Vehicle number")