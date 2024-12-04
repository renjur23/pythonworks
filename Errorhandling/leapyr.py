def leap_year(year):
    
    if year<0:
        
        return False
    
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        
        return True
        
        # print(f"{year} is leap year")
    
    else:
        
        # print(f"{year} is not a leap year")
        
        return False



def test_leap_year():
    
    assert leap_year(2024)==True,"non century year test failed"
    
    assert leap_year(2025)==False,"invalid non century year test failed"
    
    assert leap_year(2000)==True,"century leap year test failed"
    
    assert leap_year(1900)==False,"invalid century year test failed"
    
    assert leap_year(-2029)==False,"invalid year test failed"
    
    
try:
    
    test_leap_year()
    
    print("test passed")
    
except Exception as e:
    
    print(e)