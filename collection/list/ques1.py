arr=[100,200,300,400,500]

k=int(input("Enter the no of rotations :"))

for i in range(1,k+1):
    
    popped_element=arr.pop()
    
    arr.insert(0,popped_element)

print(arr)


color1=["red","green","blue"]

color2=color1.copy()

color2.pop()

print(color2)

# sort

lst=[2,5,3,6,4,9]

lst.sort()

print(lst)

lst.sort(reverse=True)

print(lst)