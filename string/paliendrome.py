# text=input("enter the text : ")

# reversed_text=text[::-1]

# print("palindrome") if text==reversed_text else print("not palindrome")

text=input("enter the text : ")

length=len(text)-1

reversed_text=""

for i in range(length,-1,-1):
    
    reversed_text+=text[i]
    
print(reversed_text)

if reversed_text==text:
    
    print("palindrome")
    
else:
    
    print("not palindrome")