# text="helloworld"

# result=text.capitalize()

# print(result)

# text1="HelloWorld"

# result1=text1.casefold()

# print(result1)

# text2="HelloWorld"

# result2=text2.isalpha()

# print(result2)

# text3="HelloWorld12"

# result3=text3.isalnum()

# print(result3)


# text4="123"

# result4=text4.isdigit()

# print(result4)

# text5="HelloWorld"

# result5=text5.startswith("He")

# print(result5)

# result6=text5.endswith("ld")

# print(result6)

# for ch in text5:
    
#     print(ch)
    
# test="HelloWorld"

# vowels="aeiou"

# for ch in test:
    
#     if ch in vowels:
        
#         print(ch)    



# text="hello,world,python"

# result=text.split(" ")

# print(result)

# task="\t helloworld \tpython \t"

# new_task=task.strip("\t")

# print(new_task)

task1="\t helloworld \tpython \t"

# new_task1=task1.lstrip("\t")

new_task1=task1.rstrip("\t")

print(new_task1)

test="hello,world,python"

result=test.replace("o","a",2)

print(result)


# slicing

# test1="python programming"

# print(test1[0:6])

# print(test1[7::])

# print(test1[::2])

# print(test1[::-1])

# test2="hello,world,python"

# print(test2.index("o"))

# text="renjurenjith@gmail.com"   

# index=text.index("@")

# print(index)

# print(text[:index])

# print(text[:text.index("@")])


test="hellopython"

index_o=test.index("o")

reversed_sub_str=test[index_o-1::-1]

balanced_sub_str=test[index_o:]

result=reversed_sub_str+balanced_sub_str

print(result)

        