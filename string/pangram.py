text=" The quick brown fox jumps over the lazy dog" 

all_letters="abcdefghijklmnopqrstuvwxyz"

is_pangram=True

for ch in all_letters:
    
    if ch not in text:
        
        is_pangram=False
        
        break
        
print(is_pangram)