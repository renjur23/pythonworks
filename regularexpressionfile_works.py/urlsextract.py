from re import findall

f=open("D:\\Pythonworks\\regularexpressionfile_works.py\\urls.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:
    
    print(url)