# text1="PQRS"

# text2="ABCD"

# result=""


# for i in range(0,4):
    
#     result+=text1[i]+text2[i]
    
# print(result)



text3="PQRST"

text4="ABC"

output=""

smallest_text= text3 if text3<text4 else text4

print(smallest_text)

largest_txt=text3 if text3>text4 else text4

print(largest_txt)



for i in range(0,len(smallest_text)):
    
    output+=text3[i]+text4[i]
    
print(output)

balance_txt=largest_txt[len(smallest_text):]

merged_txt=output+balance_txt

print(merged_txt)



