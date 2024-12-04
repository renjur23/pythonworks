# sum
def sum(num1,num2):
    
    result=num1+num2
    
    print(result)
    
sum(10,20)

# substract

def sub(num1,num2):
    
    result=num1-num2
    
    print(result)
    
sub(40,20)

# multiply
def mul(num1,num2):
    
    result=num1*num2
    
    print(result)
    
mul(4,20)

# divide
def div(num1,num2):
    
    result=num1/num2
    
    print(result)   
    
div(40,20)


# last digit_max

def last_digit_max(num1,num2):
    
    num1_last_digit=num1%10
    
    num2_last_digit=num2%10
    
    print(num1_last_digit if num1_last_digit>num2_last_digit else num2_last_digit)
        
last_digit_max(123,456)
    