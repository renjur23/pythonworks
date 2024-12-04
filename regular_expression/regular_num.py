from re import finditer

text="I have 3 cars,2 bike and 1-cycle"

# pattern="[a-zA-Z]"

# pattern="[0-9]"

# pattern="[a-zA-Z0-9]"

# pattern="[^ak0-9A-Z, /-]"

pattern="[^a-zA-Z0-9 ]"

matcher=finditer(pattern,text)

for obj in matcher:
    
    print(obj.start(),obj.group())