lst=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
]

lst_obj=[item for item in lst if isinstance(item,list)]

print(max(lst_obj,key=len))

# for item in lst:
    
#     if isinstance(item,list):
        
#         lst_obj.append(item)
        
# print(lst_obj)