# largest number

# num1=int(input("enter the first number1 : "))

# num2=int(input("enter the second number2 : "))

# num3=int(input("enter the third number3 : "))

# if num1> num2 and num1> num3:
    
#     print(f"{num1} is the largest number")
    
# elif num2> num1 and num2> num3: 
    
#     print(f"{num2} is the largest number")
    
# elif num3> num1 and num3> num2:
    
#     print(f"{num3} is the largest number")  
    
# elif num1== num2 and num1== num3:
    
#     print(f" three numbers are equal")

# second largest number


num1=int(input("enter the first number1 : "))

num2=int(input("enter the second number2 : "))

num3=int(input("enter the third number3 : "))

if num1> num2 and num1> num3:
    
    if num2>num3:
    
      print(f"{num2} is the  second largest number")
      
      print(f" the sorted numbers are {num1},{num2},{num3}")
      
    else:
        
        print(f"{num3} is the second largest number")
        
        print(f" the sorted numbers are {num1},{num3},{num2}")
    
elif num2> num1 and num2> num3: 
    
    if num1>num3:
    
      print(f"{num1} is the second largest number")
      
      print(f" the sorted numbers are {num2},{num1},{num3}")
      
    else:
        
        print(f"{num3} is the second largest number")
        
        print(f" the sorted numbers are {num2},{num3},{num1}")
    
elif num3> num1 and num3> num2:
    
   if num1>num2:
    
      print(f"{num1} is the  second largest number")
      
      print(f" the sorted numbers are {num3},{num1},{num2}")
      
   else:
        
        print(f"{num2} is the second largest number")
        
        print(f" the sorted numbers are {num3},{num2},{num1}")
        
elif num1== num2 and num1== num3:
    
    print(f" three numbers are equal")

