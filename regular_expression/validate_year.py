# validate year from 1800 -2024
from re import fullmatch

year=input("Enter the Year :")

pattern="((18|19)[0-9]{2}|200[0-9]|201[0-9]{1}|202[0,4])"

matcher=fullmatch(pattern,year)

if matcher==None:
    
    print("Invaild year")
    
else:
    
    print("Valid year")