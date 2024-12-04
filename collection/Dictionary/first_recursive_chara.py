text="ABBAC"

first_recursive_chara={}

for ch in text:
    
    if ch in first_recursive_chara:
        
        print(f"the recursive character in the given text is  {ch}")
        
        break
    
    else:
        
        first_recursive_chara[ch]=1
        

