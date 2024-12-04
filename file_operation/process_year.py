years_path="D:\\Pythonworks\\datasets\\years.txt"

century_path="D:\\Pythonworks\\datasets\\century_yr.txt"

leap_yr_path="D:\\Pythonworks\\datasets\\leap_yr.txt"

f_read=open(years_path,"r")

f_century=open(century_path,"w")

f_leap=open(leap_yr_path,"w")

def is_century_year(year):
    
    return True  if year%100==0 else False

def is_leap_year(year):
    
    return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False


for year in f_read:
    
    year=int(year)
    
    if year%100==0:
        
        f_century.write(str(year)+"\n")
        
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        
        f_leap.write(str(year)+"\n")
        

f_read.close()

f_century.close()

f_leap.close()
    
    
        
