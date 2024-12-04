# text="ABBABBCCAAEDF"

# word_occurance={o:text.count(o) for o in text}

# print(word_occurance)
# # for k,v in word_occurance.items():
    
# #     if v==1:
        
# #         print(k)

# non_recursive__char={k for k,v in word_occurance.items() if v==1}

# print(non_recursive__char)

words=["hello","hai","hello","hai","hi","hai"]

word_count={w:words.count(w) for w in words}

print(word_count)

recursive_words={k for k,v in word_count.items() if v>1}

print(recursive_words)

non_recursive_words={k for k,v in word_count.items() if v==1}

print(non_recursive_words)

highest_count=0

most_recursive_word={}

for k,v in word_count.items():
    
    if v>highest_count:
        
         highest_count=v
        
         most_recursive_word={k:v}
         
        
        
    
print(most_recursive_word)


