from re import fullmatch

user_input=input("enter a variable:")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

# start with upper or lower case
#any number of alphabets,numbers,_
 
if matcher==None:
    
    print("Invalid Variable")

else:
    
    print("Valid Variable")
    
    