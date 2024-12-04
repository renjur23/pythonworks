from re import finditer

text="i have 3cars 2bikes and 1-cycle"

# pattern=r"\w"
# pattern="\d"

# pattern="\D"

# pattern="\W"

# pattern="\s"

pattern="\S"

matcher=finditer(pattern,text)

for obj in matcher:
    
    print(obj.start(),obj.group())