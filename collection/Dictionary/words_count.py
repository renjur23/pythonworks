words=["hai","hello","hello","hi","hai"]

# words="this is a sample program to  count the number od words.this is a python program"

words_count={}

for w in words:
    
    if w in words_count:
        
        words_count[w]+=1
        
    else:
        
        words_count[w]=1
        
print(words_count)
        
        