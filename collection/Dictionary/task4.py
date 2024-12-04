user_input=input("enter the pair of brackets = ")

symbol_dictionary={"{":"}",
               "(":")",
               "[":"]",
               "<":">"
               }

top=-1

symbol_stack=[]

is_vaild=True

for symbol in user_input:
    
    if symbol in symbol_dictionary:
        
        top+=1
        
        symbol_stack.append(symbol)
        
    elif top==-1:
        
        is_vaild=False
        
    elif symbol==symbol_dictionary.get(symbol_stack[top]):
        
        top=top-1
        
        symbol_stack.pop()
        
    else:
        
        is_vaild=False
        
if len(symbol_stack)==0 and is_vaild==True:
        
    print("Valid")

else:
    
    print("Invalid ")