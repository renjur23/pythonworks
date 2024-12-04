def poll(age):
    
    assert age>18,"invalid age"
    
    print("voted")
    
try:
    
    poll(14)
    
except Exception as e:
    
    print(e)
    

def review(rating):
    
    assert rating>0,"bad review"
    
    assert rating in range(0,11),"too high"
    
    print("rated")
    
review(-1)