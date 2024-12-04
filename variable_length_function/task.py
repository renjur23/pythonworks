def sort_num(*args,**kwargs):
    
    if kwargs.get("reverse")=="True":
        
        return sorted(args,reverse=True)
        
        
    
    if kwargs.get("reverse")=="False":
        
        return sorted(args)
        
        
        

print(sort_num(1,5,3,6,4,2,7,8,reverse="False"))


print(sort_num(1,5,2,6,4,3,7,8,reverse="True"))