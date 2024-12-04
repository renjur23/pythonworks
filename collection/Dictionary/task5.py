lst1=["apple","mango","orange","kiwi"]

lst2=[100,200]

fruits={}

for i in range(0,len(lst2)):
    
    list_one_element_index=lst1[i]
    
    list_two_element_index=lst2[i]
    
    fruits[list_one_element_index]=list_two_element_index
    
print(fruits)

balance_element=lst1[len(lst2):]

for index,element in enumerate(balance_element):
    
    fruits[element]=index+1
    
print(fruits)
    
    