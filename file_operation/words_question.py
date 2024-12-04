f=open("D:\\Pythonworks\\datasets\\sample_text.txt","r")

words=[]

count=[]

for line in f:
    
    line=line.rstrip("\n")
    
    all_words=line.split(" ")

    
    for w in all_words:
        
            
      words.append(w)

print(words)

word_count={w:words.count(w) for w in words}

nested_word=[[v,k]  for k,v in word_count.items()]

print(sorted(nested_word,reverse=True))