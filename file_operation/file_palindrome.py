f_word_read=open("D:\\Pythonworks\\datasets\\word.txt","r")

f_palindrome=open("D:\\Pythonworks\\datasets\\palindrome.txt","w")

for line in f_word_read:
    
    word=line.rstrip("\n")
    
    reversed_word=word[::-1]
    
    if word==reversed_word:
        
        f_palindrome.write(word+"\n")
        
f_word_read.close()

f_palindrome.close()