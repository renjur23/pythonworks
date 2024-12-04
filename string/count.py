text="pneumonoultramicroscopicsilicovolcanoconiosis"

vowels=("a","e","i","o","u")

vowels_count=0

consonants_count=0

for ch in text:
    
    if ch in vowels:
        
        vowels_count+=1
        
    else:
        
        consonants_count+=1
        
print(f"vowels count is {vowels_count} and consonants count is {consonants_count}")
        