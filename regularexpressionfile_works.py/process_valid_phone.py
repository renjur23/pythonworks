from re import fullmatch

f=open("D:\\Pythonworks\\regularexpressionfile_works.py\\phone_num.txt")

for line in f:
    
    phone=line.rstrip("\n")
    
    pattern="(91)?[0-9]{10}"
    
    matcher=fullmatch(pattern,phone)
    
    if matcher!=None:
        
        print(phone)