text="ABCABC"

for i in range(len(text)):
    
  for j in range(i+1,len(text)):
    
       if text[i]==text[j]:
           
        print(f"The first repeated alphabet is {text[i]}")
        
        break 
    
  break
        

              
        
            

           
