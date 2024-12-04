# pattern printing
#   * * *
#   * * * 
#   * * *


for row in range(1,5):
    
    
    for col in range(1,4):
        
        print("*",end=" \t")
        
    print()
    
# $

# $ $

# $ $ $

# $ $ $ $
  
  
for row in range(1,5):
    
    for col in range(1,row):
        
        print("$",end=" \t")
    
    print()
    
    
# 1
# 2 2
# 3 3 3
# 4 4 4 4

end=int(input("enter the end number : "))

for row in range(1,end+1):
    
    for col in range(1,row+1):
        
        print(row,end=" \t")
        
    print()
    
    
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for row in range(1,6):
    
    for col in range(1,row+1):
        
        print(col,end=" \t")
        
    print()
    
# * * * * *

# * * * *

# * * * 

# * * 

# *

for row in range(5,0,-1):
    
    for col in range(1,row+1):
        
        print("*",end=" \t")
        
    print()
    
#      *
#    *   *
#  *   *   * 
# *  *    *   *

