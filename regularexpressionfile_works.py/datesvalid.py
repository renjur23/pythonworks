from re import findall

f=open("D:\\Pythonworks\\regularexpressionfile_works.py\\dates.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dates=findall(pattern,content)

for date in all_dates:
    
    print(date)

