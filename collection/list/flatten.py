num=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

# result=[]

# for ls in num:
    
#     for n in ls:
        
#         result.append(n)
        
# print(result)

lst=[n for ls in num for n in ls]

print(lst)
        
        