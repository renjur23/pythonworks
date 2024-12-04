num=[5,2,3,9]

cubes=[i**3 for i in num]

print(cubes)


odd=[i for i in num if i%2!=0]

print(odd)

new_num=[i+1 if i>5 else i-1 for i in num]

print(new_num)

