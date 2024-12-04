source_word=input("Enter the source word -->")

target_word=input("Enter the target word -->")

chara_count={ch:source_word.count(ch) for ch in source_word}

is_kangaro_word=True

for ch in target_word:
    
    if ch in chara_count  and chara_count.get(ch)>0 :
        
        chara_count[ch]-=1
        
    else:
        
        is_kangaro_word=False
        
print(is_kangaro_word)

# for ch in source_word:
    
#     if ch in chara_count:
        
#         chara_count[ch]+=1
    
#     else:
        
#         chara_count[ch]=1

# print(chara_count)
