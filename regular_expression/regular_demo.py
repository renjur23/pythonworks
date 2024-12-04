from re import finditer

# text="ababababbaab"

# pattern="ab"

# matcher=finditer(pattern,text)

# for obj in matcher:
    
#     print(obj.start(),obj.group())

text="fatcatmatsatthatfast"


# pattern="at"

matcher=finditer("(at)",text)

for obj in matcher:
    
    print(obj.group())
    
    print(obj.start(),obj.group())

