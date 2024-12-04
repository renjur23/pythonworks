from re import finditer

f=open("D:\\Pythonworks\\regularexpressionfile_works.py\\socialpost.txt",encoding="utf-8")

for line in f:
    
    hashtag=line.rstrip("\n")
    
    print(hashtag)
    
    pattern="#\w+"
    
    matcher=finditer(pattern,hashtag)
    
    for obj in matcher:
        
        print(obj.group())
    