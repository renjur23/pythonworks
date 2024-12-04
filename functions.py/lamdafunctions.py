# # add=lambda num1,num2:num1+num2

# # print(add(20,40))

# # sub=lambda num3,num4:num3+num4

# # print(sub(30,10))

# # cube=lambda n1:n1**3

# # print(cube(9))

# # square=lambda n2:n2**2

# # print(square(16))

# # max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

# # print(max_two("hello","python"))

# # min_two=lambda str3,str4:str3 if len(str3)<len(str4) else str3

# # print(min_two("hello","python"))

# smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

# print(smart_sub(30,50))


# words=["hai","hi","python","developer"]

# get_length=lambda word:len(word)

# print(max(words,key=get_length))

# # def get_length(words):
    
# #     return len(words)

# # print(max(words,key=get_length))

# get_min_length=lambda word:len(word)

# print(min(words,key=get_min_length))


# text="this is a sample program to find the maximum character in the given sentense"

# spilted_text=text.split(" ")

# max_char=lambda chara:len(chara)

# print(max(spilted_text,key=max_char))


# sample=["hi","world","lambda","python","hello"]

# srt_word=lambda word:len(word)

# print(sorted(sample,key=srt_word))

# print(sorted(sample,key=srt_word,reverse=True))

# def get_length(w):
    
#     return len(w)

# srt_word=sorted(sample,key=get_length,reverse=True)

# print(srt_word)

text="this is the sample python program to check the most repeated word in the given text"

word=text.split(" ")

def get_count(w):
    
    return  word.count(w)

most_recursive_word=max(word,key=get_count)

print(most_recursive_word)

