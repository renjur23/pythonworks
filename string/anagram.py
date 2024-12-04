source_word=input("enter the source word : ")

target_word=input("enter the target word : ")

is_anagram=True

for ch in source_word:
    
    if ch not in target_word:
        
        is_anagram=False
        
        break
        
print(is_anagram)