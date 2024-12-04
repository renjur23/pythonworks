def multiplication_table(number,limit):
    
    for  i in range(1,limit+1):
        
        print(f"{i} X {number}   = {i*number}")   

number=int(input("enter the number : "))    

limit=int(input("enter the limit : "))

multiplication_table(number,limit)