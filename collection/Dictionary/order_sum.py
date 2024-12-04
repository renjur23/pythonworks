orders=["tea","coffee","juice","tea","juice","coffee","dosa"]

order_summery={}

for items in orders:
    
    if items in order_summery:
        
        order_summery[items]+=1
        
    else:
        
        order_summery[items]=1
        
print(order_summery)