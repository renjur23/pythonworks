# add

colors={"green","red","yellow"}

colors.add("blue")

print(colors)

# /////
arr=[10,20,10,30,40,50,30]

st=set()

for num in arr:
    
    st.add(num)
    
print(st)

st1={10,20,20,30,40}

st2={10,20,3,6,4,8,9,10}

inter_st=st1.intersection(st2)

print(inter_st)

union_st=st1.union(st2)

print(union_st)


dif_st=st1.difference(st2)

print(dif_st)


st2.remove(10)

print(st2)

print(st1.issubset(st2))


st3={1,2,3,4}

st4={1,2,3,4,5,6,}

print(st4.issuperset(st3))

symmteric_diff_set=st3.symmetric_difference(st4)

print(symmteric_diff_set)

st3.update(st4)

print(st3)


text="this is a test to remove the duplicate words this text is simple"

text2="this simpile text remove duplicate"

print(set(text2).issubset(set(text)))

words=text.split(" ")

print(set(words))