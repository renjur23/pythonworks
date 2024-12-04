box=[
    {"color":"green","size":10},
    
    {"color":"yellow","size":4},
    
    {"color":"red","size":6}
]

# for i in box:
    
#     print(i.get("size"))
    
#     print(i.get("color"))

colors=[i.get("color") for i in box]

print(colors)